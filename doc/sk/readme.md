# Navigátor hlavnej oblasti

**Verzia:** 1.0.0  
**Autor:** 2026 Jan Balák & Claude  
**Licencia:** GNU General Public License, verzia 2  
**Minimálna verzia NVDA:** 2025.3  
**Testované s NVDA:** 2026.1  
**Stiahnutie:** <https://janbalak.name>

---

## Popis

Navigátor hlavnej oblasti pridáva jednoklávesovú rýchlu navigáciu pre
orientačný bod ARIA `<main>` (alternatívne zapisovaný ako `role="main"`) na
webových stránkach.

NVDA už umožňuje prechádzať medzi *všetkými* orientačnými bodmi ARIA pomocou
**Čiarka** (ďalší) a **Shift+Čiarka** (predchádzajúci). Tento doplnok dopĺňa
túto funkciu o vyhradený pár kláves, ktorý prechádza *výhradne* medzi
oblasťami hlavného obsahu — podobne ako **H / Shift+H** funguje len pre
nadpisy.

`<main role="main">` je spracovaný identicky ako `<main>`, pretože
prehliadače ho NVDA sprístupňujú rovnakým spôsobom: ako jeden orientačný bod
s rolou *main*.

---

## Inštalácia

1. Stiahnite súbor `mainLandmarkNavigator-1.0.0.nvda-addon`.
2. Otvorte súbor (Enter alebo dvojklik) pri spustenom NVDA, alebo zvoľte
   **ponuka NVDA → Nástroje → Správa doplnkov → Inštalovať** a prejdite
   k súboru.
3. Potvrďte výzvu na inštaláciu.
4. Na požiadanie reštartujte NVDA.

---

## Používanie

| Klávesa | Akcia |
|---------|-------|
| **J** | Prejde na **ďalšiu** hlavnú oblasť na stránke |
| **Shift+J** | Prejde na **predchádzajúcu** hlavnú oblasť na stránke |

Obe klávesy fungujú **iba v režime čítania NVDA** (teda pri prehliadaní
webovej stránky, nie vtedy, keď má zameranie formulárový prvok alebo iný
interaktívny prvok v prietočnom režime). V akomkoľvek inom kontexte je
klávesa transparentne odovzdaná aplikácii.

Po nájdení hlavnej oblasti NVDA oznámi jej obsah pomocou rovnakého hlasového
a braillského výstupu ako zabudované príkazy rýchlej navigácie.

Ak v požadovanom smere žiadna hlavná oblasť neexistuje, NVDA oznámi:
- *„Žiadna ďalšia hlavná oblasť"*
- *„Žiadna predchádzajúca hlavná oblasť"*

---

## Zmena klávesových skratiek

1. Otvorte **ponuka NVDA → Nastavenia → Vstupné gestá…**
2. Do vyhľadávacieho poľa napíšte *main* alebo prejdite do kategórie **Režim
   prehliadania** (Browse mode).
3. Vyberte *Presunie sa na ďalšiu hlavnú oblasť na webovej stránke* alebo
   variant pre predchádzajúci a stlačte **Pridať** na priradenie nového
   klávesu, alebo **Odstrániť** na jeho odobratie.
4. Potvrďte tlačidlom **OK**.

---

## Kompatibilita

| Prehliadač | Jadro | Stav |
|------------|-------|------|
| Firefox | IAccessible2 (Gecko) | ✅ Podporované |
| Google Chrome | UIA / IAccessible2 | ✅ Podporované |
| Microsoft Edge | UIA | ✅ Podporované |
| Prehliadače na báze Chromium | UIA / IAccessible2 | ✅ Podporované |

---

## Známe obmedzenia

- Doplnok naviguje iba vo **virtuálnom bufferi** (režim čítania). V
  aplikáciách, ktoré sprístupňujú orientačné body ARIA cez UIA bez
  virtuálneho buffera, nemá efekt.
- Ak stránka neobsahuje žiadny prvok `<main>`, je oznámená príslušná správa
  o absencii oblasti a kurzor zostane na aktuálnej pozícii.

---

## Protokol zmien

### 1.0.0 (2026-06-29)
- Prvé vydanie.
- Rýchla navigácia J / Shift+J pre orientačné body `<main>` a `role="main"`.
- Preklady: angličtina, čeština, slovenčina, nemčina.
- Minimálna verzia NVDA: 2025.3; testované na 2026.1.
