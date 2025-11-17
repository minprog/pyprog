# Browser-geschiedenis

Maak een Python-class genaamd `BrowserHistory` die de geschiedenis van een webbrowser beheert. Gebruik één of meer geschikte Python-collections om de data bij te houden. Implementeer veelvoorkomende operaties zoals pagina's bezoeken, teruggaan, vooruitgaan, zoeken en opschonen.

## Initializer

- Initialiseert een lege browsergeschiedenis.

- Houdt minimaal bij:
    - De complete lijst met bezochte pagina's in volgorde.
    - De huidige positie in de geschiedenis (deze is belangrijk voor de meeste operaties!).

## Operatie: visit

- Voegt een nieuwe URL toe aan de geschiedenis.
- Als de gebruiker niet aan het einde van de geschiedenis staat, verwijder dan de geschiedenis vanaf het huidige punt en vervang door de nieuwe URL.
- Zet de huidige positie op de nieuwe pagina.

## Operatie: back

- Verplaatst de huidige positie één stap terug.
- Geeft de nieuwe huidige URL terug.
- Als er niet verder terug kan worden gegaan, blijft de positie gelijk.

## Operatie: forward

- Verplaatst de huidige positie één stap vooruit.
- Randvoorwaarden zoals bij `back()`.

## Operatie: current

- Geeft de URL die op dit moment actief is.

## Operatie: find

- Geeft een lijst van alle URLs waarin een gegeven substring voorkomt.
- Zoeken is case-insensitive!

## Operatie: clear

- Maakt de volledige geschiedenis leeg.
- Reset de huidige positie.

## Errors

- Geef een `IndexError` als de positie aangepast moet worden maar dit kan niet. Bedenk bij welke operaties dit nodig is.
