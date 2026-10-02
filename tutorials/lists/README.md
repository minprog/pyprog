# Tutorial: lists

Een list is een reeks waarden in een vaste volgorde. Je kent dat al van
strings, maar een list kan elke soort waarde bevatten, en je kunt hem
aanpassen. In deze tutorial bouw je stap voor stap een aantal kleine functies
die met lists werken.

**Hoe het werkt.** Bij elke stap krijg je de code voor één functie.
Kopieer die naar de editor hiernaast en vervang de `...` door je eigen code.
Klik op de knop **doctest** om alle functies te controleren die je schrijft.
Als alle doctests goed zijn, klik dan op **typecheck** om te zorgen dat je types goed zijn.

Werk de pagina's op volgorde door, want elke pagina bouwt voort op de vorige.

{% next "Beginnen" %}

## 1. Lists maken en teruggeven

Een list schrijf je met blokhaken, met komma's tussen de waarden. De lege list
`[]` is net zo goed een list.

    [1, 2, 3]
    ["a", "b", "c"]
    []

Schrijf eerst een functie die een list teruggeeft. Altijd dezelfde, zie de
doctest die al geschreven is.

```python
def make_list() -> list[int]:
    """
    >>> make_list()
    [1, 2, 3]
    """
    return ...
```

{% next "Verder: indexeren" %}

## 2. Indexeren

Net als bij strings heeft elk element een **index**, en je telt vanaf 0.
Ook negatieve indexen werken: `xs[-1]` is het laatste element.

```
 "a"  "b"  "c"
  0    1    2
 -3   -2   -1
```

Schrijf een functie die het eerste element van een list teruggeeft.

```python
def first_item(xs: list[str]) -> str:
    """
    >>> first_item(["a", "b", "c"])
    'a'
    >>> first_item(["x"])
    'x'
    """
    return ...
```

{% next "Verder: het laatste element" %}

Schrijf een functie die het laatste element teruggeeft. Je hoeft de lengte van
de list niet te weten.

```python
def last_item(xs: list[int]) -> int:
    """
    >>> last_item([10, 20, 30])
    30
    >>> last_item([5])
    5
    """
    return ...
```

{% next "Verder: lengte en bereik" %}

## 3. Lengte en bereik

`len(xs)` geeft het aantal elementen. Met een **slice** pak je een stuk van
een list. Het resultaat is een nieuwe list:

    xs = [10, 20, 30, 40]
    xs[1:3]  ->  [20, 30]
    xs[:2]   ->  [10, 20]
    xs[2:]   ->  [30, 40]

Het element bij de eerste index hoort erbij, dat bij de tweede niet.

Schrijf een functie die de eerste twee elementen teruggeeft.

```python
def first_two(xs: list[int]) -> list[int]:
    """
    >>> first_two([10, 20, 30, 40])
    [10, 20]
    >>> first_two([1, 2])
    [1, 2]
    """
    ...
```

{% next "Verder: een element aanpassen" %}

## 4. Een list aanpassen

Anders dan een string kun je een list wel aanpassen. Met een toewijzing
verander je het element op een bepaalde plek:

    xs[0] = "nieuw"

Dit verandert de list zelf, het maakt geen kopie. Een functie die dat doet
hoeft dus niets terug te geven.

Schrijf een functie die het eerste element van `xs` vervangt door `value`.
Je ziet in de doctest hoe je kunt controleren of de list echt is aangepast.

```python
def replace_first(xs: list[str], value: str) -> None:
    """
    >>> letters = ["x", "y", "z"]
    >>> replace_first(letters, "A")
    >>> letters
    ['A', 'y', 'z']
    """
    ...
```

{% next "Verder: elementen toevoegen" %}

## 5. Elementen toevoegen

Een list kun je laten groeien met methoden. Een methode roep je aan met een
punt achter de list:

    xs.append(4)        # zet 4 achteraan
    xs.insert(1, 99)    # zet 99 op index 1, de rest schuift op

Ook deze methoden passen de list zelf aan. Ze geven niets terug, dus schrijf
nooit `xs = xs.append(4)`.

Schrijf een functie die `item` achteraan toevoegt.

```python
def add_last(xs: list[int], item: int) -> None:
    """
    >>> numbers = [1, 2]
    >>> add_last(numbers, 3)
    >>> numbers
    [1, 2, 3]
    """
    ...
```

{% next "Verder: op een plek invoegen" %}

Schrijf een functie die `item` op de gegeven index invoegt.

```python
def add_at(xs: list[str], index: int, item: str) -> None:
    """
    >>> letters = ["a", "c"]
    >>> add_at(letters, 1, "b")
    >>> letters
    ['a', 'b', 'c']
    """
    ...
```

{% next "Verder: elementen verwijderen" %}

## 6. Elementen verwijderen

Ook verwijderen doe je met methoden:

    xs.remove(2)    # haalt de eerste 2 weg
    xs.pop()        # haalt het laatste element weg en geeft het terug
    xs.pop(0)       # haalt het element op index 0 weg en geeft het terug

`remove` zoekt op waarde en haalt alleen het eerste exemplaar weg. `pop` werkt
op positie.

Schrijf een functie die de eerste voorkomende `value` uit de list haalt.

```python
def remove_first(xs: list[int], value: int) -> None:
    """
    >>> numbers = [1, 2, 3, 2]
    >>> remove_first(numbers, 2)
    >>> numbers
    [1, 3, 2]
    """
    ...
```

{% next "Verder: pop gebruiken" %}

Schrijf een functie die het laatste element uit de list haalt en teruggeeft.
Na afloop is de list dus een element korter.

```python
def take_last(xs: list[int]) -> int:
    """
    >>> numbers = [1, 2, 3]
    >>> take_last(numbers)
    3
    >>> numbers
    [1, 2]
    """
    return ...
```

{% next "Verder: lists combineren" %}

## 7. Lists combineren

Net als bij strings plakt `+` twee lists aan elkaar en herhaalt `*` een list.
Het resultaat is steeds een nieuwe list. De originelen blijven zoals ze waren.

    [1, 2] + [3]    ->  [1, 2, 3]
    [0, 1] * 2      ->  [0, 1, 0, 1]

Schrijf een functie die `a` en `b` combineert tot één nieuwe list.

```python
def combine(a: list[int], b: list[int]) -> list[int]:
    """
    >>> combine([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> combine([], [5])
    [5]
    """
    ...
```

{% next "Verder: herhalen" %}

Schrijf een functie die een list van `n` nullen teruggeeft. Dit patroon gebruik
je later vaak om een list met beginwaarden te maken.

```python
def zeros(n: int) -> list[int]:
    """
    >>> zeros(3)
    [0, 0, 0]
    >>> zeros(0)
    []
    """
    ...
```

{% next "Verder: zoeken" %}

## 8. Controleren en zoeken

Met `in` controleer je of een waarde in een list voorkomt. Met `.index()` vind
je op welke plek het eerste exemplaar staat, en met `.count()` tel je hoe vaak
een waarde voorkomt:

    3 in [1, 2, 3]            ->  True
    [5, 6, 7].index(7)        ->  2
    [1, 2, 2, 3].count(2)     ->  2

`.index()` geeft een foutmelding als de waarde er niet in zit. Controleer dus
eerst met `in`.

Schrijf een functie die controleert of `value` in `xs` zit.

```python
def has_value(xs: list[str], value: str) -> bool:
    """
    >>> has_value(["a", "b", "c"], "b")
    True
    >>> has_value(["a", "b", "c"], "z")
    False
    """
    ...
```

{% next "Verder: tellen" %}

Schrijf een functie die telt hoe vaak `value` in `xs` zit, met de methode
`.count()`.

```python
def count_value(xs: list[int], value: int) -> int:
    """
    >>> count_value([1, 2, 2, 3], 2)
    2
    >>> count_value([1, 2, 3], 9)
    0
    """
    ...
```

{% next "Verder: een positie vinden" %}

Schrijf een functie die de index van het eerste exemplaar van `value`
teruggeeft, of `-1` als het er niet in zit. Dit is hetzelfde patroon als bij
strings: eerst controleren, dan pas zoeken.

```python
def position(xs: list[str], value: str) -> int:
    """
    >>> position(["a", "b", "c"], "c")
    2
    >>> position(["a", "b", "c"], "z")
    -1
    """
    ...
```

{% next "Verder: loopen" %}

## 9. Een list langslopen

Je loopt een list langs zoals je een string langsloopt. Een teller of totaal
begin je vóór de loop:

    total = 0
    for number in xs:
        total += number

Schrijf een functie die alle getallen in de list bij elkaar optelt. Gebruik een
loop en niet `sum()`. Een lege list heeft som 0.

```python
def total(xs: list[int]) -> int:
    """
    >>> total([1, 2, 3])
    6
    >>> total([])
    0
    """
    ...
```

{% next "Verder: het grootste getal" %}

Voor het grootste getal houd je het grootste getal tot nu toe bij. Begin met het
eerste element en vergelijk de rest ermee. Je mag aannemen dat de list niet
leeg is. Gebruik een loop en niet `max()`.

```python
def biggest(xs: list[int]) -> int:
    """
    >>> biggest([3, 9, 2])
    9
    >>> biggest([-5, -2, -8])
    -2
    >>> biggest([7])
    7
    """
    ...
```

{% next "Verder: een nieuwe list opbouwen" %}

## 10. Een nieuwe list opbouwen

Dit is hetzelfde accumulator-patroon als bij strings, maar dan met een lege
list en `append`:

    result = []
    for item in xs:
        if ...:
            result.append(item)
    return result

Schrijf een functie die alleen de positieve getallen (groter dan 0)
teruggeeft, in dezelfde volgorde.

```python
def positives(xs: list[int]) -> list[int]:
    """
    >>> positives([-2, 0, 5, 7, -1])
    [5, 7]
    >>> positives([-1, -2])
    []
    """
    ...
```

{% next "Verder: elk element veranderen" %}

In plaats van te kiezen kun je ook elk element veranderen. Schrijf een functie
die een **nieuwe** list teruggeeft met elk getal vermenigvuldigd met `factor`.
De list die je meekrijgt mag niet veranderen.

```python
def multiply_all(xs: list[int], factor: int) -> list[int]:
    """
    >>> multiply_all([1, 2, 3], 10)
    [10, 20, 30]
    >>> numbers = [1, 2]
    >>> multiply_all(numbers, 5)
    [5, 10]
    >>> numbers
    [1, 2]
    """
    ...
```

{% next "Verder: loopen met een index" %}

## 11. Loopen met een index

Soms heb je de positie nodig, bijvoorbeeld om twee naburige elementen te
vergelijken:

    for index in range(len(xs) - 1):
        if xs[index] > xs[index + 1]:
            ...

Let op de `- 1`: bij het laatste element bestaat `xs[index + 1]` niet meer.

Schrijf een functie die controleert of de getallen van klein naar groot staan.
Gelijke getallen naast elkaar mogen. Een list met 0 of 1 element is altijd
goed.

```python
def is_sorted(xs: list[int]) -> bool:
    """
    >>> is_sorted([1, 2, 2, 5])
    True
    >>> is_sorted([1, 3, 2])
    False
    >>> is_sorted([])
    True
    """
    ...
```

{% next "Verder: sorteren en kopiëren" %}

## 12. Sorteren en kopiëren

Er zijn twee manieren om te sorteren, en het verschil is belangrijk:

    sorted(xs)    # geeft een nieuwe, gesorteerde list; xs blijft zoals hij was
    xs.sort()     # sorteert xs zelf en geeft niets terug

Schrijf een functie die een gesorteerde kopie teruggeeft en de originele list
niet aanpast.

```python
def sorted_copy(xs: list[int]) -> list[int]:
    """
    >>> numbers = [3, 1, 2]
    >>> sorted_copy(numbers)
    [1, 2, 3]
    >>> numbers
    [3, 1, 2]
    """
    ...
```

{% next "Verder: een alias" %}

Als je een list aan een tweede variabele toewijst, kopieer je hem niet. Je hebt
dan twee namen voor dezelfde list:

    a = [1, 2]
    b = a
    b.append(3)
    a       ->  [1, 2, 3]

Wil je echt een losse kopie, gebruik dan `xs.copy()` (of `xs[:]`).

Schrijf een functie die `xs` kopieert, aan de kopie `0` toevoegt en de kopie
teruggeeft. De originele list moet hetzelfde blijven.

```python
def with_zero(xs: list[int]) -> list[int]:
    """
    >>> numbers = [1, 2]
    >>> with_zero(numbers)
    [1, 2, 0]
    >>> numbers
    [1, 2]
    """
    ...
```

{% next "Afronden" %}

## Klaar

Klik nog één keer op **doctest** en **typecheck**.
Als er staat dat alle tests slagen, en er geen problemen met types zijn,
dan ben je klaar met de tutorial.

Slaagt er nog iets niet, verbeter dan je code en vraag om hulp als je er niet uitkomt.
