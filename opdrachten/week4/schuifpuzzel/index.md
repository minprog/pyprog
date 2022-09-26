# Schuifpuzzel

Een schuifpuzzel is een vierkante puzzel die meestal bestaat uit `4 * 4 = 16` velden.
In al deze velden zitten tegels, op één veld na.
Doordat er een tegel mist, is er een vrij veld en kun je de andere tegels verschuiven.

Door telkens één tegel te verschuiven kun je de volgorde van de tegels veranderen.
Op de tegels staan dan de cijfers 1 t/m 15, en de schuifpuzzel is opgelost als de
tegels in oplopende volgorde gesorteerd staan van linksboven tot rechtsonder (zie voorbeeld hieronder).

![correct_config](tiles1.png){: style="width:20rem;"}

Het verschuiven van tegels kan alleen horizontaal en verticaal. In het voorbeeld
kun je dus de tegels met de cijfers 12 en 15 verplaatsen.

Zoals je je misschien wel kunt voorstellen, zijn er ontzettend veel verschillende
configuraties van tegels mogelijk.
Voor deze opdracht nemen we aan dat je de schuifpuzzel begint met een configuratie
waarbij de tegels in aflopende volgorde van linksboven tot rechtsonder zijn gesorteerd.
Dit houdt in dat de lege tegel zich in de hoek rechtsonder bevindt.
De beginconfiguratie voor een schuifpuzzel
met zijden van 4 velden is weergegeven in het voorbeeld hieronder.

![start_config](tiles2.png){: style="width:20rem;"}

Er bestaan schuifpuzzels van verschillende groottes (voor deze opdracht,
moeten de zijden minstens 3 velden en maximaal 9 velden lang zijn). Belangrijk
om te weten is, is dat wanneer een zijde een even aantal velden heeft (en er dus
een oneven aantal tegels zijn) de tegels 1 & 2 moeten worden omgewisseld.
Dit is nodig zodat de puzzel oplosbaar is, en dat zie je dus ook terug in het voorbeeld hierboven.

## Opdracht

Schrijf, in een bestand genaamd `schuifpuzzel.py`, een programma dat een speler een schuifpuzzel laat oplossen.

* De schuifpuzzel heeft altijd het formaat 4 × 4.

* De beginconfiguratie is de configuratie zoals hierboven beschreven.

* Vraag de speler telkens om een nieuwe tegel te schuiven. Mocht de speler een tegel kiezen die niet verschoven kan worden, laat de speler dan een nieuwe tegel kiezen. Je mag er hierbij van uit gaan dat de speler correcte tegel nummers invult.

* De puzzel is opgelost als de tegels in oplopende volgorde staan gesorteerd zoals eerder beschreven.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en verdere uitleg van de aanpak die je gekozen hebt. Zoals je ziet hebben we voor deze opdracht het hoofdprogramma al voor je geschreven; je hoeft dus alleen de andere functies aan te vullen.

Het wordt ook bij deze opdracht aangemoedigd om extra functies te introduceren die een klein deel van het probleem oplossen. Die moeten dan ook types hebben en doctests.

    Board = list[list[int]]

    def is_won(board: Board) -> bool:
        """
        Controleert of het bord in een winnende configuratie staat. Geeft True als
        de configuratie winnend is, False als dat niet het geval is.
        """

    def move_tile(board: Board, tile: int) -> bool:
        """
        Als de te verplaatsten tegel verplaatsbaar is: schuift de tegel in de
        configuratie van het bord en geeft True. Als dat niet het geval is, blijft
        het bord in de oorspronkelijke configuratie en functie geeft False.
        """

    def print_board(board: Board) -> None:
        """
        Print alle rijen van het bord onder elkaar. Het format is zoals in de
        voorbeelden onderaan de opdracht.
        """

    def create_board() -> Board:
        """
        Initialiseert een bord van formaat 4 x 4.
        Sorteert de nummers op aflopende volgorde van links boven naar rechts beneden.
        De volgorde van de tegels 1 en 2 is verwisseld.
        """

    if __name__ == '__main__':
        print("Welkom bij de schuifpuzzel!")
        board = create_board()
        while not is_won(board):
            print_board(board)
            tile = input("Tegel die je wil schuiven: ")
            valid = move_tile(board, int(tile))
            if not valid:
                print("Deze tegel kan je niet schuiven.")
        print("Gefeliciteerd, je hebt de schuifpuzzel opgelost!")

## Tips

* Bovenaan het programma declareren we een type genaamd `Board`. Je ziet dat dit eigenlijk een lijst van lijsten met daarin integers is.

    * Tip: we gebruiken hier `list` met een kleine letter. In het boek laat men zien dat je een "list van iets" kunt declareren als `List[iets]` maar dit is inmiddels verouderd. Het voordeel is dat je geen `import` meer hoeft te doen hiervoor.
    
    * Heb je de verouderde Python 3.7 of 3.8? Gebruik dan `Board = List[List[int]]` met hoofdletters.

* Voor het board in dit programma zijn dit 4 lijsten van
  lengte 4. Als je het bord gaat vullen, is het dus handig om hem rij voor rij in te vullen. De lege tegel wordt gerepresenteerd door het cijfer 0.

* Bij `move_tile()` moet je zowel de rij als de kolom van de te verplaatsen tegel en het lege veld
  weten. Dit kan je dan ook gebruiken om te checken of de gekozen tegel verplaatst kan worden.
  Hierbij moeten de tegels in ieder geval ofwel in dezelfde rij staan ofwel in dezelfde kolom. Waar
  moeten de tegels nog meer aan voldoen?

* Bij `is_won()` moet je checken of het bord in de goede configuratie staat. Doordat de volgorde
  oplopend is, is dit goed te tellen door middel van een teller in een dubbele `for`-loop.

* Als je meerdere keren achter elkaar wil printen (op één regel) moet je `print` aanpassen zodat er geen ENTER of newline wordt geprint. Dat kan zo: `print(getal, end="")`. Het gaat hier om het opgeven van `end=""` als argument aan `print`.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python schuifpuzzel.py
    Welkom bij de schuifpuzzel!
     15 14 13 12
     11 10  9  8
      7  6  5  4
      3  2  1  0
    Tegel die je wil schuiven: 4
     15 14 13 12
     11 10  9  8
      7  6  5  0
      3  2  1  4
    Tegel die je wil schuiven: 5
     15 14 13 12
     11 10  9  8
      7  6  0  5
      3  2  1  4
    Tegel die je wil schuiven: 2
    Deze tegel kan je niet schuiven.
     15 14 13 12
     11 10  9  8
      7  6  0  5
      3  2  1  4
    Tegel die je wil schuiven: 6
     15 14 13 12
     11 10  9  8
      7  0  6  5
      3  2  1  4
    Tegel die je wil schuiven:
    ...
    ...
    ...
      1  2  3  4
      5  6  7  8
      9 10 11  0
     13 14 15 12
    Tegel die je wil schuiven: 12
    Gefeliciteerd, je hebt de schuifpuzzel opgelost!

## Testen

Je kunt je oplossing testen met hulp van een [tekstbestand met de oplossing van de puzzel](solution.txt). Met het volgende commando kun je de inhoud van het tekstbestand doorgeven aan je programma:

    python schuifpuzzel.py < solution.txt

De bestanden moeten dan wel in dezelfde directory staan!
