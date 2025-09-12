# String-analyse

Maak een Python-module genaamd `analyse.py`. Schrijf de volgende functies met doctests. Je maakt voor deze opgave geen `main`, maar wel doctests!

## Spacing

Schrijf een functie `isspace` die een string `s` aanneemt met daarin één teken en bepaalt of deze string "witruimte" is. Een teken is witruimte als het één van de volgende tekens is:

- spatie (`" "`)
- tab (`"\t"`)
- newline (`"\n"`)

Je kunt deze tekens opnemen in je code zoals hierboven geschreven.

- Wat moet de functie doen als de gegeven string leeg is? `False` returnen.
- Wat moet de functie doen als de gegeven string meer dan één teken bevat? Dat is niet gedefinieerd in deze opgave. Je mag dit negeren.

## Klinker-check

Schrijf een functie `isvowel` die een string `s` aanneemt met daarin één *of meer* tekens en bepaalt of alle tekens in deze string klinkers zijn. Als klinkers beschouwen we: `a`, `e`, `i`, `o` en `u`.

- Wat moet de functie doen als de gegeven string leeg is? `False` returnen.
- Wat moet de functie doen als de gegeven string meer dan één teken bevat? Alle tekens moeten klinkers zijn, dus wat er moet gebeuren staat hierboven al in de opgave.

## Eén klinker

Schrijf een functie `has_single_vowel` die een string `s` aanneemt. De functie checkt of er minimaal en maximeel één klinker in voorkomt. Je moet dus alle tekens afgaan en een teller bijhouden. Om te checken of één teken een klinker is gebruik je de eerder gemaakte functie `isvowel`.

## Klinkers tellen

Schrijf een functie `count_vowels` die een string `s` aanneemt en telt hoeveel klinkers erin voorkomen. Als de string leeg is dan is het resultaat ook gewoon `0`.
