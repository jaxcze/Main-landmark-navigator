# Main Landmark Navigator

**Verze:** 1.0.2
**Autor:** 2026 Jan Balák & Claude
**Licence:** GNU General Public License, verze 2
**Minimální verze NVDA:** 2019.3
**Testováno s NVDA:** 2026.1
**Stažení:** <https://nvda-addons.janbalak.name/main-landmark-navigator/>

## Popis

Main Landmark Navigator přidává jednoklávesovou rychlou navigaci pro orientační bod ARIA `<main>` (také zapisovaný jako `role="main"`) na webových stránkách — jako H / Shift+H pro nadpisy, ale zaměřenou výhradně na hlavní oblast obsahu.

## Instalace

1. Stáhněte soubor `mainLandmarkNavigator-1.0.1.nvda-addon`.
2. Otevřete soubor při spuštěném NVDA a potvrďte instalaci.
3. Na požádání restartujte NVDA.

## Použití

| Klávesa | Akce |
|---------|------|
| **J** | Přejde na **další** hlavní oblast |
| **Shift+J** | Přejde na **předchozí** hlavní oblast |

Klávesy fungují pouze v prohlížecím režimu NVDA. Ve formulářových prvcích, desktopových aplikacích nebo jiných kontextech mimo prohlížecí režim jsou klávesy transparentně předány dál. Nápověda ke vstupu (NVDA+1 poté J) popis zkratky zobrazí jen v prohlížecím režimu.

Pokud v daném směru žádná hlavní oblast neexistuje, NVDA ohlásí: *Žádná další hlavní oblast* nebo *Žádná předchozí hlavní oblast*.

## Změna klávesových zkratek

Otevřete **nabídka NVDA → Předvolby → Vstupní gesta**, vyhledejte *main* a příkazy najdete v kategorii **Prohlížecí režim**.

## Seznam změn

### 1.1.0 (2026-07-18)
- Skripty přesunuty na VirtualBuffer: nápověda ke vstupním gestům (Insert+1) nyní hlásí J / Shift+J pouze tehdy, když je focus ve webovém prohlížeči (prohlížecí režim).
- Přidán dekorátor `@script` pro popis a kategorii v dialogu Vstupní gesta (API NVDA 2019.3+).
- Snížena minimální verze NVDA z 2025.3 na 2019.3.
- Přidány soubory README, LICENSE a PROMPTS.md do repozitáře.

### 1.0.2 (2026-07-18)
- Oprava: minimální verze NVDA snížena z 2025.3 na 2019.3 — doplněk nepoužívá žádné API specifické pro 2025.3.
- Oprava: J / Shift+J se již neohlašují v režimu nápovědy ke gestům mimo prohlížecí režim (override `getScript()`).
- Přidáno: soubory `README.md`, `LICENSE` a `PROMPTS.md` do zdrojového repozitáře.

### 1.0.1 (2026-07-17)
- Oprava: pole `url` v `manifest.ini` nyní odkazuje na dedikovanou stránku doplňku (požadavek NVDA Add-on Store).
- Změna: minimální verze NVDA snížena na 2019.3.
- Změna: zkratky J / Shift+J přesunuty z GlobalPlugin do přímého přístupu do třídy VirtualBuffer — nápověda ke vstupu je oznamována jen v prohlížecím režimu.
- Přidáno: compat shim pro `controlTypes.OutputReason` (NVDA < 2021.1).

### 1.0.0 (2026-06-29)
- První vydání. Rychlá navigace J / Shift+J pro orientační body `<main>` a `role="main"`. Překlady: čeština, slovenština, angličtina, němčina.
