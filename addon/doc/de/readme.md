# Main Landmark Navigator

**Version:** 1.0.2
**Autor:** 2026 Jan Balák & Claude
**Lizenz:** GNU General Public License, Version 2
**Mindest-NVDA-Version:** 2019.3
**Getestet mit NVDA:** 2026.1
**Download:** <https://nvda-addons.janbalak.name/main-landmark-navigator/>

## Beschreibung

Main Landmark Navigator fügt eine Einzeltasten-Schnellnavigation für den ARIA-Orientierungspunkt `<main>` (auch als `role="main"`) auf Webseiten hinzu — wie H / Shift+H für Überschriften, aber ausschließlich auf den Hauptinhaltsbereich fokussiert.

## Installation

1. Laden Sie `mainLandmarkNavigator-1.0.1.nvda-addon` herunter.
2. Öffnen Sie die Datei bei laufendem NVDA und bestätigen Sie die Installation.
3. Starten Sie NVDA neu, wenn Sie dazu aufgefordert werden.

## Verwendung

| Taste | Aktion |
|-------|--------|
| **J** | Zum **nächsten** Hauptbereich springen |
| **Shift+J** | Zum **vorherigen** Hauptbereich springen |

Die Tasten sind nur im NVDA-Lesemodus aktiv. Die Eingabehilfe (NVDA+1 dann J) kündigt die Tastenkombination nur im Lesemodus an.

## Änderungsprotokoll

### 1.1.0 (2026-07-18)
- Skripte in VirtualBuffer verschoben: die Eingabehilfe (Insert+1) kündigt J / Shift+J jetzt nur an, wenn der Fokus in einem Webbrowser liegt (Lesemodus).
- `@script`-Dekorator für Beschreibungs- und Kategorie-Metadaten im Eingaben-Dialog hinzugefügt (NVDA 2019.3+ API).
- Mindest-NVDA-Version von 2025.3 auf 2019.3 gesenkt.
- README, LICENSE und PROMPTS.md zum Repository hinzugefügt.

### 1.0.2 (2026-07-18)
- Korrektur: Mindest-NVDA-Version von 2025.3 auf 2019.3 gesenkt — es wird keine 2025.3-spezifische API verwendet.
- Korrektur: J / Shift+J werden im Eingabehilfe-Modus außerhalb des Lesemodus nicht mehr angezeigt (`getScript()`-Override).
- Hinzugefügt: `README.md`, `LICENSE` und `PROMPTS.md` im Quell-Repository.

### 1.0.1 (2026-07-17)
- Korrektur: `url` in `manifest.ini` verweist jetzt auf die dedizierte Add-on-Seite.
- Änderung: Mindest-NVDA-Version auf 2019.3 gesenkt.
- Änderung: J / Shift+J von GlobalPlugin in VirtualBuffer-Klassen-Injektion verschoben.
- Hinzugefügt: Kompatibilitäts-Shim für `controlTypes.OutputReason` (NVDA < 2021.1).

### 1.0.0 (2026-06-29)
- Erstveröffentlichung. J / Shift+J Schnellnavigation. Übersetzungen: Tschechisch, Slowakisch, Englisch, Deutsch.
