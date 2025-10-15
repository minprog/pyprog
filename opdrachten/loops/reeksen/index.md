# Loops: reeksen

In deze opdracht schrijf je een Python-module met daarin diverse functies die iets printen. Een `main` wordt hier niet gevraagd.

Lees paragraaf 4.7 van het boek over het printen van reeksen.

In deze opgave maak je voor elke reeks een aparte functie. Het algemene formaat is zoals in het volgende voorbeeld. Je moet diverse aanpassingen aan doen voor de opgaven! Denk na over welke delen van de code je kan aanpassen om de reeks te veranderen, en wat voor effect elke verandering heeft.

    def reeks() -> None:
        """
        >>> reeks()
        10
        20
        30
        40
        50
        """
        for i in range(1, 6, 1):
            print(i * 10)

Je ziet hierboven dat we één doctest hebben omdat de functie altijd dezelfde reeks print. Datzelfde doe je bij alle functies hieronder.

## Opgaven

1. Schrijf een functie `reeks1` die met hulp van een `for`-loop precies 10 waarden van deze reeks print: `0 2 4 6 8 10 ...`

1. Schrijf een functie `reeks2` die met hulp van een `for`-loop precies 12 waarden van deze reeks print: `1 3 5 7 9 11 ...`

1. Schrijf een functie `reeks3` die met hulp van een `for`-loop precies 15 waarden van deze reeks print: `1 2 5 10 17 26 37 ...`

1. Schrijf een functie `reeks4` die met hulp van een `for`-loop precies 9 waarden van deze reeks print: `5 4 3 2 1 0 -1 -2 -3 ...`

1. Schrijf een functie `reeks5` die met hulp van een `while`-loop precies 7 waarden van deze reeks print: `1 3 9 27 81 ...` (gebruik `*` om te vermenigvuldigen)

1. Schrijf een functie `reeks6` die met hulp van een `while`-loop precies 10 waarden van deze reeks print: `1000 100 10 1 0 0 ...` (gebruik hier `//` om te delen)

1. Schrijf een functie `reeks7` die met hulp van een `for`-loop met een `if` precies 10 waarden van deze reeks print: `1 2 * 4 5 * 7 8 * 10 ...`

1. Schrijf een functie `reeks8` die met hulp van een `while`-loop met een `if` precies 10 waarden van deze reeks print: `1 2 # 8 16 # 64 128 # 512 ...` (gebruik `*` om te vermenigvuldigen)
