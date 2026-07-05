# Navigátor hlavní oblasti

**Verze:** 1.0.1  
**Autor:** 2026 Jan Balák & Claude  
**Licence:** GNU General Public License, verze 2  
**Minimální verze NVDA:** 2025.3  
**Testováno s NVDA:** 2026.1  
**Stažení:** <https://janbalak.name>

---

## Popis

Navigátor hlavní oblasti přidává jednoklávesovou rychlou navigaci pro
orientační bod ARIA `<main>` (alternativně zapisovaný jako `role="main"`) na
webových stránkách.

NVDA již umožňuje přecházet mezi *všemi* orientačními body ARIA pomocí
**Čárka** (další) a **Shift+Čárka** (předchozí). Tento doplněk tuto funkci
doplňuje o vyhrazenou dvojici kláves, která přechází *výhradně* mezi
oblastmi hlavního obsahu — podobně jako **H / Shift+H** funguje pouze pro
nadpisy.

`<main role="main">` je zpracováván identicky jako `<main>`, protože
prohlížeče ho NVDA zpřístupňují naprosto stejným způsobem: jako jeden
orientační bod s rolí *main*.

---

## Instalace

1. Stáhněte soubor `mainLandmarkNavigator-1.0.0.nvda-addon`.
2. Otevřete soubor (Enter nebo dvojklik) při spuštěném NVDA, nebo zvolte
   **nabídka NVDA → Nástroje → Správa doplňků → Instalovat** a přejděte
   k souboru.
3. Potvrďte výzvu k instalaci.
4. Na požádání restartujte NVDA.

---

## Použití

| Klávesa | Akce |
|---------|------|
| **J** | Přejde na **další** hlavní oblast na stránce |
| **Shift+J** | Přejde na **předchozí** hlavní oblast na stránce |

Obě klávesy fungují **pouze v režimu čtení NVDA** (tedy při prohlížení
webové stránky, nikoli tehdy, když má zaměření formulářový prvek nebo jiný
interaktivní prvek v průchozím režimu). V jakémkoli jiném kontextu je
kláves transparentně předána aplikaci.

Po nalezení hlavní oblasti NVDA oznámí její obsah pomocí stejného hlasového
a braillského výstupu jako vestavěné příkazy rychlé navigace.

Pokud v požadovaném směru žádná hlavní oblast neexistuje, NVDA oznámí:
- *„Žádná další hlavní oblast"*
- *„Žádná předchozí hlavní oblast"*

---

## Změna klávesových zkratek

1. Otevřete **nabídka NVDA → Předvolby → Vstupní gesta…**
2. Do vyhledávacího pole napište *main* nebo přejděte do kategorie **Režim
   procházení** (Browse mode).
3. Vyberte *Přesune se na další hlavní oblast na webové stránce* nebo
   variantu pro předchozí a stiskněte **Přidat** pro přiřazení nové klávesy,
   nebo **Odebrat** pro její odebrání.
4. Potvrďte tlačítkem **OK**.

---

## Kompatibilita

| Prohlížeč | Jádro | Stav |
|-----------|-------|------|
| Firefox | IAccessible2 (Gecko) | ✅ Podporováno |
| Google Chrome | UIA / IAccessible2 | ✅ Podporováno |
| Microsoft Edge | UIA | ✅ Podporováno |
| Prohlížeče na bázi Chromium | UIA / IAccessible2 | ✅ Podporováno |

---

## Známá omezení

- Doplněk naviguje pouze ve **virtuálním bufferu** (režim čtení). V
  aplikacích, které zpřístupňují orientační body ARIA přes UIA bez
  virtuálního bufferu (např. některé součásti Microsoft Office), nemá efekt.
- Pokud stránka neobsahuje žádný prvek `<main>`, je oznámena příslušná zpráva
  o absenci oblasti a kurzor zůstane na aktuální pozici.

---

## Protokol změn

### 1.0.1 (2026-07-03)
- Oprava: pole `url` v `manifest.ini` nyní odkazuje přímo na prezentační stránku doplňku (požadavek NVDA Add-on Store).

### 1.0.0 (2026-06-29)
- První vydání.
- Rychlá navigace J / Shift+J pro orientační body `<main>` a `role="main"`.
- Překlady: angličtina, čeština, slovenština, němčina.
- Minimální verze NVDA: 2025.3; testováno na 2026.1.
