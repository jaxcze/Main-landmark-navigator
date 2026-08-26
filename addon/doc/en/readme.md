# Main Landmark Navigator

**Version:** 1.0.4
**Author:** 2026 Jan Balák
**License:** GNU General Public License, version 2
**Minimum NVDA version:** 2019.3
**Tested with NVDA:** 2026.1
**Download:** <https://nvda-addons.janbalak.name/main-landmark-navigator/>

## Description

Main Landmark Navigator adds single-key quick navigation for the `<main>` ARIA landmark (also written as `role="main"`) on web pages — like H / Shift+H for headings, but focused exclusively on the main content area.

## Installation

1. Download `mainLandmarkNavigator-1.0.4.nvda-addon`.
2. Open the file while NVDA is running and confirm the installation.
3. Restart NVDA when asked.

## Usage

| Key | Action |
|-----|--------|
| **J** | Move to the **next** main region |
| **Shift+J** | Move to the **previous** main region |

Keys only activate in NVDA browse mode. In form fields, desktop applications, or any non-browse-mode context the key is forwarded transparently. Input help (NVDA+1 then J) only describes the shortcut when browse mode is active.

`<main role="main">` is treated identically to `<main>` — browsers expose both as a single landmark with role *main*.

When no main region exists in the requested direction, NVDA announces:

- *No next main region*
- *No previous main region*

## Changing keyboard shortcuts

Open **NVDA menu → Preferences → Input Gestures**, search for *main*, find the commands under the **Browse mode** category and reassign as needed.

## Changelog

### 1.0.4 (2026-08-26)
- Fixed: author/copyright metadata (manifest, source header, translation templates, per-language readmes) no longer credits an AI assistant as a co-author — attributed to Jan Balák alone. No functional change.

### 1.0.3 (2026-08-22)
- Fixed: main-landmark detection no longer runs a redundant slow fallback check for every non-main landmark once the fast path already gave a definitive answer, improving J / Shift+J responsiveness on pages with many landmarks.
- Removed unmaintained duplicate copies of the plugin source and docs that lived outside `addon/` and were never packaged by `build.py`.

### 1.0.2 (2026-07-18)
- Scripts moved to `VirtualBuffer` class: J / Shift+J are now announced in input help (NVDA+1) only when a web virtual buffer is active, matching the behaviour of built-in quick-nav keys (H, L, T …).
- Minimum NVDA version lowered to 2019.3; added compatibility shim for `controlTypes.OutputReason` (NVDA < 2021.1).
- Added `PROMPTS.md` documenting the AI-assisted development process.

### 1.0.1 (2026-07-03)
- Fixed: `url` in `manifest.ini` now points to the add-on's dedicated presentation page (required by the NVDA Add-on Store).

### 1.0.0 (2026-06-29)
- Initial release.
- J / Shift+J quick navigation for `<main>` and `role="main"` landmarks on web pages.
- Works in browse mode in Firefox, Chrome, Edge, and other Chromium-based browsers.
- Keys transparently forwarded in all non-browse-mode contexts (form fields, desktop apps).
- Announces "No next / previous main region" when none is found in that direction.
- Shortcuts reconfigurable via NVDA's Input Gestures dialog (Browse mode category).
- Translations: Czech, Slovak, English, German.
