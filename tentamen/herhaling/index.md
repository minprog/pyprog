# Herhaling voor tentamen deel 1

> Maak deze opgaven als je de tussentoets nog niet gehaald hebt.

## Opgave 1 (van het makkelijkere soort)

Schrijf een functie die bepaalt of de elementen in parameter `lst` gesorteerd zijn, dat wil zeggen: elk element is niet kleiner dan het vorige element.

    is_sorted(lst: list[object]) -> bool

Voorbeeld
: `['a', 'b', 'c']` is gesorteerd

Uitgangspunt
: elementen in de gegeven lijst zullen vergelijkbaar zijn met de operator `<`

Verplicht gebruiken
: een for-loop voor de lijst, de operator `<`

Niet gebruiken
: de lijst sorteren mag niet

## Opgave 2 (van het minder makkelijke soort)

Schrijf een functie die bepaalt of parameter \texttt{password} minimaal twee cijfers heeft, een hoofdletter en een kleine letter.

    verb|password_check(password: str) -> bool

Voorbeeld
: `'Rariteit22'` geeft `True`

Uitgangspunt
: parameter `password` is een willekeurige string

Verplicht gebruiken
: een for-loop die één teken per keer neemt, variabelen om tellers bij te houden, en `c.isdigit()`, `c.isupper()` en `c.islower()` om te kijken wat voor teken `c` is

Niet gebruiken
: `split`, `find`, enz.
