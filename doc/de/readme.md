# Hauptbereich-Navigator

**Version:** 1.0.1  
**Autor:** 2026 Jan Balák & Claude  
**Lizenz:** GNU General Public License, Version 2  
**Mindest-NVDA-Version:** 2025.3  
**Getestet mit NVDA:** 2026.1  
**Download:** <https://janbalak.name>

---

## Beschreibung

Der Hauptbereich-Navigator fügt eine Einzeltasten-Schnellnavigation für den
ARIA-Orientierungspunkt `<main>` (auch als `role="main"` geschrieben) auf
Webseiten hinzu.

NVDA ermöglicht bereits die Navigation zwischen *allen* ARIA-Orientierungs­punkten
mit **Komma** (nächster) und **Shift+Komma** (vorheriger). Dieses Add-on
ergänzt diese Funktion durch ein dediziertes Tastenpaar, das sich
*ausschließlich* zwischen Hauptinhaltsbereichen bewegt — ähnlich wie
**H / Shift+H** nur für Überschriften funktioniert.

`<main role="main">` wird identisch zu `<main>` behandelt, da Browser beide
Varianten NVDA auf exakt dieselbe Weise bereitstellen: als einen
Orientierungspunkt mit der Rolle *main*.

---

## Installation

1. Laden Sie `mainLandmarkNavigator-1.0.0.nvda-addon` herunter.
2. Öffnen Sie die Datei (Eingabe oder Doppelklick) während NVDA läuft, oder
   wählen Sie **NVDA-Menü → Werkzeuge → Add-ons verwalten → Installieren** und
   navigieren Sie zur Datei.
3. Bestätigen Sie die Installationsaufforderung.
4. Starten Sie NVDA neu, wenn Sie dazu aufgefordert werden.

---

## Verwendung

| Taste | Aktion |
|-------|--------|
| **J** | Zum **nächsten** Hauptbereich der Seite springen |
| **Shift+J** | Zum **vorherigen** Hauptbereich der Seite springen |

Beide Tasten funktionieren **nur im NVDA-Lesemodus** (d. h. beim Lesen einer
Webseite, nicht wenn ein Formularfeld oder ein anderes interaktives Element
im Durchgangsmodus den Fokus hat). In jedem anderen Kontext wird die Taste
transparent an die Anwendung weitergeleitet.

Wenn ein Hauptbereich gefunden wird, gibt NVDA dessen Inhalt mit derselben
Sprach-/Braille-Ausgabe aus wie die eingebauten Schnellnavigationsbefehle.

Wenn in der gewünschten Richtung kein Hauptbereich vorhanden ist, gibt NVDA aus:
- *„Kein nächster Hauptbereich"*
- *„Kein vorheriger Hauptbereich"*

---

## Tastenkürzel ändern

1. Öffnen Sie **NVDA-Menü → Einstellungen → Eingaben…**
2. Geben Sie im Suchfeld *main* ein oder navigieren Sie zur Kategorie
   **Lesemodus** (Browse mode).
3. Wählen Sie *Springt zum nächsten Hauptbereich der Webseite* oder die
   Variante für den vorherigen und drücken Sie **Hinzufügen**, um eine neue
   Taste zuzuweisen, oder **Entfernen**, um sie zu löschen.
4. Bestätigen Sie mit **OK**.

---

## Kompatibilität

| Browser | Engine | Status |
|---------|--------|--------|
| Firefox | IAccessible2 (Gecko) | ✅ Unterstützt |
| Google Chrome | UIA / IAccessible2 | ✅ Unterstützt |
| Microsoft Edge | UIA | ✅ Unterstützt |
| Chromium-basierte Browser | UIA / IAccessible2 | ✅ Unterstützt |

---

## Bekannte Einschränkungen

- Das Add-on navigiert nur im **virtuellen Puffer** (Lesemodus). In
  Anwendungen, die ARIA-Orientierungspunkte über UIA ohne virtuellen Puffer
  bereitstellen (z. B. bestimmte Microsoft-Office-Komponenten), hat es keinen
  Effekt.
- Enthält eine Seite kein `<main>`-Element, wird die entsprechende
  Fehlermeldung ausgegeben und der Cursor bleibt an seiner aktuellen Position.

---

## Änderungsprotokoll

### 1.0.1 (2026-07-03)
- Korrektur: Das Feld `url` in `manifest.ini` verweist jetzt direkt auf die Präsentationsseite der Erweiterung (Anforderung des NVDA-Add-on-Stores).

### 1.0.0 (2026-06-29)
- Erstveröffentlichung.
- J / Shift+J Schnellnavigation für `<main>`- und `role="main"`-Orientierungspunkte.
- Übersetzungen: Englisch, Tschechisch, Slowakisch, Deutsch.
- Mindest-NVDA-Version: 2025.3; getestet mit 2026.1.
