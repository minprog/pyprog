# Tutorial: collections

Je kent al twee soorten collecties: strings en lists. Python heeft er meer, en
elk soort past bij een ander doel. In deze tutorial leer je er drie kennen:

- een **tuple** bewaart een vaste reeks waarden die je niet meer aanpast,
- een **set** bewaart waarden zonder dubbele,
- een **dict** (dictionary) bewaart waarden onder een naam, zodat je ze daarop terugvindt.

**Hoe het werkt.** Bij elke stap krijg je de code voor één functie.
Kopieer die naar `tutorial_collections.py` in de editor en vervang de `...` door
je eigen code. Klik op de knop **doctest** om alle functies te controleren die
je schrijft. Als alle doctests goed zijn, klik dan op **typecheck** om te
controleren of je types kloppen.

Werk de pagina's op volgorde door; elke pagina bouwt voort op de vorige.

{% next "Beginnen" %}

## 1. Tuples

Een tuple schrijf je met gewone haakjes, met komma's tussen de waarden:

    (1, 2, 3)
    ("a", 10)

Een tuple lijkt op een list, maar je kunt hem niet aanpassen. Een tuple heeft
een vaste lengte en vaste inhoud. Daarom gebruik je hem voor waarden die bij
elkaar horen, zoals een naam met een leeftijd.

Het type van een tuple noem je per plek: `tuple[int, int, int]` is een tuple
met drie gehele getallen. In `tuple[str, int]` staat eerst een string en
daarna een geheel getal.

Schrijf een functie die altijd dezelfde tuple teruggeeft.

```python
def make_tuple() -> tuple[int, int, int]:
    """
    >>> make_tuple()
    (1, 2, 3)
    """
    return ...
```

{% next "Verder: indexeren" %}

Een element uit een tuple haal je op met een index, net als bij een list:
`t[0]` is het eerste element.

```python
def first_of_tuple(t: tuple[int, int, int]) -> int:
    """
    >>> first_of_tuple((10, 20, 30))
    10
    >>> first_of_tuple((7, 8, 9))
    7
    """
    return ...
```

{% next "Verder: een tuple maken" %}

Je kunt een tuple ook maken van variabelen. Dit doe je al sinds de eerste
tutorial: met `return x, y` geef je een tuple terug.

```python
def pair(name: str, age: int) -> tuple[str, int]:
    """
    >>> pair("Sam", 20)
    ('Sam', 20)
    >>> pair("Kim", 31)
    ('Kim', 31)
    """
    return ...
```

{% next "Verder: uitpakken" %}

Je kunt een tuple ook **uitpakken**. Dan krijgt elke waarde meteen een eigen
variabele:

    a, b = (1, 2)

Na deze regel is `a` gelijk aan 1 en `b` gelijk aan 2. Een tuple aanpassen kan
niet, maar je kunt wel een nieuwe tuple maken van de losse waarden.

Wissel de twee waarden in een tuple om. Pak hem eerst uit.

```python
def swap(t: tuple[int, int]) -> tuple[int, int]:
    """
    >>> swap((1, 2))
    (2, 1)
    >>> swap((5, 5))
    (5, 5)
    """
    ...
```

{% next "Verder: sets" %}

## 2. Sets

Een set bewaart waarden zonder dubbele en zonder vaste volgorde. Je schrijft
hem met accolades:

    {1, 2, 3}

Zet je dezelfde waarde twee keer in een set, dan staat hij er maar één keer in.
Een lege set maak je met `set()`. Let op: `{}` is geen lege set maar een lege
dict (zie verderop).

Het type van een set noem je met het type van de elementen: `set[int]` is een
set met gehele getallen.

Omdat een set geen vaste volgorde heeft, vergelijken we sets in de tests met
`==`. Dat is waar als beide sets dezelfde waarden hebben.

```python
def make_set() -> set[int]:
    """
    >>> make_set() == {1, 2, 3}
    True
    """
    return ...
```

{% next "Verder: opzoeken" %}

Met `in` kijk je of een waarde in een set zit. Dat werkt ook bij strings en
lists, maar bij een set gaat het heel snel, ook als de set groot is.

```python
def has_item(s: set[int], x: int) -> bool:
    """
    >>> has_item({1, 2, 3}, 2)
    True
    >>> has_item({1, 2, 3}, 5)
    False
    """
    return ...
```

{% next "Verder: toevoegen" %}

Met `s.add(x)` voeg je een waarde toe aan de set `s`. Net als bij `append` op
een list verandert de set zelf. De functie geeft daarom niets terug, en dat zie
je aan `-> None`. Zit de waarde er al in, dan gebeurt er niets.

```python
def add_item(s: set[int], item: int) -> None:
    """
    >>> s = {1, 2}
    >>> add_item(s, 3)
    >>> s == {1, 2, 3}
    True
    >>> add_item(s, 2)
    >>> s == {1, 2, 3}
    True
    """
    ...
```

{% next "Verder: sets combineren" %}

Twee sets combineer je met `|`. Het resultaat is een nieuwe set met alle waarden
uit beide sets, zonder dubbele. Dit heet de **vereniging** (union).

```python
def union_of_sets(a: set[int], b: set[int]) -> set[int]:
    """
    >>> union_of_sets({1, 2}, {2, 3}) == {1, 2, 3}
    True
    >>> union_of_sets(set(), {4}) == {4}
    True
    """
    return ...
```

{% next "Verder: een list omzetten" %}

Met `set(xs)` maak je een set van een list, of van een string. De dubbele
waarden verdwijnen daarbij vanzelf. Met `len` tel je dan hoeveel verschillende
waarden er waren.

Geef terug hoeveel verschillende getallen er in de list staan.

```python
def count_different(xs: list[int]) -> int:
    """
    >>> count_different([1, 2, 2, 3, 1])
    3
    >>> count_different([])
    0
    """
    return ...
```

{% next "Verder: dicts" %}

## 3. Dicts

Een dict bewaart waarden onder een **sleutel** (key). Je zoekt een waarde op
met zijn sleutel, niet met een plaats in een rij. Je schrijft een dict met
accolades, met `sleutel: waarde` tussen komma's:

    {"a": 1, "b": 2}
    {"naam": "Sam", "stad": "Utrecht"}

Een sleutel komt maar één keer voor in een dict. Het type noemt eerst het type
van de sleutels en daarna het type van de waarden: `dict[str, int]` heeft
strings als sleutel en gehele getallen als waarde.

Ook dicts vergelijk je in de tests met `==`.

```python
def make_dict() -> dict[str, int]:
    """
    >>> make_dict() == {"a": 1, "b": 2}
    True
    """
    return ...
```

{% next "Verder: een waarde opvragen" %}

Met blokhaken vraag je de waarde bij een sleutel op: `d["b"]`. Bestaat de
sleutel niet, dan krijg je een `KeyError`.

```python
def get_value(d: dict[str, int], key: str) -> int:
    """
    >>> get_value({"x": 10, "y": 20}, "y")
    20
    >>> get_value({"x": 10, "y": 20}, "x")
    10
    """
    return ...
```

{% next "Verder: een waarde instellen" %}

Met een toewijzing voeg je een paar toe, of verander je de waarde van een
sleutel die er al is:

    d["c"] = 3

Net als bij lists en sets verandert de dict zelf, dus de functie geeft niets
terug.

```python
def set_value(d: dict[str, int], key: str, value: int) -> None:
    """
    >>> d = {"a": 1}
    >>> set_value(d, "b", 2)
    >>> d == {"a": 1, "b": 2}
    True
    >>> set_value(d, "a", 9)
    >>> d == {"a": 9, "b": 2}
    True
    """
    ...
```

{% next "Verder: controleren of een sleutel bestaat" %}

Met `in` kijk je of een sleutel in een dict staat. Het gaat dus om de sleutels,
niet om de waarden.

```python
def has_key(d: dict[str, int], key: str) -> bool:
    """
    >>> has_key({"a": 1, "b": 2}, "b")
    True
    >>> has_key({"a": 1, "b": 2}, "z")
    False
    """
    return ...
```

{% next "Verder: een standaardwaarde" %}

Soms weet je niet zeker of een sleutel bestaat. Met `d.get(key, 0)` vraag je de
waarde op, en als de sleutel ontbreekt krijg je in plaats daarvan de tweede
waarde (hier 0). Er komt dan geen fout.

```python
def get_or_zero(d: dict[str, int], key: str) -> int:
    """
    >>> get_or_zero({"a": 5}, "a")
    5
    >>> get_or_zero({"a": 5}, "b")
    0
    """
    return ...
```

{% next "Verder: een dict doorlopen" %}

Een dict loop je door met een `for`-loop. Dat levert de sleutels. Daarnaast
heb je drie methoden:

- `d.keys()` geeft alle sleutels,
- `d.values()` geeft alle waarden,
- `d.items()` geeft elk paar als tuple `(sleutel, waarde)`. Die pak je meteen
  uit: `for key, value in d.items():`.

Tel alle waarden in de dict bij elkaar op.

```python
def total_value(d: dict[str, int]) -> int:
    """
    >>> total_value({"x": 10, "y": 20})
    30
    >>> total_value({})
    0
    """
    ...
```

{% next "Verder: combineren" %}

## 4. Combineren

Nu combineer je wat je weet. Tel hoe vaak elke letter in een string voorkomt.
Het resultaat is een dict met de letters als sleutel en de aantallen als waarde.

Loop over de string. Zit de letter al in de dict, dan tel je er 1 bij op.
Anders begin je bij 1. Met `get` hoef je die twee gevallen niet apart te
behandelen.

```python
def count_letters(s: str) -> dict[str, int]:
    """
    >>> count_letters("aab") == {"a": 2, "b": 1}
    True
    >>> count_letters("") == {}
    True
    """
    ...
```

{% next "Verder: omkeren" %}

Maak een nieuwe dict waarin sleutels en waarden zijn omgewisseld. Ga ervan uit
dat elke waarde maar één keer voorkomt.

```python
def invert_dict(d: dict[str, int]) -> dict[int, str]:
    """
    >>> invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    True
    >>> invert_dict({}) == {}
    True
    """
    ...
```

{% next "Afronden" %}

## Klaar

Klik nog één keer op **doctest** en daarna op **typecheck**. Als er staat dat
alle tests slagen en er geen fouten zijn, ben je klaar met de tutorial.

Slaagt er nog iets niet, dan noemt de uitvoer de functie, de aanroep die
geprobeerd is, wat eruit had moeten komen en wat eruit kwam. Verbeter die ene
functie en klik opnieuw.
