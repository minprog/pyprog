# Temperatuurtabellen

Graden Celsius en graden Fahrenheit staan met elkaar in verband via `F = (18C + 320) / 10` en andersom `C = (10F - 320) / 18`. Een conversietabel kan er als volgt uitzien. Deze is op basis van de temperatuur in Celcius, en loopt van 0° tot en met 20°, in stappen van 5 graden.

|      C |   F|
|-------:|---:|
|      0 |  32|
|      5 |  41|
|     10 |  50|
|     15 |  59|
|     20 |  68|


## Opdracht

Schrijf, in een bestand genaamd `temperatuur.py`, een programma dat de gebruiker vraagt om de eenheid van temperatuur: `C` van Celsius of `F` van Fahrenheit. Vervolgens vraagt het programma om de begintemperatuur, de eindtemperatuur en de stapgrootte. Daarna wordt een nette tabel uitgeprint, met op iedere rij een temperatuur in de gekozen eenheid en daarbij de omgerekende temperatuur.

* Je programma moet niet gevoelig zijn voor hoofdletters: zowel `c` als `C` moeten worden gezien als Celsius.
* De eindtemperatuur moet groter zijn dan de begintemperatuur.
* De stapgrootte moet een positief geheel getal zijn.
* Je moet de getallen (en letters) rechts uitlijnen.
* Alle temperaturen worden op gehele graden naar *boven* afgerond.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def convert_temperature(old_type: str, old_temp: str) -> int:
        """
        Zet de temperatuur (old_temp) van het type old_type om naar
        de temperatuur van het nieuwe type.
        """

    def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int):
        """
        Print de conversie-tabel.
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Tips

* Voor het uitlijnen van de getallen zijn er verschillende technieken. Denk aan `str.format()` voor het omzetten van getallen naar strings, of `str.rjust()`. Ook kun je [f-strings gebruiken](https://peps.python.org/pep-0498/) om dit voor elkaar te krijgen.

* We gaan ervan uit dat we geen temperaturen tegenkomen in de duizendtallen. Dit houdt in dat je ervan uit mag gaan dat er voor drie karakters ruimte moet zijn in de tabel, precies zoals in de voorbeelden hieronder.

## Voorbeelden

Je programma moet uiteindelijk exact werken zoals in de voorbeelden hieronder.

    $ python temperatuur.py
    Welke eenheid van temperatuur (C of F)? C
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 20
    Wat is de stapgrootte? 5
      C |   F
      0 |  32
      5 |  41
     10 |  50
     15 |  59
     20 |  68

    $ python temperatuur.py
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 10
    Wat is de stapgrootte? 2
      F |   C
      0 | -17
      2 | -16
      4 | -15
      6 | -14
      8 | -13
     10 | -12

    $ python temperatuur.py
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 10
    Wat is de stapgrootte? 3
      F |   C
      0 | -17
      3 | -16
      6 | -14
      9 | -12

    $ python temperatuur.py
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 100
    Wat is de eindtemperatuur? 0
    Wat is de stapgrootte? 3
      F |   C

    $ python temperatuur.py
    Welke eenheid van temperatuur (C of F)? v
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 9
    Wat is de stapgrootte? -3
    Wat is de stapgrootte? 0
    Wat is de stapgrootte? 3
      F |   C
      0 | -17
      3 | -16
      6 | -14
      9 | -12
