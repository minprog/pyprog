# Binair tellen

Computers rekenen binair, omdat de berekeningen met transistors gedaan worden die alleen de stand "aan" en "uit" kennen. Door een hoop aan/uit achter elkaar te zetten kun je getallen representeren. 

![embed](https://www.youtube-nocookie.com/embed/gs4Sb4ar4qw?si=0DIIeXw9UevbSkMy)

Schrijf, in een bestand genaamd `binair.py`, een programma dat om vier bits vraagt (0 of 1) en dit omzet naar een decimaal getal en uitprint.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python binair.py
    bit 1: 0
    bit 2: 1
    bit 3: 0
    bit 4: 0
    4

    $ python binair.py
    bit 1: 1
    bit 2: 1
    bit 3: 1
    bit 4: 1
    15

    $ python binair.py
    bit 1: 0
    bit 2: 1
    bit 3: 0
    bit 4: 1
    5

## Code

Ontwerp je code zoals hieronder beschreven.
Vul de docstring aan met doctests en de gewenste uitkomsten, en eventueel verdere uitleg over je aanpak.
Schrijf ook code om invoer te vragen en de functie aan te roepen.

    def convert(bit1: int, bit2: int, bit3: int, bit4: int) -> int:
        """
        Zet het getal dat gerepresenteerd wordt door bit1 t/m bit 4
        om in decimale representatie.
        """
    
    if __name__ == '__main__':
        <vraag input van de gebruiker, roep convert aan, print de uitkomst>

## Hints

Gebruik een enkele expressie om de bits hun waarde te geven en een decimaal getal te maken. Dit zijn de waardes van de bits:

| bit | waarde |
|:---:|:------:|
|  1  | 8      |
|  2  | 4      |
|  3  | 2      |
|  4  | 1      |

## Testen

Probeer je programma uit en gebruik een externe referentie om de werking te valideren. Als je toch een bug spot, pas dan je programma aan.
