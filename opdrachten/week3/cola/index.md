# Cola-automaat

Stel nou je hebt ontzettende dorst en je wil graag een flesje cola uit een drankautomaat halen.
In de automaat waar je voor staat kost een flesje cola 50 cent en worden er alleen maar muntstukken van 25, 10, en 5 cent geaccepteerd.
In principe kan je gedachteloos muntjes in de automaat stoppen maar je hebt teveel dorst om goed na te denken en wil wel zeker weten dat je voldoende wisselgeld terug krijgt.
De perfecte reden om een programma te schrijven waarmee je de drankautomaat kan nabootsen om te controleren welke munten je moet invoeren en het bijbehorende wisselgeld te berekenen.

## Opdracht

Schrijf, in een bestand genaamd `cola.py`, een programma dat de gebruiker vraagt om een muntstuk in te voeren (een per keer) en dat het nog te betalen bedrag weergeeft.
Als er genoeg muntstukken zijn ingeworpen, moet het programma geven hoeveel wisselgeld je terug krijgt.

* Je mag aannemen dat de gebruiker alleen maar integers invoert.
* De automaat accepteert alleen maar muntstukken van 25, 10, en 5 cent, zorg dat andere muntstukken niet worden geaccepteerd.


## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.


    def check_coin(coin: int) -> bool:
        """
        Controleert of een munt wordt toegelaten.
        """

    def determine_due(coin: int) -> bool:
        """
        Bepaalt hoeveel nog moet worden betaald nadat de eerste munt is ingeworpen. De ingeworpen munt moet valide zijn.
        """

    def prompt_coin(due: int) -> int:
        """
        Blijft de gebruiker om nieuwe munten vragen totdat het te betalen bedrag is bereikt.
        Output is de hoeveelheid wisselgeld.
        """

    if __name__ == '__main__':
        Prompt de gebruiker voor de eerste input, roep je functies aan, en print het wisselgeld.

## Tips

* De gebruiker moet herhaadelijk nieuwe munten inwerpen en hiervoor geprompt worden. Dit is handig om te doen in een loop. We hebben een eindconditie, dus welk soort loop is handig om te gebruiken?
* Niet alle functies hoeven aangeroepen te worden in de `if __name__ == '__main__'`. De functie `check_coin` wordt alleen maar gebruikt in de andere twee functies.


## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python cola.py
    Geld verschuldigd: 50
    Munt inwerpen: 25
    Geld verschuldigd: 25
    Munt inwerpen: 25
    Wisselgeld: 0

    $ python cola.py
    Geld verschuldigd: 50
    Munt inwerpen: 10
    Geld verschuldigd: 40
    Munt inwerpen: 25
    Geld verschuldigd: 15
    Munt inwerpen: 25
    Wisselgeld: 10

    $ python cola.py
    Geld verschuldigd: 50
    Munt inwerpen: 10
    Geld verschuldigd: 40
    Munt inwerpen: 30
    Geld verschuldigd: 40
    Munt inwerpen: 25
    Geld verschuldigd: 15
    Munt inwerpen: 5
    Geld verschuldigd: 10
    Munt inwerpen: 10
    Wisselgeld: 0
