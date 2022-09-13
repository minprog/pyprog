# Sjoelen

Sjoelen is een oud Nederlands spel dat je zowel in je eentje als tegen anderen kan spelen. Iedere speler speelt drie rondes waarbij die probeert 30 schijven in vier verschillende gleuven te krijgen.

De vier gleuven hebben een verschillend aantal punten: 2, 3, 4, en 1. Wanneer in elke gleuf een sjoelsteen is geschoven, levert dit 20 punten op. Alle overige stenen die geen deel uitmaken van zo'n 'kwartet' tellen voor de waarde van het bakje waarin ze zijn geschoven.
Wanneer er bijvoorbeeld `[3, 4, 3, 5]` stenen in de verschillende bakken liggen, zijn er drie kwartetten die samen `3*20 = 60` punten opleveren. Daarna houdt je nog `[0, 1, 0, 2]` over in de bakken, dit samen is `0 * 1 + 1 * 3 + 0 * 4 + 2 * 1 = 5` punten. Bij elkaar resulteert dit in `60 + 5 = 65` punten.

Om een sjoelspel te simuleren nemen we aan dat per geschoven steen de kans 25% is dat die in een van de vier gleuven komt (en 75% dat het mis is).
Wanneer een steen in een bak komt is de kans 30% dat die in een bak met 1 punt komt, 30% voor 2 punten, 20% voor 3 punten, en 20% voor 4 punten.

## Opdracht

Schrijf, in een bestand genaamd `sjoelen.py`, een programma waarbij je drie rondes van een sjoelspel simuleert. Hierbij moet je bijhouden hoeveel stenen in de verschillende bakken liggen en uitrekenen hoeveel punten er behaald zijn.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def calculate_points(board: list) -> int:
        """
        Bereken het aantal punten dat is behaald met sjoelen. De volgorde van de punten is [2, 3, 4, 1]. Wanneer er een kwartet tussen zit, telt dit voor 20 punten.
        """

    def shuffle_round(board: list, stones: int):
        """
        Simuleer een ronde sjoelen. Return het bord en het aantal stenen dat nog geschoven kan worden.
        """

    if __name__ == '__main__':
        Zet het bord en het aantal stenen, simuleer drie rondes en bereken het aantal punten.

## Tips

* We werken hier met kansen. Er zijn verschillende manieren om dit te simuleren. Een manier is om een willekeurig getal tussen de 0 en 1 te genereren. Door dit getal met de gegeven kans te vergelijken kan je bepalen of iets wel of niet is gelukt. In ons geval is er een 25% kans dat een steen in een gleuf komt, dus als we een willekeurig getal `x` tussen de 0 en 1 generen (met bijvoorbeeld `random.uniform(0,1)`) kunnen we kijken of dit getal groter of kleiner dan 0.25 is. Als `x <= 0.25` is de steen succesvol in een gleuf geschoven, bij `x > 0.25` niet.
* Bij het bepalen van de gleuf werken we met vier kansen die samen optellen tot 1 (0.3 + 0.2 + 0.2 + 0.3 = 1). Als we hierbij bijvoorbeeld stellen dat de schijf in de gleuf met twee punten komt als `x <= 0.3`, dan kunnen we zeggen dat die in de schijf met drie punten komt als `0.3 < x <= 0.5`.
* Let op: je wil de lijst met je eindconfiguratie nog een keer printen. Zorg dus dat je de lijst niet veranderd bij het berekenen van je punten.


## Voorbeelden

    $ python sjoelen.py
    Je bent geëindigd op deze configurate: [4, 3, 3, 5]
    Dat zijn 64 punten!

    $ python sjoelen.py
    Je bent geëindigd op deze configurate: [2, 4, 6, 2]
    Dat zijn 62 punten!

    $ python sjoelen.py
    Je bent geëindigd op deze configurate: [6, 2, 3, 7]
    Dat zijn 57 punten!
