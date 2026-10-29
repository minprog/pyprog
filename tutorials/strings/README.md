# Tutorial: strings

Strings zijn reeksen tekens. In deze tutorial bouw je stap voor stap een aantal
kleine functies die met strings werken.

**Hoe het werkt.** Bij elke stap krijg je de code voor één functie.
Kopieer die naar de editor hiernaast en vervang de `...` door je eigen code.
Klik op de knop **doctest** om alle functies te controleren die je schrijft.
Als alle doctests goed zijn, klik dan op **typecheck** te zorgen dat je types goed zijn.

Werk de pagina's op volgorde door, want elke pagina bouwt voort op de vorige.

{% next "Beginnen" %}

## 1. Strings maken en teruggeven

Een string schrijf je als tekens tussen aanhalingstekens. Enkele en dubbele
aanhalingstekens werken allebei, en de lege string `''` is net zo goed een
string.

Schrijf nu eerst een functie die een string teruggeeft.
Altijd dezelfde, zie de doctest die al geschreven is.


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

Elk teken in een string heeft een positie, de **index**, en je telt die vanaf 0:

```
 P  y  t  h  o  n
 0  1  2  3  4  5
```

`s[0]` is dus het eerste teken en `s[1]` het tweede.

Schrijf nu (met bovenstaande kennis) een functie die altijd het eerste teken van een string teruggeeft.

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

Python begrijpt ook **negatieve indexen**.
Die tellen vanaf het einde van de string:
`s[-1]` is het laatste teken, `s[-2]` het teken daarvoor.

Schrijf een functie die altijd het laatste teken van een string teruggeeft.

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

Gebruik dit om een functie te schrijven die een superexcited versie van die string teruggeeft. Gebruik zowel plakken als herhalen!!!

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

Plakken en herhalen kun je vrij combineren. Onderstaande functie krijgt de strings `a` en `b` en moet er dan iets mee doen. Lees de doctest goed om te bedenken wat deze functie moet teruggeven.

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

Schrijf een functie die controleert of de gegeven string (`x`) *onderdeel is* van de van het woord `'python'`.

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

Je kunt de tekens ook zelf een voor een langslopen, bijvoorbeeld om de letters van de string te **doorzoeken**:

    for char in s:
        if char == ...:
            return True
    return False

Zodra je vindt wat je zoekt, geef je meteen `True` terug. Is de loop klaar zonder
dat er iets teruggegeven is, dan zat het er niet in en geef je `False` terug.

Schrijf een functie met zo'n loop die `True` teruggeeft als de letter o in `x` zit, en anders
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
als de letter `'o'` NIET in `x` zit.
Begin bij de loop die je net geschreven hebt en bedenk hoe je het moet omgooien om het juiste resultaat te krijgen.

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

Je kunt niet alleen loopen met de letters in een string, maar ook met de index.
Dan kun je bijhouden en vertellen *waar* iets staat:

    for index in range(len(s)):
        if s[index] == ...:
            return index

Schrijf een functie die bepaalt waar de (eerste) `o` in een string gevonden kan worden, dus op welke index.
`-1` teruggeven is de gebruikelijke manier om te zeggen "niet gevonden". Doe dat als de `o` helemaal niet vindbaar blijkt.

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

Gebruik dit om een functie te schrijven. Lees de doctest om te bepalen wat de functie moet doen. (Net iets meer dan alleen omzetten.)

```python
def shout(s: str) -> str:
    """
    >>> shout("hello")
    'HELLO!'
    """
    ...
```

{% next "Verder: de zachte versie" %}

Zelfde idee, maar dan andersom. Lees weer de doctest en implementeer de functie.

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

Schrijf een functie die telt hoeveel klinkers er in een string zitten (a, e, i, o en u).
Twee hints: met `in` kun je controleren of één teken uit de string een klinker is, en de laatste test staat in hoofdletters maar moet ook gewoon klinkers tellen.

Deze is dus meer denkwerk dan de vorige functies.

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

{% next "Verder: spacing" %}

## 7. Spacing

Schrijf een functie `isspace` die een string `s` aanneemt met daarin één teken en bepaalt of deze string "witruimte" is. Een teken is witruimte als het één van de volgende tekens is:

- [spatie](https://en.wikipedia.org/wiki/Space_(punctuation)) (dit teken schrijf je als `" "`)
- [tab](https://en.wikipedia.org/wiki/Tab_key) (dit teken schrijf je als `"\t"`)
- [newline](https://en.wikipedia.org/wiki/Newline) (dit teken schrijf je als `"\n"`)

Je kunt deze tekens opnemen in je code zoals hierboven geschreven. Misschien goed om even uit te leggen: sommige speciale tekens kun je opnemen in een string door middel van een backslash `\` en dan bijvoorbeeld een letter. Een `\n` is bijvoorbeeld nodig omdat je niet zomaar een Enter midden in een string in je code kunt tikken.

De functie kan uit één regel bestaan:

    def isspace(c: str) -> bool:
        return <hier de formule of c witruimte is>

- Wat moet de functie doen als de gegeven string meer dan één teken bevat? Dat is niet gedefinieerd in deze opgave. Je mag dit negeren.

```python
def isspace(c: str) -> bool:
    """
    >>> isspace(" ")
    True
    >>> isspace("\t")
    True
    >>> isspace("\n")
    True
    >>> isspace("a")
    False
    """
    ...
```

{% next "Verder: klinker-check" %}

## 8. Klinker-check

Schrijf een functie `isvowel` die een string `s` aanneemt met daarin één *of meer* tekens en bepaalt of alle tekens in deze string klinkers zijn. Als klinkers beschouwen we: `a`, `e`, `i`, `o` en `u`.

Je moet dus checken of <u>alle</u> tekens klinkers zijn. De logica gebiedt dat als je ook maar één teken tegenkomt dat <u>geen</u> klinker is, je direct `False` mag returnen. Het ziet er dan zo uit:

    for char in s:
        if ...:
            return False
    return True

- Dus in de loop zie je dat, op een bepaalde voorwaarde, direct `return False` wordt gedaan.
- Wat moet de functie doen als de gegeven string leeg is? `True` returnen (dit is makkelijker). Check dit gewenste resultaat in een extra doctest.

```python
def isvowel(s: str) -> bool:
    """
    >>> isvowel("a")
    True
    >>> isvowel("slim")
    False
    >>> isvowel("")
    True
    """
    ...
```

{% next "Verder: eén klinker" %}

## 9. Eén klinker

Schrijf een functie `has_single_vowel` die een string `s` aanneemt. De functie checkt of er minimaal en maximaal één klinker in voorkomt. Je moet dus alle tekens afgaan en een teller bijhouden. Om te checken of één teken een klinker is gebruik je de eerder gemaakte functie `isvowel`.

    aantal_klinkers = 0
    for char in s:
        if ...:
            aantal_klinkers += 1

    <hier code om een conclusie te trekken op basis van aantal_klinkers>

```python
def has_single_vowel(s: str) -> bool:
    """
    >>> has_single_vowel("bims")
    True
    >>> has_single_vowel("yolo")
    False
    >>> has_single_vowel("")
    False
    """
    ...
```

{% next "Verder: verschillend?" %}

## 10. Verschillend?

Schrijf een functie `is_different` die twee strings `s1` en `s2` aanneemt en bepaalt of deze strings verschillen.

Hiervoor ga je loopen met indexes, van 0 tot het einde van de strings. Je bekijkt steeds *hetzelfde* teken van beide strings (bijv. op index 1). Als de strings op één plek verschillen, dan weet je dat de strings verschillen, en kan de functie direct `return True` doen. Als ze niet verschillen op die plek, dan weet je nog niks. Je gaat dan door naar de volgende.

Hints:

- Schrijf het eerst zodat het werkt als je strings van gelijke lengte ("abc" en "def") geeft.
- Denk daarna hoe je het gaat afhandelen als de strings van verschillende lengte zijn en verwerk dit in de code.

```python
def is_different(s1: str, s2: str) -> bool:
    """
    >>> is_different("dance", "night")
    True
    >>> is_different("dance", "dance")
    False
    >>> is_different("piano", "pianissimo")
    True
    >>> is_different("", "")
    False
    """
    ...
```

{% next "Verder: hoe verschillend?" %}

## 11. Hoe verschillend?

Schrijf een functie `count_difference` die twee strings `s1` en `s2` aanneemt en bepaalt hoeveel verschillen de strings hebben.

We gebruiken een vereenvoudigd algoritme. Als de strings verschillen van lengte dan berekenen we dat verschil en dat is de basis. Dan vergelijken we zoveel mogelijk de tekens per positie, zoals bij de vorige functie. Voor elke positie waar de tekens verschillen tel je één op bij de basis.

```python
def count_difference(s1: str, s2: str) -> int:
    """
    >>> count_difference("dance", "night")
    5
    >>> count_difference("dance", "dance")
    0
    >>> count_difference("piano", "pianissimo")
    6
    >>> count_difference("", "mamba")
    5
    """
    ...
```

{% next "Afronden" %}

## Klaar

Klik nog één keer op **doctest** en **typecheck**.
Als er staat dat alle tests slagen, en er geen problemen met types zijn,
dan ben je klaar met de tutorial.

Slaagt er nog iets niet, verbeter dan je code en vraag om hulp als je er niet uitkomt.
