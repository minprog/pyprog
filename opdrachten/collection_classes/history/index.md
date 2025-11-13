# Opdracht: Implementeer de class `BrowserHistory`

## 1. Doel van de opdracht
Maak een Python-class die de geschiedenis van een webbrowser beheert. Gebruik een of meer geschikte Python-collections om de data bij te houden. Implementeer veelvoorkomende operaties zoals pagina's bezoeken, teruggaan, vooruitgaan, zoeken en opschonen.

## 2. Functionele eisen

### 2.1 Constructor
- Initialiseert een lege browsergeschiedenis.
- Houdt minimaal bij:
  - De complete lijst met bezochte pagina's in volgorde.
  - De huidige positie in de geschiedenis.

### 2.2 `visit(url)`
- Voegt een nieuwe URL toe aan de geschiedenis.
- Als de gebruiker niet aan het einde van de geschiedenis staat, verwijder dan de forward-geschiedenis.
- Zet de huidige positie op de nieuwe pagina.

### 2.3 `back()`
- Verplaatst de huidige positie één stap terug.
- Geeft de nieuwe huidige URL terug.
- Als er niet verder terug kan worden gegaan, blijft de positie gelijk.

### 2.4 `forward()`
- Verplaatst de huidige positie één stap vooruit.
- Randvoorwaarden analoog aan `back()`.

### 2.5 `current()`
- Retourneert de URL die op dit moment actief is.

### 2.6 `find(keyword)`
- Geeft een lijst van alle URLs waarin de keyword-substring voorkomt.
- Zoeken is case-insensitive.

### 2.7 `clear()`
- Maakt de volledige geschiedenis leeg.
- Reset de huidige positie.

## 3. Ontwerpkeuzes (inleververantwoording)
Beschrijf kort:
- Welke datastructuren zijn gekozen en waarom.
- Hoe randgevallen worden afgehandeld (geen history, back/forward buiten bereik, etc.).
- Eventuele extra functies die zijn toegevoegd.

## 4. Optionele uitbreidingen
- Maximale lengtelimiet op de geschiedenis.
- Opslaan van timestamps per entry.
- Exporteren en importeren van geschiedenis naar JSON.
- Undo/redo-functionaliteit.

## 5. Minimale testcases
Studenten leveren tests aan die verifiëren dat:
- `visit` correct werkt, inclusief verwijderen van forward-geschiedenis.
- `back` en `forward` grenzen correct afhandelen.
- `find` correcte zoekresultaten geeft.
- `clear` de gehele geschiedenis reset.
