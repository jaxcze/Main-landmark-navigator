# AI-Assisted Development — Prompt Log

This add-on was developed with [Claude](https://claude.ai) (Anthropic).
The conversation took place in Czech; prompts are shown in the original language
with an English summary for each step.

---

## 1 — Initial creation

**Prompt (CS):**
> Vytvoř nvda addon s nejnižší verzí nvda 2025.3 a především optimalizované
> pro 2026.1. jazyk doplňku primárně pro en, ale pak i pro cs, sk, de.
> Předpokládám, že základní ohlašování „žádná další hlavní oblast" a „žádná
> předchozí hlavní oblast" se dá poskládat z již existujících řetězců v nvda.
> Plugin bude přecházet na následující a předchozí hlavní oblast na webu,
> definované jak pomocí `<main>`, tak i `role="main"`. Pokud to bude typu
> `<main role="main">`, tak to bude bráno jako jedna oblast. Uživatelsky
> definované zkratky budou tedy na další a předchozí hlavní oblast. Snad bude
> možné definovat i jednopísmennou rychlou navigaci, např. pomocí „J" pro
> následující a „Shift+J" pro předchozí hlavní oblast. Aby se to chovalo, jako
> jiné další prvky stránky.

**Summary:** Create an NVDA add-on (min. 2025.3, target 2026.1) with
J / Shift+J single-key quick-navigation between `<main>` / `role="main"`
landmarks on web pages. Localize into EN, CS, SK, DE. Behave like other
built-in quick-nav keys (H for headings, L for lists, etc.).

---

## 2 — Installation failure diagnosis

**Prompt (CS):**
> JDE stáhnout ale nejde spustit. mimojiné do autora dej „2026 Jan Balák & Claude".
> A vše pro publikaci, readme atd. co je potřeba podle pravidel nvda.

**Summary:** Add-on downloaded successfully but failed to start. Also: change
author to "2026 Jan Balák & Claude" and prepare all publication artefacts
(per-language doc/readmes, `.pot` translation template, `build.py`).

**Root cause found by Claude:** The `@script(gesture=…)` decorator was being
used for gesture binding on a `GlobalPlugin`. This is fragile in some NVDA
versions; the approach was replaced with the classic `__gestures` dict combined
with direct `__doc__` and `.category` attribute assignment on the script
functions.

---

## 3 — Navigation silent when landmark exists

**Prompt (CS):**
> ano, tohle funguje. ale přecijen mám dotaz. píšeš, že se to explicitně musí
> oznamovat. […] jediný problém byl, že odečítač neměl dedikovanou klávesovku
> pro pouze hlavní oblast.

**Summary:** Add-on now loads and announces "no next / previous" correctly.
But when a `<main>` landmark IS present, NVDA is silent and the cursor
doesn't move.

**Root cause found by Claude:** The `except TypeError / except AttributeError`
chain around `_set_selection()` was too narrow. NVDA 2025.3 raises a different
internal exception type; it escaped all `except` clauses, propagated silently
through NVDA's script handler, and neither movement nor announcement occurred.
Fix: replace with `except Exception` (broad catch) and add explicit
`speech.cancelSpeech()` + `speech.speakTextInfo()` so the announcement never
depends on `_set_selection()` internal behaviour.

---

## 4 — Presentation website

**Prompt (CS):**
> v příloze je funkční prezentační web dalšího mého addonu. vezmi texty a
> nejnutnější proměnné, které se budou lišit a naplň to pro prezentaci tohoto
> doplňku s main oblastí. název té složky bude main-landmark-navigator

**Summary:** Adapt an existing PHP presentation website (Last Item Announcer)
for this add-on: swap add-on name, version, download file, all four language
files, counter config, `.htaccess`, and deployment README. Leave all logic,
CSS, and templates unchanged.

---

## 5 — Unicode escape fix

**Prompt (CS):**
> Web: jsou zde nejspíše escapované unicode, např na hlavní obrazovce
> • Rychlá navigace J\u00a0/\u00a0Shift+J na další a předchozí hlavní oblast
> obsahu. Tak to ještě projdi a oprav

**Summary:** PHP single-quoted strings do not interpret `\uXXXX` sequences;
they appear literally in the browser. Also, `&lt;main&gt;` embedded in strings
that pass through `htmlspecialchars()` (`e()`) double-escapes to `&amp;lt;`.
Fix: replace all escape sequences with actual UTF-8 characters and use plain
`<main>` text (let `e()` escape it correctly).

---

## 6 — Store rejection: manifest URL

**Prompt (CS):**
> Tohle přišlo z addon store: This add-on is been rejected, since the URL
> provided in the manifest.ini doesn't provide information about the add-on.

**Summary:** `url = https://janbalak.name` points to the generic homepage.
Changed to `https://nvda-addons.janbalak.name/main-landmark-navigator/`.

---

## 7 — Version bump 1.0.1 + full publication package

**Prompt (CS):**
> Změnit verzi na 1.0.1 a vrací opět kompletní balík publikaci

**Summary:** Bump version to 1.0.1, rebuild `.nvda-addon`, recalculate SHA256,
update `addon-datastore.json`, and package the three-layer release ZIP:
installable file + source tree + store submission JSON.

---

## 8 — Store review feedback (this release, 1.0.2)

**Prompt (CS):**
> zapracuj tyto připomínky z addon store: […] udělej vše kromě 1

Reviewer comments addressed in 1.0.2 (point 1 — README/LICENSE — deferred):

| # | Reviewer comment | Action |
|---|------------------|--------|
| 2 | Minimum version 2019.3 or use 2025.3 API | Lowered min to 2019.3; added `OutputReason` shim for NVDA < 2021.1 |
| 4 | Input help announces J outside browse mode | Scripts moved to `VirtualBuffer` class via `__init__`/`terminate` injection — now scoped to browse mode only |
| 6 | Add AI prompts list | This file (`PROMPTS.md`) |
