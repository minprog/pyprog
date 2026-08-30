# Tutorial: strings

Strings zijn reeksen tekens. In deze tutorial bouw je stap voor stap een aantal
kleine functies die met strings werken.

**Hoe het werkt.** Elke pagina hieronder laat één functie zien. Kopieer die naar
`tutorial_strings.py` in de editor en vervang de `...` door je eigen code. Klik
op de knop **doctest** om alle functies te controleren die je tot dan toe
geschreven hebt. De regels met `>>>` in elke functie zijn de tests: ze laten een
aanroep zien en het antwoord dat eruit moet komen.

Je bestand begint bijna leeg. Dat klopt — je vult het zelf.

Werk de pagina's op volgorde door; elke pagina bouwt voort op de vorige.

{% next "Beginnen" %}

## 1. Strings maken en teruggeven

Een string schrijf je als tekens tussen aanhalingstekens. Enkele en dubbele
aanhalingstekens werken allebei, en de lege string `''` is net zo goed een
string.

```python
def greet() -> str:
    """
    >>> greet()
    'Hello'
    """
    return ...
```

{% next "Verder: indexeren" %}

## 2. Indexeren

Elk teken heeft een positie, de index, en je telt vanaf 0:

```
 P  y  t  h  o  n
 0  1  2  3  4  5
```

`s[0]` is dus het eerste teken en `s[1]` het tweede.

```python
def first_char(s: str) -> str:
    """
    >>> first_char("Python")
    'P'
    >>> first_char("abc")
    'a'
    """
    return ...
```

{% next "Verder: achteruit tellen" %}

Negatieve indexen tellen vanaf het eind: `s[-1]` is het laatste teken, `s[-2]`
het teken daarvoor.

```python
def last_char(s: str) -> str:
    """
    >>> last_char("Python")
    'n'
    >>> last_char("code")
    'e'
    """
    ...
```

{% next "Verder: strings combineren" %}

## 3. Strings combineren en herhalen

Je kunt rekenen met strings. `+` plakt twee strings aan elkaar, `*` herhaalt er
een:

    'Hi' + '!'  ->  'Hi!'
    'Go' * 3    ->  'GoGoGo'

```python
def excited(word: str) -> str:
    """
    >>> excited("Hi")
    'Hi!!!'
    >>> excited("You")
    'You!!!'
    """
    ...
```

{% next "Verder: allebei tegelijk" %}

Plakken en herhalen kun je vrij combineren. Onderstaande functie krijgt string `a` en `b` en moet er iets mee doen. Lees de test goed om te bedenken wat deze functie moet geven.

```python
def double_and_space(a: str, b: str) -> str:
    """
    >>> double_and_space("go", "team")
    'gogo teamteam'
    """
    ...
```

{% next "Verder: zoeken" %}

## 4. Controleren en zoeken

Met `in` controleer je of de ene string in de andere voorkomt:

    'a' in 'dog'    ->  False
    'o' in 'dog'    ->  True
    'dog' in 'dog'  ->  True

Hier controleer je of de gegeven string deel uitmaakt van het woord `'python'`.

```python
def part_of_python(x: str) -> bool:
    """
    >>> part_of_python('py')
    True
    >>> part_of_python('n')
    True
    >>> part_of_python('java')
    False
    """
    ...
```

{% next "Verder: zoeken met een loop" %}

Je kunt de tekens ook zelf een voor een langslopen:

    for char in s:
        if char == ...:
            return True
    return False

Zodra je vindt wat je zoekt, geef je meteen `True` terug. Is de loop klaar zonder
dat er iets teruggegeven is, dan zat het er niet in en geef je `False` terug.

Schrijf zo'n loop die `True` teruggeeft als de letter o in `x` zit, en anders
`False`.

```python
def has_o(x: str) -> bool:
    """
    >>> has_o("dog")
    True
    >>> has_o("cat")
    False
    """
    ...
```

{% next "Verder: andersom" %}

Met een vergelijkbare loop controleer je of iets er juist *niet* in zit: `True`
als de letter o NIET in `x` zit. Begin bij de loop die je net geschreven hebt en
bedenk welk antwoord waar hoort.

```python
def has_no_o(x: str) -> bool:
    """
    >>> has_no_o("cat")
    True
    >>> has_no_o("dog")
    False
    """
    ...
```

{% next "Verder: een positie vinden" %}

Loop je over de indexen in plaats van over de tekens, dan kun je vertellen *waar*
iets staat:

    for index in range(len(s)):
        if s[index] == ...:
            return index

`-1` teruggeven is de gebruikelijke manier om te zeggen "niet gevonden". Geef
hier dus de positie van de eerste letter o terug, of anders `-1`.

```python
def where_o_at(text: str) -> int:
    """
    >>> where_o_at("Python")
    4
    >>> where_o_at("abc")
    -1
    """
    ...
```

{% next "Verder: hoofd- en kleine letters" %}

## 5. Hoofd- en kleine letters

`upper()` geeft een kopie van de string in hoofdletters, `lower()` een in kleine
letters:

    'boe'.upper()       ->  'BOE'
    'Universum'.lower() ->  'universum'

Lees de test heel goed — er wordt net iets meer gevraagd dan alleen de letters
omzetten.

```python
def shout(s: str) -> str:
    """
    >>> shout("hello")
    'HELLO!'
    """
    ...
```

{% next "Verder: zachtjes" %}

Zelfde idee, andere kant op. Lees ook hier de test goed.

```python
def quiet(s: str) -> str:
    """
    >>> quiet("LOUD")
    'loud...'
    """
    ...
```

{% next "Verder: tellen" %}

## 6. Tekens langslopen

Om iets in een string te tellen houd je een teller bij die je ophoogt zodra je
tegenkomt waar je naar zoekt:

    aantal = 0
    voor elk teken in de string:
        als het is wat we zoeken:
            verhoog aantal

Hier tel je de klinkers a, e, i, o en u. Twee hints: met `in` kun je controleren
of een teken een van meerdere tekens is, en de laatste test staat in
hoofdletters.

```python
def count_vowels(s: str) -> int:
    """
    >>> count_vowels("education")
    5
    >>> count_vowels("Python")
    1
    >>> count_vowels("RODENT!")
    2
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
