# -*- coding: utf-8 -*-
# Main Landmark Navigator — NVDA global plugin
# Copyright (C) 2026 Jan Balák & Claude
# Released under the GNU General Public License, version 2.
#
# Navigates between <main> / role="main" landmarks on web pages
# using J (next) and Shift+J (previous) in NVDA browse mode.
#
# Architecture
# ------------
# Scripts are injected into the VirtualBuffer CLASS (not a GlobalPlugin),
# so they behave identically to NVDA's built-in H/L/T quick-nav keys:
#
#   • Active only while browse mode is on (passThrough == False).
#     When pass-through is active (form fields), the VirtualBuffer does
#     not process gestures at all — no gesture.send() needed.
#   • Input help (NVDA+1) announces the script description ONLY when a
#     VirtualBuffer is the active tree interceptor, not in desktop apps.
#   • Gestures are added to _VirtualBuffer__gestures in __init__ and
#     removed in terminate(), leaving the class clean after uninstall.
#
# NVDA version compatibility
# --------------------------
# Minimum: 2019.3 (script decorator; VirtualBuffer API stable since then).
# controlTypes.OutputReason was introduced in 2021.1; pre-2021.1 NVDA
# used string-based speech reasons. We detect and adapt at import time.

import globalPluginHandler
import api
import ui
import addonHandler

addonHandler.initTranslation()

# ── OutputReason compatibility ──────────────────────────────────────────────
# NVDA 2021.1+ → controlTypes.OutputReason enum.
# Older NVDA  → speech.REASON_* string constants.
try:
    import controlTypes
    _REASON_QUICKNAV = controlTypes.OutputReason.QUICKNAV
except AttributeError:
    try:
        import speech as _s
        _REASON_QUICKNAV = getattr(_s, 'REASON_QUICKNAV',
                           getattr(_s, 'REASON_FOCUS', 'focus'))
    except Exception:
        _REASON_QUICKNAV = 'focus'

# ── Script category ─────────────────────────────────────────────────────────
# Import NVDA's own "Browse mode" category string so our scripts appear
# in the same Input Gestures group as H, L, T, Comma …
try:
    from browseMode import SCRCAT_BROWSEMODE as _CATEGORY
except (ImportError, AttributeError):
    _CATEGORY = _('Browse mode')


# ── Private helpers ──────────────────────────────────────────────────────────

def _is_main_landmark(item):
    """Return True if *item* (QuickNavItem) is a 'main' ARIA landmark."""
    # Fast path — C++ VBuf node fieldAttributes
    vbuf_node = getattr(item, 'vBufNode', None)
    if vbuf_node is not None:
        try:
            attrs = vbuf_node.fieldAttributes
            landmark = attrs.get('landmark') or attrs.get('landmarkRole') or ''
            if landmark.strip().lower() == 'main':
                return True
        except Exception:
            pass
    # Fallback — NVDAObject.landmark property
    try:
        obj = item.obj
        if obj is not None:
            landmark = getattr(obj, 'landmark', '') or ''
            if landmark.strip().lower() == 'main':
                return True
    except Exception:
        pass
    return False


def _navigate_main_landmark(tree_interceptor, direction):
    """Move the browse-mode caret to the next / previous <main> element.

    :param tree_interceptor: Active VirtualBuffer instance (== self when
                             called from a VirtualBuffer-injected script).
    :param direction: ``'next'`` or ``'previous'``.
    """
    import textInfos
    import speech

    try:
        caret = tree_interceptor.selection
        caret.collapse()
    except Exception:
        return

    if direction == 'next':
        # Translators: Announced when there is no next main region on the page.
        error_msg = _('No next main region')
    else:
        # Translators: Announced when there is no previous main region on the page.
        error_msg = _('No previous main region')

    try:
        node_iter = tree_interceptor._iterNodesByType('landmark', direction, caret)
    except Exception:
        ui.message(error_msg)
        return

    for item in node_iter:
        if not _is_main_landmark(item):
            continue

        try:
            target = item.textInfo
            target.collapse()
        except Exception:
            continue

        # Move the virtual cursor — broad except catches NVDA-internal errors
        # that are more specific than TypeError/AttributeError.
        try:
            tree_interceptor._set_selection(target, reason=_REASON_QUICKNAV)
        except Exception:
            try:
                tree_interceptor.selection = target
            except Exception:
                pass

        # Announce explicitly; do not rely on _set_selection speaking.
        try:
            speech.cancelSpeech()
            read_info = target.copy()
            read_info.expand(textInfos.UNIT_LINE)
            speech.speakTextInfo(
                read_info,
                unit=textInfos.UNIT_LINE,
                reason=_REASON_QUICKNAV,
            )
        except Exception:
            # Translators: Fallback announced when the main region is found
            # but full speech output fails.
            ui.message(_('Main region'))

        return

    ui.message(error_msg)


# ── VirtualBuffer script functions ───────────────────────────────────────────
# These are injected into virtualBuffers.VirtualBuffer in GlobalPlugin.__init__
# so they behave exactly like NVDA's built-in quick-nav scripts.
# 'self' inside these functions is the VirtualBuffer instance.

def _vbuf_next(self, gesture):
    _navigate_main_landmark(self, 'next')

def _vbuf_prev(self, gesture):
    _navigate_main_landmark(self, 'previous')

# Assign translatable __doc__ and category NOW (after initTranslation).
# Translators: Description shown in the NVDA Input Gestures dialog.
_vbuf_next.__doc__ = _('Moves to the next main region on the web page')
# Translators: Description shown in the NVDA Input Gestures dialog.
_vbuf_prev.__doc__ = _('Moves to the previous main region on the web page')
_vbuf_next.category = _CATEGORY
_vbuf_prev.category = _CATEGORY


# ── Global Plugin ────────────────────────────────────────────────────────────

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """Main Landmark Navigator.

    Injects J / Shift+J browse-mode quick-navigation scripts into the
    VirtualBuffer class so they are active and announced (in input help)
    only while NVDA's browse mode is engaged — identical behaviour to
    the built-in H / Shift+H heading navigation.
    """

    def __init__(self):
        super().__init__()
        import virtualBuffers

        # ── Inject script methods ──────────────────────────────────────
        virtualBuffers.VirtualBuffer.script_nextMainLandmark     = _vbuf_next
        virtualBuffers.VirtualBuffer.script_previousMainLandmark = _vbuf_prev

        # ── Bind gestures at class level ───────────────────────────────
        # NVDA's ScriptableObject reads _ClassName__gestures from each
        # class in the MRO via cls.__dict__.get('_ClassName__gestures').
        # Setting _VirtualBuffer__gestures on the class dict is the same
        # as writing  __gestures = {...}  inside the class body.
        existing = dict(
            getattr(virtualBuffers.VirtualBuffer, '_VirtualBuffer__gestures', {})
        )
        existing['kb:j']       = 'nextMainLandmark'
        existing['kb:shift+j'] = 'previousMainLandmark'
        virtualBuffers.VirtualBuffer._VirtualBuffer__gestures = existing

    def terminate(self):
        """Remove injected scripts and gesture bindings on unload."""
        try:
            import virtualBuffers

            for name in ('script_nextMainLandmark', 'script_previousMainLandmark'):
                try:
                    delattr(virtualBuffers.VirtualBuffer, name)
                except AttributeError:
                    pass

            gestures = dict(
                getattr(virtualBuffers.VirtualBuffer, '_VirtualBuffer__gestures', {})
            )
            gestures.pop('kb:j', None)
            gestures.pop('kb:shift+j', None)
            virtualBuffers.VirtualBuffer._VirtualBuffer__gestures = gestures
        except Exception:
            pass

        super().terminate()
