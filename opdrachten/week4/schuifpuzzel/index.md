# Schuifpuzzel

Een schuifpuzzel is een vierkante puzzel die meestal bestaat uit `4 * 4 = 16` velden.
In al deze velden zitten tegels, op één veld na. Doordat er een tegel mist, is er een los veld en kan je de andere tegels verschuiven.
Door telkens een tegel per keer te verschuiven kan je de volgorde van de tegels veranderen.
Op de tegels staan dan de cijfers 1 t/m 15, de schuifpuzzel is opgelost als de
tegels in oplopende volgorde gesorteerd staan van linksboven tot rechtsonder (zie voorbeeld hieronder).
Het verschuiven van tegels kan alleen horizontaal en verticaal. In het voorbeeld
kan je dus de tegels met de cijfers 12 en 15 verplaatsen.

![correct_config](tiles1.png)

Zoals je je misschien wel kan voorstellen, zijn er ontzettend veel verschillende
configuraties van tegels mogelijk.
Voor deze opdracht nemen we aan dat je de schuifpuzzel begint met een configuratie
waarbij de tegels in aflopende volgorde van linksboven tot rechtsonder zijn gesorteerd.
Dit houdt in dat de lege tegel zich in de hoek rechtsonder bevindt.

Er bestaan schuifpuzzels van verschillende groottes (voor deze opdracht,
moeten de zijden minstens 3 velden en maximaal 9 velden lang zijn). Belangrijk
om te weten is, is dat wanneer een zijde een even aantal velden heeft (en er dus
een oneven aantal tegels zijn) de tegels 1 & 2 moeten worden omgewisseld.
Dit is nodig zodat de puzzel oplosbaar is. De beginconfiguratie voor een schuifpuzzel
met zijden van 4 velden is weergegeven in het voorbeeld hieronder.

![start_config](tiles2.png)


## Opdracht

Schrijf, in een bestand genaamd `schuifpuzzel.py`, een programma dat een speler een schuifpuzzel laat oplossen.

* De speler mag zelf de grootte van het bord kiezen. Deze grootte moet groter gelijk dan 3 zijn en kleiner gelijk dan 9.
* De beginconfiguratie is de configuratie zoals hierboven beschreven.
* Prompt de speler telkens om een nieuwe tegel te schuiven. Mocht de speler een tegel kiezen die niet verschoven kan worden,
laat de speler dan een nieuwe tegel kiezen. Je mag er hierbij van uit gaan dat de speler correcte tegel nummers invult.
* De puzzel is opgelost, als de tegels in oplopende volgorde staan gesorteerd.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest
en eventueel verdere uitleg.
Zoals je ziet hebben we voor deze opdracht de `if __name__ == '__main__'` al voor
je geschreven, je hoeft dus alleen de andere functies aan te vullen.


    def get_size() -> int:
        """
        Vraag de gebruiker naar het formaat van het bord.
        Het formaat moet >= 3 en <= 9 zijn.
        """

    def is_won(board: list) -> bool:
        """
        Controleer of het bord in een winnende configuratie staat. Return True als
        de configuratie winnend is, False als dat niet het geval is.


    def move_tile(board: list, tile: int) -> list:
        """
        Als de te verplaatsten tegel verplaatsbaar is: schuif de tegel in de
        configuratie van het bord en return True. Als dat niet het geval is, moet
        het bord in de oorspronkelijke configuratie blijven en moet False worden
        gereturned.

    def print_board(board: list):
        """
        Print het bord per rij naar de terminal.
        """

    def set_board(size: int) -> list:
        """
        Initialiseer een bord van formaat: size x size.
        Sorteer de nummers op aflopende volgorde van links boven naar rechts beneden.
        De volgorde van de tegels 1 en 2 wordt verwisseld als size een even getal is.
        """

    if __name__ == '__main__':

        print("Welkom bij de schuifpuzzel!")

        size = get_size()
        board = set_board(size)

        while not is_won(board):
            print_board(board)

            tile = input("Tegel die je wil schuiven: ")
            board, valid = move_tile(board, int(tile))
            if not valid:
                print("Deze tegel kan je niet schuiven.")

        print("Gefeliciteerd, je hebt de schuifpuzzel opgelost!")

## Tips

* Het bord is in de code weergegeven als een lijst van lijsten. Hierbij zijn er
`size` lijsten van lengte `size`. Als je het bord gaat vullen, is het dus handig
om hem rij voor rij in te vullen.
* Bij `move_tile()` moet je zowel de rij als de kolom van de te verplaatsen tegel
en het lege veld weten. Dit kan je dan ook gebruiken om te checken of de gekozen
tegel verplaatst kan worden. Hierbij moeten de tegels in ieder geval ofwel in
dezelfde rij staan ofwel in dezelfde kolom. Waar moeten de tegels nog meer aan voldoen?
* Bij `is_won()` moet je checken of het bord in de goede configuratie staat.
Doordat de volgorde oplopend is, is dit goed te tellen door middel van een counter
in een dubbele loop (wat voor loop kan je hier het beste gebruiken?).

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python schuifpuzzel.py
    Welkom bij de schuifpuzzel!
    Welk formaat bord wil je spelen? 3
    [8, 7, 6]
    [5, 4, 3]
    [2, 1, 0]
    Tegel die je wil schuiven: 3
    [8, 7, 6]
    [5, 4, 0]
    [2, 1, 3]
    Tegel die je wil schuiven: 4
    [8, 7, 6]
    [5, 0, 4]
    [2, 1, 3]
    Tegel die je wil schuiven: 2
    Deze tegel kan je niet schuiven.
    [8, 7, 6]
    [5, 0, 4]
    [2, 1, 3]
    Tegel die je wil schuiven: 5
    [8, 7, 6]
    [0, 5, 4]
    [2, 1, 3]
    Tegel die je wil schuiven:
    ...
    ...
    ...
    [1, 2, 3]
    [4, 5, 6]
    [7, 0, 8]
    Tegel die je wil schuiven: 8
    Gefeliciteerd, je hebt de schuifpuzzel opgelost!
