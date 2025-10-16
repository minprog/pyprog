# String-analyse

Maak een Python-module genaamd `analyse.py`. Schrijf de volgende functies met doctests. Je maakt voor deze opgave geen `main`, maar wel doctests!

## Spacing

Schrijf een functie `isspace` die een string `s` aanneemt met daarin één teken en bepaalt of deze string "witruimte" is. Een teken is witruimte als het één van de volgende tekens is:

- spatie (`" "`)
- tab (`"\t"`)
- newline (`"\n"`)

Je kunt deze tekens opnemen in je code zoals hierboven geschreven.

De functie kan uit één regel bestaan:

    def isspace(c: str) -> bool:
        return <hier de formule of c witruimte is>

- Wat moet de functie doen als de gegeven string meer dan één teken bevat? Dat is niet gedefinieerd in deze opgave. Je mag dit negeren.
- Schrijf minstens twee doctests.

## Klinker-check

Schrijf een functie `isvowel` die een string `s` aanneemt met daarin één *of meer* tekens en bepaalt of alle tekens in deze string klinkers zijn. Als klinkers beschouwen we: `a`, `e`, `i`, `o` en `u`.

Je moet dus checken of <u>alle</u> tekens klinkers zijn. De logica gebiedt dat als je maar één teken tegenkomt dat <u>geen</u> klinker is, je `False` mag returnen. Het ziet er dan zo uit:

    for char in s:
        if ...:
            return False
    return True

- Wat moet de functie doen als de gegeven string leeg is? `True` returnen. Check dit in een extra doctest.

## Eén klinker

Schrijf een functie `has_single_vowel` die een string `s` aanneemt. De functie checkt of er minimaal en maximeel één klinker in voorkomt. Je moet dus alle tekens afgaan en een teller bijhouden. Om te checken of één teken een klinker is gebruik je de eerder gemaakte functie `isvowel`.

    aantal_klinkers = 0
    for char in s:
        if ...:
            klinkers += 1
    <hier code om een conclusie te trekken op basis van aantal_klinkers>

## Klinkers tellen

Schrijf een functie `count_vowels` die een string `s` aanneemt en telt hoeveel klinkers erin voorkomen. Als de string leeg is dan is het resultaat ook gewoon `0`.

Gebruik de template van de vorige oefening! Een groot deel kun je hergebruiken.
