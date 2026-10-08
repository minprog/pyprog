# Tutorial: herhalen met loops

Met functies die iets uitrekenen kun je al veel. Maar soms moet je iets
meerdere keren doen: een reeks getallen laten zien, alle jaren in een periode
langslopen, of doorzoeken tot je iets gevonden hebt. Daarvoor zijn loops.

**Hoe het werkt.** Elke pagina hieronder laat één functie zien. Kopieer die naar
`loops_python.py` in de editor en vervang de `...` door je eigen code. Klik
op de knop **doctest** om alle functies te controleren die je tot dan toe
geschreven hebt. De regels met `>>>` in elke functie zijn de tests: ze laten een
aanroep zien en wat daarvan op het scherm moet verschijnen of wat eruit moet
komen.

Werk de pagina's op volgorde door; elke pagina bouwt voort op de vorige.

{% next "Beginnen" %}

## 1. Getallen printen met een for-loop

Een `for`-loop voert dezelfde code meerdere keren uit. Dit voorbeeld laat de
getallen 1 tot en met 5 zien, elk op een eigen regel:

    for i in range(1, 6):
        print(i)

Dit gebeurt er:

- `i` is de **loopvariabele**. Bij elke ronde krijgt `i` de volgende waarde.
- `range(1, 6)` levert de getallen vanaf 1 tot **voor** 6. Het eerste getal
  doet dus mee, het laatste niet. Je krijgt 1, 2, 3, 4 en 5.
- Alleen de regels die ingesprongen staan onder de `for` worden herhaald.
- Schrijf je `range(6)`, dan begin je bij 0 en krijg je 0, 1, 2, 3, 4 en 5.

Let op het verschil met wat je tot nu toe deed. Eerder gaf een functie een
antwoord terug met `return`. Hier laat de functie iets zien op het scherm met
`print`. De functie geeft zelf niets terug, en daarom staat er `-> None` achter
de header. In de test zie je daarom onder de aanroep precies de regels staan die
geprint worden.

Kopieer de functie naar de editor en klik op **doctest**.

```python
def print_one_to_five() -> None:
    """
    >>> print_one_to_five()
    1
    2
    3
    4
    5
    """
    for i in range(1, 6):
        print(i)
```

{% next "Verder: zelf een reeks printen" %}

Nu zelf. Print de kwadraten van 1 tot en met 6. Binnen de loop mag je
rekenen met `i`, bijvoorbeeld `print(i * 10)` om tientallen te printen.

```python
def print_squares() -> None:
    """
    >>> print_squares()
    1
    4
    9
    16
    25
    36
    """
    ...
```

{% next "Verder: een stapgrootte" %}

## 2. Een stapgrootte kiezen

Standaard telt `range` steeds één verder. Met een derde getal bepaal je zelf de
stap:

    range(begin, einde, stap)

Het voorbeeld hieronder print de veelvouden van 5 van 5 tot en met 30:

    for i in range(5, 31, 5):
        print(i)

- Je begint bij 5 en telt steeds 5 erbij op: 5, 10, 15, 20, 25, 30.
- Het einde doet nooit mee. Wil je dat 30 nog wel meedoet, dan zet je er een
  getal achter dat groter is dan 30, maar kleiner dan het volgende getal in de
  reeks (35). Hier werkt 31.

```python
def print_fives() -> None:
    """
    >>> print_fives()
    5
    10
    15
    20
    25
    30
    """
    for i in range(5, 31, 5):
        print(i)
```

{% next "Verder: zelf een stapgrootte kiezen" %}

Print de eerste zeven veelvouden van 7, dus 7 tot en met 49.

```python
def print_sevens() -> None:
    """
    >>> print_sevens()
    7
    14
    21
    28
    35
    42
    49
    """
    ...
```

{% next "Verder: aftellen" %}

## 3. Aftellen

De stap mag ook negatief zijn. Dan telt `range` terug:

    for i in range(5, 0, -1):
        print(i)

Dit print 5, 4, 3, 2 en 1. Ook nu doet het einde niet mee: bij een negatieve
stap stopt de loop dus **voor** het einde, en komt 0 er niet in.

```python
def print_countdown() -> None:
    """
    >>> print_countdown()
    5
    4
    3
    2
    1
    """
    for i in range(5, 0, -1):
        print(i)
```

{% next "Verder: zelf aftellen" %}

Tel in stappen van 3 terug van 20 tot en met -1. Let op dat de reeks ook onder
nul komt en dat het einde niet meedoet.

```python
def print_down_by_three() -> None:
    """
    >>> print_down_by_three()
    20
    17
    14
    11
    8
    5
    2
    -1
    """
    ...
```

{% next "Verder: een if in de loop" %}

## 4. Een if in de loop

Je kunt in een loop bij elke ronde iets kiezen met `if` en `else`. Dit voorbeeld
print de getallen 1 tot en met 12, maar zet een uitroepteken in plaats van elk
getal dat deelbaar is door 5:

    for i in range(1, 13):
        if i % 5 == 0:
            print("!")
        else:
            print(i)

- `i % 5 == 0` is waar als `i` deelbaar is door 5. Dit ken je al van
  `is_divisible` uit de eerste tutorial.
- Na `if ...:` en na `else:` komt weer een ingesprongen blok. Dat betekent dat
  `print("!")` hier twee niveaus naar rechts staat: één voor de `for`, één voor
  de `if`.
- Tekst zet je tussen aanhalingstekens. Print je `"!"`, dan zie je een `!` op
  het scherm.

```python
def print_with_exclamations() -> None:
    """
    >>> print_with_exclamations()
    1
    2
    3
    4
    !
    6
    7
    8
    9
    !
    11
    12
    """
    for i in range(1, 13):
        if i % 5 == 0:
            print("!")
        else:
            print(i)
```

{% next "Verder: zelf een voorwaarde kiezen" %}

Print de getallen 1 tot en met 10, maar print een `x` in plaats van elk even
getal. Een getal is even als het deelbaar is door 2.

```python
def print_odds_only() -> None:
    """
    >>> print_odds_only()
    1
    x
    3
    x
    5
    x
    7
    x
    9
    x
    """
    ...
```

{% next "Verder: while" %}

## 5. Doorgaan zolang het kan

Een `for`-loop gebruik je als je van tevoren weet welke getallen je langsloopt.
Soms bepaal je het volgende getal liever zelf, bijvoorbeeld door steeds te
verdubbelen. Dan gebruik je een `while`-loop. Die herhaalt zijn blok zolang een
voorwaarde waar is:

    number = 1
    count = 0
    while count < 6:
        print(number)
        number = number * 2
        count = count + 1

Dit gebeurt er:

- Vóór de loop zet je de variabelen op hun beginwaarde: `number` begint op 1 en
  `count` op 0.
- De voorwaarde `count < 6` wordt voor elke ronde gecontroleerd. Is die niet
  meer waar, dan stopt de loop.
- Binnen de loop pas je de variabelen zelf aan. `number = number * 2` verdubbelt
  `number`, en `count = count + 1` telt mee hoeveel getallen je al hebt
  geprint.
- Vergeet je `count` te verhogen, dan is de voorwaarde altijd waar en stopt de
  loop nooit.

Dit print zes getallen: 1, 2, 4, 8, 16 en 32.

```python
def print_doublings() -> None:
    """
    >>> print_doublings()
    1
    2
    4
    8
    16
    32
    """
    number = 1
    count = 0
    while count < 6:
        print(number)
        number = number * 2
        count = count + 1
```

{% next "Verder: zelf een while-loop schrijven" %}

Print vijf getallen waarvan elk het vorige maal 5 is, beginnend bij 1.

```python
def print_fives_powers() -> None:
    """
    >>> print_fives_powers()
    1
    5
    25
    125
    625
    """
    ...
```

{% next "Verder: delen" %}

## 6. Steeds delen

Delen met `/` geeft altijd een kommagetal. Voor een geheel getal gebruik je `//`,
dat naar beneden afrondt:

    7 // 2      geeft 3
    1 // 2      geeft 0
    0 // 2      geeft 0

Je kunt dit gebruiken om steeds door een getal te delen. Dit voorbeeld halveert
vanaf 100, negen keer:

```python
def print_halvings() -> None:
    """
    >>> print_halvings()
    100
    50
    25
    12
    6
    3
    1
    0
    0
    """
    number = 100
    count = 0
    while count < 9:
        print(number)
        number = number // 2
        count = count + 1
```

Na een tijdje blijft `number` op 0 staan, omdat `0 // 2` weer 0 is. De loop gaat
gewoon door tot `count` 9 bereikt heeft.

{% next "Verder: zelf delen" %}

Begin bij 729 en deel steeds door 3. Print negen getallen.

```python
def print_thirds() -> None:
    """
    >>> print_thirds()
    729
    243
    81
    27
    9
    3
    1
    0
    0
    """
    ...
```

{% next "Verder: tellen" %}

## 7. Tellen met een loop

Nu gebruik je loops om iets uit te rekenen in plaats van te printen. Voor de
volgende opdrachten heb je de functie `is_leap_year` nodig. Die is hier al af:
kopieer hem naar de editor en klik op **doctest**.

```python
def is_leap_year(y: int) -> bool:
    """
    >>> is_leap_year(2024)
    True
    >>> is_leap_year(2023)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
```

Laat hem in het bestand staan, want de functies hieronder roepen hem aan.

Om iets te tellen houd je een variabele bij die je vóór de loop op 0 zet en
waar je binnenin 1 bij optelt met `count = count + 1`. Vergeet niet aan het
eind te `return`'en: dat gebeurt ná de loop, dus minder ver ingesprongen.

Tel zo de schrikkeljaren van `start` tot en met `end`. Denk eraan dat je `end + 1`
nodig hebt in de `range` om `end` mee te laten doen.

```python
def count_leap_years(start: int, end: int) -> int:
    """
    >>> count_leap_years(2000, 2001)
    1
    >>> count_leap_years(2020, 2024)
    2
    >>> count_leap_years(1800, 1900)
    24
    """
    ...
```

{% next "Verder: doorzoeken" %}

## 8. Doorzoeken tot je er bent

Bij het tellen weet je van tevoren welke jaren je langsloopt. Hier niet: je weet
pas dat je klaar bent als je het n-de schrikkeljaar te pakken hebt. Dit is een
taak voor `while`:

    while found < n:
        ...

Begin bij `start` en loop de jaren één voor één af. Tel elk schrikkeljaar dat je
tegenkomt, en zodra je er `n` hebt is het jaar waar je op staat het antwoord.
Je hebt dus een variabele nodig voor het jaar en een voor het aantal dat je
gevonden hebt, en beide pas je binnen de loop aan.

```python
def nth_leap_year(start: int, n: int) -> int:
    """
    >>> nth_leap_year(2000, 1)
    2000
    >>> nth_leap_year(1800, 1)
    1804
    >>> nth_leap_year(2000, 3)
    2008
    """
    ...
```

{% next "Afronden" %}

## Klaar

Klik nog één keer op **doctest**. Als er staat dat alle tests slagen, ben je
klaar met de tutorial.

Slaagt er nog iets niet, dan noemt de uitvoer de functie, de aanroep die
geprobeerd is, wat eruit had moeten komen en wat eruit kwam. Verbeter die ene
functie en klik opnieuw.
