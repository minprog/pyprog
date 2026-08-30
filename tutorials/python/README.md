# Tutorial: van Karel naar Python

In Karel schreef je instructies die *iets deden*: Karel liep een stap, draaide,
legde een beeper neer. In Python schrijf je meestal functies die *iets
uitrekenen* en het antwoord teruggeven. Zo'n functie krijgt gegevens binnen en
levert een uitkomst op.

De formules die je op het werkblad hebt opgeschreven ga je hier in Python
schrijven.

**Hoe het werkt.** Elke pagina hieronder laat één functie zien. Kopieer die naar
`tutorial_python.py` in de editor en vervang de `...` door je eigen code. Klik
op de knop **doctest** om alle functies te controleren die je tot dan toe
geschreven hebt. De regels met `>>>` in elke functie zijn de tests: ze laten een
aanroep zien en het antwoord dat eruit moet komen.

Werk de pagina's op volgorde door; elke pagina bouwt voort op de vorige.

{% next "Beginnen" %}

## 1. Hoe een functie eruitziet

Hier is een complete functie. Kopieer hem naar de editor en klik meteen op
**doctest**: hij is al af, dus de test slaagt.

```python
def kwadraat(a: int) -> int:
    """
    >>> kwadraat(6)
    36
    >>> kwadraat(2)
    4
    """
    return a * a
```

Wat staat daar precies?

- `def` begint een functie, net zoals `DEFINE-NEW-INSTRUCTION` in Karel een
  instructie begon.
- `kwadraat` is de naam. Tussen de haakjes staan de **parameters**: gegevens die
  de functie binnenkrijgt. Karel-instructies hadden die niet.
- `a: int` zegt dat `a` een geheel getal is, en `-> int` dat er een geheel getal
  uit komt. Python controleert dat niet, maar het vertelt de lezer wat je bedoelt.
- De dubbele punt en het **inspringen** bepalen wat er bij de functie hoort.
  Karel had daar `BEGIN` en `END` voor; Python kijkt naar de witruimte links.
- De tekst tussen `"""` is de docstring. De regels met `>>>` daarin zijn tests.
- `return` geeft het antwoord terug en beëindigt de functie.

{% next "Verder: zelf een functie schrijven" %}

Nu zelf. Dezelfde vorm, alleen de derde macht in plaats van het kwadraat: `a`
maal `a` maal `a`.

```python
def derde_macht(a: int) -> int:
    """
    >>> derde_macht(2)
    8
    >>> derde_macht(5)
    125
    """
    return ...
```

{% next "Verder: meer parameters" %}

## 2. Meer dan één parameter

Een functie kan meerdere parameters hebben; je zet er komma's tussen. Bij het
aanroepen geef je de waarden in dezelfde volgorde mee.

Tel de drie getallen op en deel door 3. Delen doe je met `/`. Let op: daar komt
altijd een kommagetal uit, ook als het precies uitkomt. Daarom staat er `3.0` in
de test en niet `3`.

```python
def avg3(a: float, b: float, c: float) -> float:
    """
    >>> avg3(1, 2, 3)
    2.0
    >>> avg3(10, 20, 60)
    30.0
    """
    return ...
```

{% next "Verder: rekenen" %}

## 3. Rekenen

Python rekent met `+`, `-`, `*` en `/`, en houdt zich aan de voorrangsregels:
eerst vermenigvuldigen en delen, dan optellen en aftrekken. Met haakjes bepaal
je zelf de volgorde.

Celsius naar Fahrenheit gaat met `c` maal 9, gedeeld door 5, plus 32.

```python
def celsius_to_fahrenheit(c: float) -> float:
    """
    >>> celsius_to_fahrenheit(100)
    212.0
    >>> celsius_to_fahrenheit(0)
    32.0
    """
    return ...
```

{% next "Verder: en terug" %}

En weer terug: 32 eraf, dan maal 5, dan gedeeld door 9. Het aftrekken moet hier
eerst gebeuren, dus je hebt haakjes nodig.

```python
def fahrenheit_to_celsius(f: float) -> float:
    """
    >>> fahrenheit_to_celsius(212)
    100.0
    >>> fahrenheit_to_celsius(32)
    0.0
    """
    return ...
```

{% next "Verder: waar of niet waar" %}

## 4. Waar of niet waar

In Karel testte je dingen als `front-is-clear` in een `IF` of `WHILE`. Zo'n test
levert waar of niet waar op. In Python heten die twee waarden `True` en `False`,
en je kunt ze ook gewoon teruggeven met `return`.

Je maakt ze met vergelijkingen: `==` (gelijk aan), `!=` (niet gelijk),
`<`, `>`, `<=`, `>=`. Let op de dubbele `==`: één `=` betekent iets heel anders.

`a % b` is de rest na deling. Geef hier terug of die rest gelijk is aan 0, want
dan is `a` deelbaar door `b`.

```python
def is_divisible(a: int, b: int) -> bool:
    """
    >>> is_divisible(10, 5)
    True
    >>> is_divisible(10, 3)
    False
    """
    return ...
```

{% next "Verder: voorwaarden combineren" %}

Voorwaarden combineer je met `and` (allebei waar), `or` (minstens één waar) en
`not` (omgekeerd). Ook hier helpen haakjes om te laten zien wat bij elkaar hoort.

Een schrikkeljaar is deelbaar door 4 maar niet door 100. Jaren die deelbaar zijn
door 400 zijn óók schrikkeljaren. Daarom is 2000 er wel een en 1900 niet.
Combineer die drie regels tot één voorwaarde.

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
    return ...
```

{% next "Verder: wortels" %}

## 5. Functies uit een bibliotheek

Niet alles hoef je zelf te schrijven. `math.sqrt(x)` geeft de wortel van `x`.
Dat werkt doordat bovenaan `tutorial_python.py` de regel `import math` staat:
daarmee haal je de wiskundefuncties erbij.

Merk op dat je hier een functie *aanroept* binnen je eigen functie, net zoals je
in Karel een zelfgemaakte instructie kon gebruiken in een andere.

Geef de wortel terug van `a` in het kwadraat plus `b` in het kwadraat.

```python
def pythagoras(a: float, b: float) -> float:
    """
    >>> pythagoras(3, 4)
    5.0
    >>> pythagoras(5, 12)
    13.0
    """
    return ...
```

{% next "Verder: drie voorwaarden" %}

Een driehoek klopt als de som van elke twee zijden groter is dan de derde. Dat
zijn drie voorwaarden, en ze moeten alle drie gelden.

```python
def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """
    >>> is_valid_triangle(3, 4, 5)
    True
    >>> is_valid_triangle(1, 2, 10)
    False
    >>> is_valid_triangle(1, 1, 2)
    False
    """
    return ...
```

{% next "Verder: twee antwoorden" %}

## 6. Meer dan één antwoord teruggeven

Soms is het antwoord niet één getal. Dan zet je er komma's tussen:
`return x, y`. Wat je terugkrijgt heet een tuple, en dat zie je in de test terug
als twee waarden tussen haakjes.

Je kunt ook tussenresultaten opslaan in een **variabele**, zodat je ze niet
tweemaal hoeft uit te rekenen:

    d = b * b - 4 * a * c

Bereken eerst de discriminant, en daarna de twee oplossingen van de abc-formule.
Ga ervan uit dat de discriminant groter is dan 0, en geef de grootste oplossing
eerst.

```python
def solve_quadratic(a: float, b: float, c: float) -> tuple:
    """
    >>> solve_quadratic(1, -3, 2)
    (2.0, 1.0)
    >>> solve_quadratic(1, 0, -4)
    (2.0, -2.0)
    """
    ...
```

{% next "Verder: herhalen" %}

## 7. Herhalen

In Karel herhaalde je met `ITERATE 5 TIMES`. In Python doe je dat met een
`for`-loop, en die telt bovendien mee waar je bent:

    for jaar in range(start, end + 1):
        ...

`range(a, b)` levert de getallen `a` tot en met `b - 1`. Wil je `b` er ook bij
hebben, dan schrijf je `range(a, b + 1)`.

Wat je bijhoudt zet je in een variabele die je vóór de loop op 0 zet en er
binnenin ophoogt met `aantal = aantal + 1`. Vergeet niet aan het eind te
`return`'en: dat gebeurt ná de loop, dus minder ver ingesprongen.

Tel zo de schrikkeljaren van `start` tot en met `end`. Je mag daarbij je eigen
`is_leap_year` gebruiken.

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

## 8. Doorgaan tot je er bent

Bij een `for`-loop weet je van tevoren hoe vaak je rondgaat. Hier niet: je weet
pas dat je klaar bent als je het n-de schrikkeljaar te pakken hebt. Daarvoor is
de `while`-loop, dezelfde als Karels `WHILE ... DO`:

    while gevonden < n:
        ...

Begin bij `start` en loop de jaren één voor één af. Tel elk schrikkeljaar dat je
tegenkomt, en zodra je er `n` hebt is het jaar waar je op staat het antwoord.

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
