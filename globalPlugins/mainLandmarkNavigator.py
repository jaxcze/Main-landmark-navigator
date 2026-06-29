# -*- coding: utf-8 -*-
# Main Landmark Navigator — NVDA global plugin
# Copyright (C) 2026 Jan Balák & Claude
# Released under the GNU General Public License, version 2.
#
# Navigates between <main> / role="main" landmarks on web pages
# using J (next) and Shift+J (previous) in NVDA browse mode.
#
# Architecture notes
# ------------------
# 1. No @script decorator — uses __gestures dict + __doc__ + .category.
#    This is the oldest, most portable NVDA script-registration pattern.
#
# 2. All imports of virtualBuffers, speech, textInfos, controlTypes are
#    deferred (inside functions) so module load is clean and fast.
#
# 3. _navigate_main_landmark uses broad `except Exception` for every
#    NVDA API call.  Narrow except clauses (TypeError, AttributeError)
#    missed runtime and NVDA-internal errors, causing the script to
#    exit silently — no movement, no announcement, no error message.
#
# 4. Speech is triggered EXPLICITLY via speech.cancelSpeech() +
#    speech.speakTextInfo() after moving the cursor, so we never depend
#    on _set_selection() speaking internally (its behaviour varies across
#    NVDA versions and configurations).
#
# 5. <main role="main"> == <main> at the browser/NVDA level (one VBuf
#    node, fieldAttributes["landmark"] == "main").  No special handling.

import globalPluginHandler
import api
import ui
import addonHandler

addonHandler.initTranslation()

# Reuse NVDA's own "Browse mode" category constant so our scripts appear
# in the same Input Gestures category as H, L, T, Comma, etc.
try:
    from browseMode import SCRCAT_BROWSEMODE as _CATEGORY
except (ImportError, AttributeError):
    _CATEGORY = _("Browse mode")


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _is_main_landmark(item):
    """Return True if *item* (a QuickNavItem) is a 'main' ARIA landmark.

    Checks the C++ VBuf node's fieldAttributes first (fast, no GC pressure),
    then falls back to NVDAObject.landmark (slower Python path).
    Case-insensitive comparison guards against potential future casing changes.
    """
    # Fast path – C++ VBuf node attribute
    vbuf_node = getattr(item, "vBufNode", None)
    if vbuf_node is not None:
        try:
            attrs = vbuf_node.fieldAttributes
            # Primary key is "landmark"; "landmarkRole" tried as fallback
            landmark = (attrs.get("landmark") or attrs.get("landmarkRole") or "")
            if landmark.strip().lower() == "main":
                return True
        except Exception:
            pass

    # Fallback – NVDAObject.landmark property
    try:
        obj = item.obj
        if obj is not None:
            landmark = getattr(obj, "landmark", "") or ""
            if landmark.strip().lower() == "main":
                return True
    except Exception:
        pass

    return False


def _navigate_main_landmark(tree_interceptor, direction):
    """Move the browse-mode caret to the next / previous <main> element.

    Uses VirtualBuffer._iterNodesByType("landmark", ...) — the same
    C++ node-tree traversal that NVDA's built-in quick-nav commands use.
    Filters the results to landmark == "main" via _is_main_landmark().

    Speech is triggered explicitly after cursor movement so the function
    does not depend on _set_selection()'s internal behaviour.

    :param tree_interceptor: Active VirtualBuffer instance.
    :param direction: ``"next"`` or ``"previous"``.
    """
    # All heavy NVDA imports deferred to avoid slowing module startup.
    import controlTypes
    import textInfos
    import speech

    # --- Current caret position ------------------------------------------
    try:
        caret = tree_interceptor.selection
        caret.collapse()
    except Exception:
        return

    if direction == "next":
        # Translators: Announced when there is no next main region on the page.
        error_msg = _("No next main region")
    else:
        # Translators: Announced when there is no previous main region on the page.
        error_msg = _("No previous main region")

    # --- Iterate landmarks in the requested direction ---------------------
    try:
        node_iter = tree_interceptor._iterNodesByType("landmark", direction, caret)
    except Exception:
        ui.message(error_msg)
        return

    for item in node_iter:
        if not _is_main_landmark(item):
            continue  # Skip navigation, search, banner, etc.

        # --- Get text info for this landmark -----------------------------
        try:
            target = item.textInfo
            target.collapse()   # Caret to the very START of <main>
        except Exception:
            continue            # Node became stale; try the next match

        # --- Move the virtual cursor -------------------------------------
        # We use broad `except Exception` because _set_selection() can
        # raise NVDA-internal errors beyond TypeError/AttributeError.
        # Either path below is acceptable; we just need the cursor to move.
        try:
            tree_interceptor._set_selection(
                target,
                reason=controlTypes.OutputReason.QUICKNAV,
            )
        except Exception:
            try:
                tree_interceptor.selection = target
            except Exception:
                pass    # Cursor didn't move, but we still announce below

        # --- Announce the new position -----------------------------------
        # We ALWAYS call speech explicitly and do NOT rely on _set_selection
        # to trigger speech internally (that behaviour is version-dependent).
        #
        # speech.cancelSpeech() interrupts any ongoing or queued speech
        # (e.g. from a partial _set_selection announcement) so the user
        # hears exactly ONE announcement — the landmark and its first line.
        #
        # reason=QUICKNAV causes speakTextInfo to announce control-field
        # properties (role, state) as the cursor enters/exits elements,
        # so the user hears "main landmark" followed by the first-line text.
        try:
            speech.cancelSpeech()
            read_info = target.copy()
            read_info.expand(textInfos.UNIT_LINE)
            speech.speakTextInfo(
                read_info,
                unit=textInfos.UNIT_LINE,
                reason=controlTypes.OutputReason.QUICKNAV,
            )
        except Exception:
            # Absolute fallback: at least tell the user we found something
            # Translators: Fallback announced when the main region is found
            # but the full speech output fails.
            ui.message(_("Main region"))

        return  # Done — one landmark processed

    # --- No landmark found -----------------------------------------------
    ui.message(error_msg)


def _get_virtual_buffer():
    """Return the active VirtualBuffer if NVDA is in browse mode, else None.

    Returns None when:
    - No focus object is available
    - The tree interceptor is not a VirtualBuffer (non-web context)
    - passThrough is True (form field / interactive element has focus)
    """
    try:
        import virtualBuffers
        focus = api.getFocusObject()
        if focus is None:
            return None
        ti = getattr(focus, "treeInterceptor", None)
        if not isinstance(ti, virtualBuffers.VirtualBuffer):
            return None
        if ti.passThrough:
            return None
        return ti
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Global Plugin
# ---------------------------------------------------------------------------

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """Main Landmark Navigator.

    Provides J / Shift+J quick navigation for the 'main' ARIA landmark
    (<main> and role="main") on web pages, analogous to H / Shift+H for
    headings.  The keys are forwarded unchanged to the system in all
    non-browse-mode contexts (desktop apps, form fields, etc.).
    """

    # ------------------------------------------------------------------
    # Scripts
    # ------------------------------------------------------------------

    def script_nextMainLandmark(self, gesture):
        ti = _get_virtual_buffer()
        if ti is None:
            gesture.send()
            return
        _navigate_main_landmark(ti, "next")

    def script_previousMainLandmark(self, gesture):
        ti = _get_virtual_buffer()
        if ti is None:
            gesture.send()
            return
        _navigate_main_landmark(ti, "previous")

    # __doc__ is assigned AFTER the function definitions so _() is
    # guaranteed to be set up by addonHandler.initTranslation() above.
    # Translators: Description in the NVDA Input Gestures dialog.
    script_nextMainLandmark.__doc__ = _(
        "Moves to the next main region on the web page"
    )
    # Translators: Description in the NVDA Input Gestures dialog.
    script_previousMainLandmark.__doc__ = _(
        "Moves to the previous main region on the web page"
    )

    # Place scripts under "Browse mode" in the Input Gestures dialog
    # (same category as H, L, T, Comma, …).
    script_nextMainLandmark.category = _CATEGORY
    script_previousMainLandmark.category = _CATEGORY

    # ------------------------------------------------------------------
    # Default gesture bindings — user-overridable via Input Gestures.
    # __gestures is the most portable NVDA gesture-binding mechanism:
    # read directly from the class MRO with no decorator magic.
    # ------------------------------------------------------------------
    __gestures = {
        "kb:j":         "nextMainLandmark",
        "kb:shift+j":   "previousMainLandmark",
    }
