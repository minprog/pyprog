# Tutorial: een queue bouwen

Een **queue** (wachtrij) bewaart waarden die je later weer ophaalt, in de
volgorde waarin je ze hebt neergezet. Wie het eerst in de queue komt, komt er
ook het eerst uit. Dit heet *first in, first out* (FIFO).

Een queue ondersteunt twee hoofdhandelingen:

- **enqueue** zet een waarde achteraan de queue,
- **dequeue** haalt de waarde voorin de queue weg en geeft die terug.

```
 enqueue                                       dequeue
    |                                             |
    v      achter                      voor       v
   ---->  [ 5 ][ 8 ][ 2 ][ 7 ]  ---->
```

Je kent dit uit het dagelijks leven: de eerste klant in de rij wordt ook het
eerst geholpen. Computers gebruiken het onder andere om taken af te handelen.
De lijst met openstaande taken is een queue, zodat de oudste taak altijd als
eerste aan de beurt komt.

In deze tutorial schrijf je een klasse `Queue`. Het gaat hierbij vooral om het
**ontwerp** van een klasse: je bepaalt eerst hoe iemand de klasse gebruikt, en
daarna hoe hij van binnen werkt.

**Hoe het werkt.** Bij elke stap krijg je een methode van de klasse. Kopieer
die naar de klasse `Queue` in `my_queue.py` in de editor en vervang de `...`
door je eigen code. Klik op de knop **doctest** om alle methoden te
controleren die je schrijft. Als alle doctests goed zijn, klik dan op
**typecheck** om te controleren of je types kloppen.

Werk de pagina's op volgorde door; elke pagina bouwt voort op de vorige.

{% next "Beginnen" %}

## 1. Eerst de interface

De **interface** van een klasse is de lijst met methoden die je van buitenaf
mag gebruiken. Bij een queue zijn dat `enqueue` en `dequeue`. Zo gebruik je de
klasse straks:

    q = Queue()           # maak een nieuwe, lege queue
    q.enqueue(3)          # zet het getal 3 achteraan
    q.enqueue(1)          # zet het getal 1 achteraan
    print(q.dequeue())    # geeft het eerste getal terug: 3

Het bestand `my_queue.py` begint al met `from typing import Any`. Daarmee mag
je het type `Any` gebruiken, dat staat voor elk soort waarde. In onze queue
mag je dus alles zetten: getallen, strings, of iets anders.

Zet onder de `import` deze klasse in het bestand. De methoden doen nog niets:
ze hebben alleen een naam, parameters en een type.

```python
class Queue:

    def enqueue(self, element: Any) -> None:
        ...

    def dequeue(self) -> Any:
        ...
```

{% next "Verder: opslag" %}

## 2. De opslag

Een queue is van binnen een list, maar je laat maar twee handelingen toe. Elk
Queue-object krijgt zijn eigen, **interne** list. Die maak je aan in de
initializer, de methode `__init__`, want die wordt uitgevoerd zodra je
`Queue()` aanroept:

    def __init__(self) -> None:
        self._data: list[Any] = []

Dit maakt een lege list en bewaart die in het object onder de naam `_data`.
Zo'n naam bereik je alleen met `self`, dus binnen de methoden van de klasse.

Een naam die met een underscore (`_`) begint, is een afspraak onder
programmeurs: dit hoort bij de binnenkant van de klasse en je schrijft er geen
code buiten de klasse voor. Python dwingt dit niet af.

Zet deze methode als eerste in je klasse, boven `enqueue`.

```python
class Queue:

    def __init__(self) -> None:
        """
        >>> q = Queue()
        >>> q._data
        []
        """
        self._data: list[Any] = []
```

{% next "Verder: enqueue" %}

## 3. Enqueue

Een waarde die je in de queue zet, komt achteraan. Je list heeft een methode
om iets achteraan toe te voegen: `append`.

Schrijf `enqueue`. In deze test kijken we eenmalig in `_data`, omdat we nog geen
andere manier hebben om de inhoud te zien.

```python
    def enqueue(self, element: Any) -> None:
        """
        >>> q = Queue()
        >>> q.enqueue(3)
        >>> q.enqueue(1)
        >>> q._data
        [3, 1]
        """
        ...
```

{% next "Verder: dequeue" %}

## 4. Dequeue

Elementen komen achteraan de list binnen, dus de oudste waarde staat voorin.
`dequeue` moet die waarde uit de queue halen **en teruggeven**. Verwijderen
zonder terug te geven is nutteloos, want dan kom je de waarde nooit te weten.

De methode `pop` haalt een element uit een list en geeft het terug. Zonder
argument haalt `pop()` het laatste element weg. Met een index, `pop(0)`, haal
je het eerste element weg.

```python
    def dequeue(self) -> Any:
        """
        >>> q = Queue()
        >>> q.enqueue(3)
        >>> q.enqueue(1)
        >>> q.dequeue()
        3
        >>> q.dequeue()
        1
        """
        ...
```

Je ziet dat de volgorde klopt: de 3 ging als eerste erin en komt als eerste
eruit.

{% next "Verder: meer methoden" %}

## 5. Meer methoden

Naast `enqueue` en `dequeue` zijn nog drie handelingen handig. Schrijf ze als
volgende methoden van de klasse. Let op de spelling van `peek`.

`size` geeft het aantal elementen in de queue.

```python
    def size(self) -> int:
        """
        >>> q = Queue()
        >>> q.size()
        0
        >>> q.enqueue("a")
        >>> q.enqueue("b")
        >>> q.size()
        2
        """
        ...
```

{% next "Verder: peek" %}

`peek` geeft het element voorin de queue terug, maar haalt het niet weg. Je
kijkt dus alleen wie er aan de beurt is.

```python
    def peek(self) -> Any:
        """
        >>> q = Queue()
        >>> q.enqueue("a")
        >>> q.enqueue("b")
        >>> q.peek()
        'a'
        >>> q.size()
        2
        """
        ...
```

{% next "Verder: leegmaken" %}

`empty` maakt de queue leeg: alle elementen gaan weg. Zo'n methode geeft
niets terug.

```python
    def empty(self) -> None:
        """
        >>> q = Queue()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.empty()
        >>> q.size()
        0
        """
        ...
```

{% next "Verder: fouten opsporen" %}

## 6. Een fout vroeg zien

Wat gebeurt er als je `dequeue` aanroept terwijl de queue leeg is? Dan probeert
Python een element uit een lege list te halen, en dat geeft een foutmelding die
niets over queues zegt.

Met een **assertion** zorg je dat zo'n fout meteen duidelijk is. Een `assert`
controleert een voorwaarde. Is de voorwaarde niet waar, dan stopt het programma
met een `AssertionError` op die regel:

    assert self.size() > 0

Zet deze regel bovenaan `dequeue`. Als je dan toch uit een lege queue haalt,
weet je direct waar het misgaat.

Een assertion helpt jou, de programmeur, bij het vinden van fouten in je eigen
code. Voor een gebruiker van een programma zegt een `AssertionError` weinig.

Ook dit kun je in een doctest testen. Zet deze test onderaan de docstring van
`dequeue`. De regel met `...` staat er letterlijk; die laat doctest een lang
verhaal overslaan.

```python
        """
        >>> q = Queue()
        >>> q.dequeue()
        Traceback (most recent call last):
        ...
        AssertionError
        """
```

{% next "Afronden" %}

## Klaar

Klik nog één keer op **doctest** en daarna op **typecheck**. Als er staat dat
alle tests slagen en er geen fouten zijn, ben je klaar met de tutorial.

Slaagt er nog iets niet, dan noemt de uitvoer de methode, de aanroep die
geprobeerd is, wat eruit had moeten komen en wat eruit kwam. Verbeter die ene
methode en klik opnieuw.

## Wat heb je gebouwd?

Je queue kan minder dan een gewone list. Je kunt bijvoorbeeld niet het tweede
element bekijken zonder het eerste weg te halen, en je kunt niets achteraan
weghalen. Waarom zou je dan een queue gebruiken? Twee ideeën uit het ontwerpen
van klassen spelen hier mee:

1. De klasse heeft een **eenvoudige interface** voor één taak. Wie code leest
   waarin `enqueue` en `dequeue` voorkomen, snapt meteen wat er gebeurt.

2. De klasse **verbergt hoe ze werkt**. Wij gebruiken een list als opslag, maar
   wie de klasse gebruikt, merkt dat niet. Je kunt de binnenkant later
   veranderen en de code die de queue gebruikt blijft werken, omdat de
   interface hetzelfde blijft.

Een bekende verwante structuur is de **stack**. Daarbij haal je juist het laatst
toegevoegde element er als eerste uit. Probeer zelf eens een `Stack` te
schrijven met dezelfde aanpak.
