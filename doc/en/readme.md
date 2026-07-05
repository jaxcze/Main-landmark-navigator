# Main Landmark Navigator

**Version:** 1.0.1  
**Author:** 2026 Jan Balák & Claude  
**License:** GNU General Public License, version 2  
**Minimum NVDA version:** 2025.3  
**Tested with NVDA:** 2026.1  
**Download:** <https://janbalak.name>

---

## Description

Main Landmark Navigator adds single-key quick navigation for the `<main>`
ARIA landmark (also written as `role="main"`) on web pages.

NVDA already lets you navigate between *all* ARIA landmarks using **Comma**
(next) and **Shift+Comma** (previous). This add-on complements that by giving
you a dedicated key pair that moves *exclusively* between main-content areas —
just like **H / Shift+H** works only for headings.

`<main role="main">` is treated identically to `<main>` because browsers
expose both to NVDA in exactly the same way: one landmark with role *main*.

---

## Installation

1. Download `mainLandmarkNavigator-1.0.0.nvda-addon`.
2. Open the file (Enter or double-click) while NVDA is running, or choose
   **NVDA menu → Tools → Manage add-ons → Install** and browse to the file.
3. Confirm the installation prompt.
4. Restart NVDA when asked.

---

## Usage

| Key | Action |
|-----|--------|
| **J** | Move to the **next** main region on the page |
| **Shift+J** | Move to the **previous** main region on the page |

Both keys work **only while NVDA's browse mode is active** (i.e., when you are
reading a web page, not when a form field or other interactive element has
focus in pass-through mode). In any other context the key is forwarded
transparently to the application.

When a main region is found, NVDA announces its contents using the same
speech/braille output as the built-in quick-navigation commands.

When no main region exists in the requested direction, NVDA announces:
- *"No next main region"*
- *"No previous main region"*

---

## Changing the keyboard shortcuts

1. Open **NVDA menu → Preferences → Input Gestures…**
2. In the search box type *main* or browse to the **Browse mode** category.
3. Select *Moves to the next main region on the web page* or the previous
   variant and press **Add** to assign a new key, or **Remove** to clear it.
4. Press **OK** to save.

---

## Compatibility

| Browser | Engine | Status |
|---------|--------|--------|
| Firefox | IAccessible2 (Gecko) | ✅ Supported |
| Google Chrome | UIA / IAccessible2 | ✅ Supported |
| Microsoft Edge | UIA | ✅ Supported |
| Chromium-based browsers | UIA / IAccessible2 | ✅ Supported |

The add-on relies on `VirtualBuffer._iterNodesByType("landmark", ...)`, which
is the same internal API used by NVDA's own quick-navigation commands.

---

## Known limitations

- The add-on navigates only in the **virtual buffer** (browse mode). In
  applications that expose ARIA landmarks through UIA without a virtual buffer
  (e.g., some Microsoft Office components) it has no effect.
- If a page has no `<main>` element, the appropriate "no next / previous"
  message is announced and the cursor stays at its current position.

---

## Changelog

### 1.0.1 (2026-07-03)
- Fixed: `url` field in `manifest.ini` now points directly to the add-on's presentation page (required by the NVDA Add-on Store).

### 1.0.0 (2026-06-29)
- Initial release.
- J / Shift+J quick navigation for `<main>` and `role="main"` landmarks.
- Translations: English, Czech, Slovak, German.
- Minimum NVDA version: 2025.3; tested on 2026.1.
