# Main Landmark Navigator

**Verzia:** 1.0.2
**Autor:** 2026 Jan Balák & Claude
**Licencia:** GNU General Public License, verzia 2
**Minimálna verzia NVDA:** 2019.3
**Testované s NVDA:** 2026.1
**Stiahnutie:** <https://nvda-addons.janbalak.name/main-landmark-navigator/>

## Popis

Main Landmark Navigator pridáva jednoklávesovú rýchlu navigáciu pre orientačný bod ARIA `<main>` (tiež zapisovaný ako `role="main"`) na webových stránkach — ako H / Shift+H pre nadpisy, ale zameranú výhradne na hlavnú oblasť obsahu.

## Inštalácia

1. Stiahnite súbor `mainLandmarkNavigator-1.0.1.nvda-addon`.
2. Otvorte súbor pri spustenom NVDA a potvrďte inštaláciu.
3. Na požiadanie reštartujte NVDA.

## Používanie

| Klávesa | Akcia |
|---------|-------|
| **J** | Prejde na **ďalšiu** hlavnú oblasť |
| **Shift+J** | Prejde na **predchádzajúcu** hlavnú oblasť |

Klávesy fungujú iba v prehliadacom režime NVDA. Nápoveda k vstupu (NVDA+1 potom J) popis skratky zobrazí len v prehliadacom režime.

## Zoznam zmien

### 1.1.0 (2026-07-18)
- Skripty presunuté na VirtualBuffer: pomocník pre vstupné gestá (Insert+1) teraz hlási J / Shift+J iba vtedy, keď je focus vo webovom prehliadači (prehliadací režim).
- Pridaný dekorátor `@script` pre popis a kategóriu v dialógu Vstupné gestá (API NVDA 2019.3+).
- Znížená minimálna verzia NVDA z 2025.3 na 2019.3.
- Pridané súbory README, LICENSE a PROMPTS.md do repozitára.

### 1.0.2 (2026-07-18)
- Oprava: minimálna verzia NVDA znížená z 2025.3 na 2019.3 — doplnok nepoužíva žiadne API špecifické pre 2025.3.
- Oprava: J / Shift+J sa viac neohlasujú v režime pomoci ku gestám mimo prehliadacieho režimu (override `getScript()`).
- Pridané: súbory `README.md`, `LICENSE` a `PROMPTS.md` do zdrojového repozitára.

### 1.0.1 (2026-07-17)
- Oprava: pole `url` v `manifest.ini` teraz odkazuje na dedikovanú stránku doplnku.
- Zmena: minimálna verzia NVDA znížená na 2019.3.
- Zmena: skratky J / Shift+J presunuté do priameho vstupu do triedy VirtualBuffer.
- Pridané: compat shim pre `controlTypes.OutputReason` (NVDA < 2021.1).

### 1.0.0 (2026-06-29)
- Prvé vydanie. Rýchla navigácia J / Shift+J. Preklady: čeština, slovenčina, angličtina, nemčina.
