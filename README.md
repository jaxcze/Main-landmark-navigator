# Main Landmark Navigator

NVDA add-on that adds dedicated **J / Shift+J** quick-navigation shortcuts for
moving between `<main>` and `role="main"` landmark regions on web pages.

Works identically to NVDA's built-in **H / Shift+H** heading navigation, but
focuses exclusively on the main landmark instead of all landmarks (D / Shift+D).

## Download

Latest release: **1.0.3**  
[Download mainLandmarkNavigator-1.0.3.nvda-addon](https://github.com/janbalak/mainLandmarkNavigator/releases/latest)

Add-on homepage: <https://nvda-addons.janbalak.name/main-landmark-navigator/>

## Features

- **J** → next main region · **Shift+J** → previous main region
- Active only in NVDA browse mode (Firefox, Chrome, Edge, Chromium-based browsers)
- Keys forwarded transparently in form / pass-through mode and in desktop apps
- `<main>` and `role="main"` treated identically; `<main role="main">` counts as one area
- Announces *"No next / previous main region"* when none found in that direction
- Fully reconfigurable via **NVDA → Preferences → Input Gestures → Browse mode**
- Localized: Czech, Slovak, English, German

## Requirements

| Item | Version |
|------|---------|
| NVDA | 2019.3 or later |
| Tested with | NVDA 2026.1 |
| OS | Windows (any version supported by NVDA) |

## Installation

1. Download `mainLandmarkNavigator-1.0.3.nvda-addon`.
2. Open the file while NVDA is running (Enter or double-click).
3. Confirm the installation prompt and restart NVDA.

## Building from source

Requires Python 3.6+ and `gettext` (`msgfmt` on PATH).

```
git clone https://github.com/janbalak/mainLandmarkNavigator.git
cd mainLandmarkNavigator
python build.py
```

Output: `mainLandmarkNavigator-1.0.3.nvda-addon`

## License

GNU General Public License v2 — see [LICENSE](LICENSE).

## Author

Jan Balák & Claude (Anthropic) — <https://janbalak.name>

## Changelog

### 1.0.3 (2026-08-22)
- Fixed: main-landmark detection no longer runs a redundant slow fallback
  check for every non-main landmark once the fast path already gave a
  definitive answer, improving J / Shift+J responsiveness on pages with
  many landmarks.
- Removed unmaintained duplicate copies of the plugin source and docs that
  lived outside `addon/` and were never packaged by `build.py`.

### 1.0.2 (2026-07-18)
- Scripts moved to `VirtualBuffer` class: J / Shift+J are now announced in
  input help (NVDA+1) only when a web virtual buffer is active, matching the
  behaviour of built-in quick-nav keys (H, L, T …).
- Minimum NVDA version lowered to 2019.3; added compatibility shim for
  `controlTypes.OutputReason` (NVDA < 2021.1).
- Added `PROMPTS.md` documenting the AI-assisted development process.
- Added `README.md` and `LICENSE` to the repository.

### 1.0.1 (2026-07-03)
- Fixed: `url` in `manifest.ini` now points to the add-on's dedicated
  presentation page (required by the NVDA Add-on Store).

### 1.0.0 (2026-06-29)
- Initial release.
