# Main Landmark Navigator

**Verzia:** 1.0.5
**Autor:** Jan Balák
**Licencia:** GNU General Public License, verzia 2
**Minimálna verzia NVDA:** 2019.3
**Testované s NVDA:** 2026.1
**Stiahnutie:** <https://nvda-addons.janbalak.name/main-landmark-navigator/>

## Popis

Main Landmark Navigator pridáva jednoklávesovú rýchlu navigáciu pre orientačný bod ARIA `<main>` (tiež zapisovaný ako `role="main"`) na webových stránkach — ako H / Shift+H pre nadpisy, ale zameranú výhradne na hlavnú oblasť obsahu.

## Inštalácia

1. Stiahnite súbor `mainLandmarkNavigator-1.0.5.nvda-addon`.
2. Otvorte súbor pri spustenom NVDA a potvrďte inštaláciu.
3. Na požiadanie reštartujte NVDA.

## Používanie

| Klávesa | Akcia |
|---------|-------|
| **J** | Prejde na **ďalšiu** hlavnú oblasť |
| **Shift+J** | Prejde na **predchádzajúcu** hlavnú oblasť |

Klávesy fungujú iba v prehliadacom režime NVDA. Nápoveda k vstupu (NVDA+1 potom J) popis skratky zobrazí len v prehliadacom režime.

## Zoznam zmien

### 1.0.5 (2026-08-27)
- Oprava: pole `author` v `manifest.ini` už neobsahuje rok na začiatku — je to
  obyčajné pole na uvedenie autora, nie autorskoprávna doložka, takže teraz
  obsahuje jednoducho „Jan Balák". Žiadna funkčná zmena.
- Zmena: popis J / Shift+J v dialógu Vstupné gestá (a v režime pomoci ku
  vstupu) teraz spomína aj „hlavný landmark" popri „hlavnej oblasti", nech sa
  dá nájsť pod oboma výrazmi. Reakcia na spätnú väzbu recenzenta pri podaní
  do NVDA Add-on Store (nvaccess/addon-datastore#11129).

### 1.0.4 (2026-08-26)
- Oprava: autor/copyright metadáta (manifest, hlavička zdrojového kódu, šablóny prekladov, jazykové readme) už ako spoluautora neuvádzajú AI asistenta — autorom je len Jan Balák. Žiadna funkčná zmena.

### 1.0.3 (2026-08-22)
- Oprava: detekcia hlavnej oblasti (landmark „main") už pri nesúvisiacich orientačných bodoch zbytočne nespúšťa aj pomalú záložnú kontrolu potom, čo rýchla cesta už dala jednoznačnú odpoveď.
- Odstránené neudržiavané duplicitné kópie zdrojového kódu a dokumentácie mimo adresára `addon/`.

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
