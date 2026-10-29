# Tutorial: strings transformeren

In deze tutorial schrijf je functies die een nieuwe string maken op basis van
een gegeven string. Soms verander je tekens, soms laat je tekens weg.

**Hoe het werkt.** Bij elke stap krijg je de code voor één functie.
Kopieer die naar de editor hiernaast en vervang de `...` door je eigen code.
Klik op de knop **doctest** om alle functies te controleren die je schrijft.
Als alle doctests goed zijn, klik dan op **typecheck** om te zorgen dat je types goed zijn.

Werk de pagina's op volgorde door, want elke pagina bouwt voort op de vorige.

{% next "Beginnen" %}

## 1. Een string kopiëren

Een string kun je niet zomaar aanpassen. Je kunt niet één teken in een string
vervangen of weghalen. Wat je wel kunt doen is een nieuwe string opbouwen,
teken voor teken. Dat is dus eigenlijk een **kopie**.

    nieuwe_string = ""
    for teken in s:
        nieuwe_string += teken

Je begint met een lege string en plakt er in de loop steeds één teken achter.
Zo'n string die wordt opgebouwd noem je ook wel een *accumulator*.

Schrijf met dit patroon een functie die een precieze kopie van `s` teruggeeft.
Dat lijkt nutteloos, maar alle andere functies in deze tutorial beginnen met
precies deze loop.

```python
def kopie(s: str) -> str:
    """
    >>> kopie("hallo")
    'hallo'
    >>> kopie("")
    ''
    """
    ...
```

{% next "Verder: elk teken veranderen" %}

## 2. Elk teken veranderen

In plaats van `teken` kun je ook iets anders achter de nieuwe string plakken.
Bijvoorbeeld `teken.upper()`, de hoofdletterversie van het teken.

Schrijf een functie die `s` teken voor teken omzet naar hoofdletters. Gebruik
dus een loop, en niet `s.upper()` op de hele string.

```python
def hoofdletters(s: str) -> str:
    """
    >>> hoofdletters("hallo")
    'HALLO'
    >>> hoofdletters("Dag 3!")
    'DAG 3!'
    """
    ...
```

{% next "Verder: kiezen per teken" %}

## 3. Kiezen per teken

Meestal wil je niet elk teken veranderen, maar alleen sommige. Dan kies je per
teken wat je achter de nieuwe string plakt:

    nieuwe_string = ""
    for teken in s:
        if ...:
            nieuwe_string += ...
        else:
            nieuwe_string += teken

In de `if` doe je de gewenste wijziging, en in de `else` houd je juist het originele teken.

Schrijf een functie die elke spatie vervangt door een liggend streepje `_`.
Alle andere tekens blijven hetzelfde.

```python
def spaties_naar_streepjes(s: str) -> str:
    """
    >>> spaties_naar_streepjes("hallo daar")
    'hallo_daar'
    >>> spaties_naar_streepjes("een twee drie")
    'een_twee_drie'
    """
    ...
```

{% next "Verder: meerdere tekens tegelijk" %}

## 4. Meerdere tekens tegelijk

Met `in` controleer je of een teken voorkomt in een string. De standaardmanier is bijvoorbeeld:

    "a" in mijn_string

Maar andersom kan ook. Je hebt één enkel teken en je kunt checken of het een klinker is:

    teken in "aeiou"

Dit is `True` als `teken` een van de klinkers is.

Schrijf een functie die elke klinker vervangt door een `*`. Let op: de tweede
test bevat ook hoofdletters.

```python
def verberg_klinkers(s: str) -> str:
    """
    >>> verberg_klinkers("python")
    'pyth*n'
    >>> verberg_klinkers("Amsterdam")
    '*mst*rd*m'
    """
    ...
```

{% next "Verder: meer dan twee keuzes" %}

Met `if`/`else` kies je uit twee uitkomsten. Heb je er meer nodig, dan zet je
er `elif`-checks tussen:

    if teken in "aA":
        nieuwe_string += "4"
    elif teken in "eE":
        nieuwe_string += "3"
    ...
    else:
        nieuwe_string += teken

Python controleert de voorwaarden van boven naar beneden en voert alleen de
eerste optie uit die klopt. Je kunt zoiets "matching" noemen: de eerste match telt.

Schrijf nu een functie die een string omzet naar "leetspeak". Een `a` of `A`
wordt een `4`, `e/E` wordt `3`, `l/L` wordt `1`, `o/O` wordt `0` en `t/T` wordt
`7`. Alle andere tekens blijven zoals ze zijn.

```python
def l337sp34k(s: str) -> str:
    """
    >>> l337sp34k("leet")
    '1337'
    >>> l337sp34k("Hallo Toto!")
    'H4110 7070!'
    """
    ...
```

{% next "Verder: letters en cijfers" %}

## 5. Letters en cijfers herkennen

Strings hebben methodes die iets vertellen over de tekens erin:

    'a'.isalpha()  ->  True    (is het een letter?)
    '7'.isalpha()  ->  False
    '7'.isdigit()  ->  True    (is het een cijfer?)
    ' '.isdigit()  ->  False

Schrijf een functie die elk cijfer vervangt door een `#`. Gebruik hiervoor `isdigit()` en dus niet `in`.

```python
def verberg_cijfers(s: str) -> str:
    """
    >>> verberg_cijfers("pincode 1234")
    'pincode ####'
    >>> verberg_cijfers("R2D2")
    'R#D#'
    """
    ...
```

{% next "Verder: blackout" %}

Schrijf een functie die elke letter
onleesbaar maakt door hem te vervangen door een `#`. Gebruik `isalpha()`. Alle
andere tekens dan letters blijven zoals ze zijn.

```python
def blackout(s: str) -> str:
    """
    >>> blackout("Geheim!")
    '######!'
    >>> blackout("R2D2 is 1 robot.")
    '#2#2 ## 1 #####.'
    """
    ...
```

{% next "Verder: het teken als parameter" %}

## 6. Het teken als parameter

Tot nu toe stond het teken waar je naar zoekt vast in je code. Je kunt het ook
meegeven als parameter. Dan kun je dezelfde functie voor verschillende tekens
gebruiken.

Schrijf een functie die elk
voorkomen van het teken `c1` vervangt door het teken `c2`. Gebruik een loop met
`if`, en niet de methode `replace()`.

```python
def replace_char(s: str, c1: str, c2: str) -> str:
    """
    >>> replace_char("banaan", "a", "o")
    'bonoon'
    >>> replace_char("hallo daar", " ", "_")
    'hallo_daar'
    """
    ...
```

{% next "Verder: tekens weglaten" %}

## 7. Tekens weglaten

Je kunt een teken ook overslaan bij het maken van de nieuwe string. Dat betekent
dat het "verwijderd wordt". Als je dat doet bij het maken van een kopie, wordt
nieuwe string wordt (mogelijk) korter dan de oude.

    nieuwe_string = ""
    for teken in s:
        if ...:
            nieuwe_string += teken
    return nieuwe_string

Alleen tekens waarvoor de `if` klopt komen in de nieuwe string. Je hebt dus niet per se een `else` nodig om te verwijderen! In plaats daarvan zorg je dat niet alles gekopieerd wordt.

Schrijf nu een functie die alle spaties weglaat uit een string.

```python
def zonder_spaties(s: str) -> str:
    """
    >>> zonder_spaties("hallo daar")
    'hallodaar'
    >>> zonder_spaties(" a b c ")
    'abc'
    """
    ...
```

{% next "Verder: letter n weglaten" %}

Schrijf een functie die alle letters `n` weglaat.

```python
def verwijder_n(s: str) -> str:
    """
    >>> verwijder_n("banaan")
    'baaa'
    >>> verwijder_n("nu niet")
    'u iet'
    """
    ...
```

{% next "Verder: loopen met posities" %}

## 8. Loopen met posities

Soms moet je bij een teken ook naar het teken ervoor of erna kijken. Dan loop je
niet over de tekens, maar over de posities:

    nieuwe_string = ""
    for pos in range(len(s)):
        nieuwe_string += s[pos]

`s[pos]` is het teken op positie `pos`. Deze loop doet precies hetzelfde als de
loop in `kopie`.

Schrijf `kopie` opnieuw, maar nu met een loop over posities.

```python
def kopie_met_posities(s: str) -> str:
    """
    >>> kopie_met_posities("hallo")
    'hallo'
    >>> kopie_met_posities("")
    ''
    """
    ...
```

{% next "Verder: vooruit kijken" %}

## 9. Vooruit kijken

Met `s[pos + 1]` bekijk je het teken **na** positie `pos`. Maar pas op: bij het
laatste teken is er geen volgend teken. Dan geeft `s[pos + 1]` een `IndexError`.

Het laatste teken staat op positie `len(s) - 1`. Controleer dat dus eerst:

    if pos == len(s) - 1 or s[pos + 1] == " ":

Python stopt met rekenen zodra de eerste helft van de `or` `True` is. Bij het
laatste teken wordt `s[pos + 1]` dus nooit bekeken.

Schrijf een functie die alleen de laatste letter van elk woord houdt. Een
letter is de laatste van een woord als hij aan het eind van de string staat, of
als er een spatie na komt.

```python
def laatste_letters(s: str) -> str:
    """
    >>> laatste_letters("hallo daar")
    'or'
    >>> laatste_letters("een twee drie")
    'nee'
    """
    ...
```

{% next "Verder: n aan het eind van een woord" %}

Schrijf een functie die alle
letters `n` weglaat, maar alleen als ze aan het eind van een woord staan.

Een `n` staat aan het eind van een woord als hij het laatste teken van de
string is, of als er geen letter na komt. Na een woord kan namelijk ook een
komma of punt staan. Gebruik daarom `not s[pos + 1].isalpha()` in plaats van
`s[pos + 1] == " "`.

Let op: je houdt nu elk teken, *behalve* een `n` aan het eind van een woord.

```python
def verwijder_n_eind(s: str) -> str:
    """
    >>> verwijder_n_eind("lopen en fietsen")
    'lope e fietse'
    >>> verwijder_n_eind("banaan, nu even.")
    'banaa, nu eve.'
    """
    ...
```

{% next "Verder: achteruit kijken" %}

## 10. Achteruit kijken

Met `s[pos - 1]` bekijk je het teken **voor** positie `pos`. Bij het eerste
teken is er geen vorig teken. Python geeft dan geen foutmelding, want `s[-1]`
is het laatste teken van de string. Maar dat is niet wat je wilt! Controleer
dus eerst of `pos == 0`.

Schrijf een functie die alleen de eerste letter van elk woord houdt. Een letter
is de eerste van een woord als hij aan het begin van de string staat, of als er
een spatie voor staat.

```python
def eerste_letters(s: str) -> str:
    """
    >>> eerste_letters("hallo daar")
    'hd'
    >>> eerste_letters("een twee drie")
    'etd'
    """
    ...
```

{% next "Verder: n aan het begin van een woord" %}

Schrijf een functie die alle
letters `n` weglaat, maar alleen als ze aan het begin van een woord staan.

Een `n` staat aan het begin van een woord als hij het eerste teken van de
string is, of als er geen letter voor staat.

```python
def verwijder_n_begin(s: str) -> str:
    """
    >>> verwijder_n_begin("nu niet")
    'u iet'
    >>> verwijder_n_begin("banaan,nee")
    'banaan,ee'
    """
    ...
```

{% next "Verder: stretch" %}

## 11. Stretch

Schrijf een functie `stretch` die de tekens uit een string vermeerdert. Elk teken wordt steeds met ééntje extra vermeerderd.

Gebruik een normale transformatie-loop (`for char in s:`) maar voeg een teller toe om bij te houden hoe ver je bent.

```python
def stretch(s: str) -> str:
    """
    >>> stretch('abc')
    'abbccc'
    >>> stretch('Hoi!')
    'Hooiii!!!!'
    """
    ...
```

{% next "Verder: autocorrect" %}

## 12. Autocorrect

Schrijf een functie `autocorrect` die dubbele leestekens en spaties verwijdert uit een string. Alleen gewone letters en cijfers (te herkennen met `c.isalnum()`) worden met rust gelaten.

Gebruik een normale transformatie-loop (`for char in s:`) maar check altijd, vóórdat je een teken toevoegt aan het resultaat, of dat teken niet toevallig al aan het eind van het resultaat staat.

```python
def autocorrect(s: str) -> str:
    """
    >>> autocorrect('---')
    '-'
    >>> autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')
    'Dit hier, dit kan niet de bedoeling zijn.'
    """
    ...
```

{% next "Verder: om de letter uppercase 1" %}

## 13. Om de letter uppercase 1

Schrijf een functie `spongebob1` die elk tweede teken in een string naar uppercase omzet. Je mag de methode `.upper()` gebruiken om één letter naar uppercase te converteren.

Voor deze functie moet je een positie-loop maken zodat je weer "waar je bent" in de string (`for i in range(len(s))`). Alle oneven posities worden uppercase.

```python
def spongebob1(s: str) -> str:
    """
    >>> spongebob1('hello world!')
    'hElLo wOrLd!'
    """
    ...
```

{% next "Verder: om de letter uppercase 2" %}

## 14. Om de letter uppercase 2

Schrijf een functie `spongebob2` die elke tweede letter in een string naar uppercase omzet. Je mag de methode `.upper()` gebruiken om één letter naar uppercase te converteren.

Hier is een extra beperking, namelijk dat het echt alleen om *letters* gaat. Je moet met de methode `.isalpha()` checken of een teken alfabetisch is en alleen dan telt deze als letter.

In dit geval geeft een positie-loop geen nuttige informatie, want niet elke positie bevat een letter. Je maakt nu dus weer een normale transformatie-loop (`for char in s:`).

Algoritme:

- Loop door alle tekens in de invoerstring met een transformatie-loop.
    - Houd een teller bij voor hoeveel letters je tot nu toe hebt gezien.
        - Als char een letter is (`char.isalpha()`), dan verhoog je de teller.
        - Als de teller een even getal is (2, 4, 6, …), dan maak je deze letter uppercase.
        - Anders laat je de letter zoals hij is.
    - Voeg het teken daarna toe aan de resultaatstring.

```python
def spongebob2(s: str) -> str:
    """
    >>> spongebob2('hello world!')
    'hElLo WoRlD!'
    """
    ...
```

{% next "Afronden" %}

## Klaar

Klik nog één keer op **doctest** en **typecheck**.
Als er staat dat alle tests slagen, en er geen problemen met types zijn,
dan ben je klaar met de tutorial.

Slaagt er nog iets niet, verbeter dan je code en vraag om hulp als je er niet uitkomt.
