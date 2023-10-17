# String functions

Maak een Python-bestand aan genaamd `string_functions.py`.

Voeg de volgende functies toe, vul de uitkomsten van de voorbeelden (examples) aan, en voeg een implementatie (body) toe:

    def repeat(s: str, n: int) -> str:
      """ Return s repeated n times; if n is negative, return the empty string.

      >>> repeat('yes', 4)
      'yesyesyesyes'
      >>> repeat('no', 0)

      >>> repeat('no', -2)

      >>> repeat('yesnomaybe', 3)

      """

    def total_length(s1: str, s2: str) -> int:
      """ Return the sum of the lengths of s1 and s2.

      >>> total_length('yes', 'no')
      5
      >>> total_length('yes', '')

      >>> total_length('YES!!!!', 'Noooooo')

      """

## Hint

Gebruik alleen wat je uit het boek geleerd hebt! Constructies zoals `if`, `for` en `while` zijn niet toegestaan.

## Testen

Je kunt testen of je functie correct is door je bestand in te leveren op deze pagina. Maar je kunt ook je functie handmatig testen:

- Start `python -i string_functions.py`. Jouw programma wordt dan ingeladen en je krijgt een prompt `>>>` om commando's in te voeren.

- Tik bijvoorbeeld in `repeat('yes', 4)` om te kijken of je functie het juiste antwoord geeft.
