# Lecture: Object-oriented programming

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_3m9duva2&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_0fj1ulvm)


## Voorgeschiedenis

Objectgeoriënteerd programmeren begint bij **Sketchpad**, een programma om figuren op het scherm te tekenen. Nu nemen we dat redelijk voor lief, maar in 1963 was dat helemaal nieuw. Er kon met een "lichtpen" direct op het scherm getekend worden. Figuren bestonden uit lijnen en hoekpunten die automatisch met elkaar verbonden werden.

De programmeertaal **Simula** is de andere kant van het verhaal. Dat is de eerste programmeertaal waarin je "klassen" en eigenschappen van objecten kon beschrijven. Daarmee kon je dan kortere programma's schrijven voor programmeerproblemen waarin veel objecten een rol speelden.

Beide ideeën komen jaren later terug in **Omnigraffle**, een programma om diagrammen te maken met figuren, teksten en andere objecten. In dit programma zijn de figuren objecten op het scherm, en elk object heeft allerlei eigenschappen: breedte, hoogte, en coördinaten. Zo zijn er twee rechthoeken waarvoor de breedte en hoogte hetzelfde zijn, maar de coördinaten verschillen. En er is een cirkel die dezelfde breedte en hoogte heeft, maar andere coördinaten.

## Objecten en classes

-   Een programma als OmniGraffle moet op de achtergrond een definitie van alle figuren in het geheugen hebben. Elke definitie bestaat uit "wat voor object is dit" en een aantal eigenschappen die zijn ingesteld. Het programma heeft vervolgens als hoofdtaak om deze abstracte beschrijvingen (getallen) te gebruiken om figuren op het scherm te tekenen en manipulatie mogelijk te maken.

    ![](objects.png)

    In het diagram hierboven zie je steeds dan naam van het object, met daaronder een lijstje **eigenschappen** met concrete waardes erbij. Dit is de essentiële informatie die in het geheugen opgeslagen staat als het programma gebruikt wordt.

-   Wat we nu nog moeten doen is deze objecten onderscheiden in "classes". Dat is nodig omdat bijvoorbeeld een "rechthoek" op een heel andere manier wordt getekend dan een cirkel---simpelweg omdat ze er anders uitzien. We zeggen dat `rectangle1` en `rectangle2` van het type `Rectangle` zijn, en `circle1` is van het type `Circle`. Zo zijn `Rectangle` en `Circle` de twee classes waar het hier om gaat.

-   Nu we niet alleen objecten hebben, maar ook twee "klassen" onderscheiden, kunnen we voor de klasse `Rectangle` beschrijven hoe een rechthoek getekend moet worden op basis van een hoogte en een breedte. En voor de klasse `Circle` beschrijven we hoe een ovaal getekend moet worden, wederom op basis van hoogte en breedte. Dit maakt ook het verschil tussen objecten en classes: per rechthoek-object slaan we op wat de afmetingen zijn, maar de procedure om een rechthoek te tekenen kunnen één keer beschrijven in de klasse.

-   Een klasse is een concept dat dus vooral bestaat in programmacode, de procedures om iets te doen. Daarnaast kunnen we in een klasse vastleggen *welke* eigenschappen een object van die klasse kan of moet hebben. Hier staat bijvoorbeeld dat een rechthoek een breedte, hoogte, x, y, en een schaduw kan hebben, en een cirkel kan ook ook een breedte, een hoogte, een x, een y, en een schaduw hebben.

Hier zie je dezelfde objecten, samen met de twee classes die we onderscheiden:

![](objects_and_classes.png)

In het diagram zie je ook pijlen met "is-a" erbij. Dit is om nauwkeurig aan te geven wat de relaties is tussen een object en een klasse. We zeggen bijvoorbeeld **`rectangle2` is a `Rectange`**.

## Classes in Python

Hieronder zie je de simpelste klasse die je kan definiëren in Python:

    def Circle:
        pass

`pass` betekent eigenlijk "sla deze regel over," dus dit is een lege klasse. Er staat geen code in en er zijn geen eigenschappen gedefinieerd.

We kunnen deze klasse wel al **instantiëren**, ofwel een object maken van die klasse. Als we de volgende instructie geven wordt er geheugen vrijgemaakt voor één cirkel-object. In dit geval geven we het object een naam `circle1`.

    circle1 = Circle()

Elke keer als je de naam van de klasse geeft met de ronde haken erachter, maak je een nieuw object aan:

    circle2 = Circle()

Als het programma wordt uitgevoerd staan er dus (kortstondig) twee objecten klaar in het geheugen.

## Attributen

Als we een object hebben, dan kunnen we attributen toekennen. We maken hieronder een nieuw rechthoek-object, we geven het een naam, en dan stellen we allerlei attributen of eigenschappen in. Dit gebeurt met de "dot notation". In Python kun je willekeurige attributen instellen op een object met een commando zoals hieronder. In veel andere talen moet je juist vooraf opgeven (in de code van de klasse) welke attributen aanwezig zijn.

    >>> rectangle1 = Rectangle()
    >>> rectangle1.width = 85
    >>> rectangle1.height = 87
    >>> rectangle1.x = 245
    >>> rectangle1.y = 199

## Verantwoordelijkheden

Naast eigenschappen kunnen in een klasse ook verantwoordelijkheden gedefinieerd worden. We kunnen bijvoorbeeld aangeven dat een rechthoek de mogelijkheid heeft om de oppervlakte te berekenen:

    class Rectangle:
        def area(self):
            return self.width * self.height

Als je dan een `Rectangle` aanmaakt en de eigenschappen instelt, dan kun je de oppervlakte laten uitrekenen:

    >>> rectangle1 = Rectangle()
    >>> rectangle1.width = 85
    >>> rectangle1.height = 87
    >>> rectangle1.x = 245
    >>> rectangle1.y = 199

    >>> print(rectangle1.area())

Objecten kunnen dus niet alleen dingen opslaan, maar ze kunnen ook dingen *doen*. Wat ze *kunnen* doen, dat staat in de (code van de) klasse gedefinieerd. Het lijkt erg op een functie, maar als we over objecten en classes praten, dan noemen we dit een **methode**.

Let op het woord "**self**" in de code van `area()`. Dat betekent zoveel als "gebruik voor deze berekening het object waar het nu over gaat". Als ik bijvoorbeeld op het object `rectangle1` de methode `area()` aanroep, dan willen we de oppervlakte van `rectangle1` weten. De variabele `self` verwijst daarom altijd naar *het object waarop de method wordt aangeroepen*.

## Initializer

Soms willen we dat een object niet kan bestaan zonder een aantal eigenschappen in te stellen Daarvoor kun je een speciale methode aanmaken: de initializer. Die schrijf je zo:

    class Rectangle:
        def __init__(self):
            self.width = 10
            self.height = 10

Als we dit zo neerzetten, dan zal de initializer-methode runnen bij het aanmaken van elk object van de klasse `Rectangle`. Per saldo krijgt dus elke rechthoek nu een breedte en hoogte van 10. Het is overigens wel gewoon mogelijk om deze informatie te overschrijven met nieuwe waarden.

Je kunt ook instellen dat een initializer een aantal parameters nodig heeft.

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

Hiermee wordt het verplicht om 4 waarden mee te geven bij het aanmaken van elk object. Zou je nu een `Rectangle`-object aanmaken zonder parameters, dan krijg je een error:

    >>> rectangle3 = Rectangle()
    TypeError

Geef je wel voldoende parameters, dan wordt het object aangemaakt zoals verwacht:

    >>> rectangle4 = Rectangle(5, 5, 0, 0)
    >>> print(rectangle4.width)
    5

## Setter

Je kunt ook methoden definiëren om de waarden van een aantal eigenschappen in te stellen:

    def set_position(self, c1, c2):
        self.x = c1
        self.y = c2

Omdat het geen initializer is, wordt de methode niet automatisch gebruikt. Maar als je de methode aanroept, dan zal deze de genoemde eigenschappen instellen voor het `self`-object.

Hieronder vind je het complete voorbeeld van een `Rectangle`-klasse:

    class Rectangle:

        def __init__(self, width, height, x, y):
            self.width = width
            self.height = height
            self.x = x
            self.y = y

        def set_position(self, c1, c2):
            self.x = c1
            self.y = c2

        def area(self):
            return self.width * self.height

Je ziet een initializer waar je vier waarden moét opgeven: width, height, x en y. Je ziet `set_position`, waarmee je een nieuwe locatie kan aangeven voor de rechthoek. En je ziet "area", een methode die als taak (verantwoordelijkheid) heeft om de oppervlakte uit te rekenen.

## Queue

In het voorgaande hebben we gesproken over een paar classes die figuren op het scherm moesten voorstellen. We kunnen classes ook gebruiken om zelf datatypes te bouwen, die we dan weer kunnen gebruiken als we algoritmes aan het implementeren zijn.

Een voorbeeld van een **abstract datatype** is een "queue". Dit is een soort **lijst**, maar de operaties die je kunt uitvoeren op de lijst zijn heel specifiek, en heel beperkt:

- je kunt een element toevoegen aan de **achterkant** van de lijst (back)
- je kunt een element weghalen van de **voorkant** (front)

Het is dus niet mogelijk om andere elementen te bekijken, het is niet mogelijk om elementen te verwijderen anders dan die aan de voortkant, het is niet mogelijk om op een willkeurige plek elementen toe te voegen.

Je ziet dus dat deze datastructuur veel **minder flexibel** is dan bijvoorbeeld een lijst. Een queue hoort op een bepaalde manier gebruikt te worden. Het principe dat bij een queue hoort heet "first in, first out" (fifo). Bij een stack is dit juist "last in, first out" (lifo). Beide structuren kunnen op allerlei manieren worden ingezet in algoritmen.

Hier een voorbeeld van hoe je een object van de klasse `Queue` zou willen **gebruiken**:

    >>> q = Queue()
    >>> q.enqueue(3)
    >>> q.enqueue(1)
    >>> print(q.dequeue())
    3

### Implementatie

Goed, laten we een stukje van die klasse maken. We beginnen met een hele kale klasse:

    class Queue:
        pass

En dan kijken we nog even terug naar de code die we hierboven schreven om de klasse `Queue` te gebruiken.

Die gaat nog niet werken, want de methoden `enqueue` en `dequeue` zijn nog niet gedefinieerd. Om dat te doen halen we `pass` weg en definiëren we de methoden:

    class Queue:
    
        def __init__(self):
            ...
    
        def enqueue(self, element):
            ...
    
        def dequeue(self):
            ...

Zoals je eerder krijgt elke methode in een klasse `self` als eerste argument, en dat staat voor het object waar nu mee gewerkt wordt. In het geval van `enqueue` wilden we ook een andere parameter meegeven, namelijk het object, het element dat in de queue gezet moet worden.

Dan moeten we even na gaan denken over: wat is een queue eigenlijk, waar werken we mee? Ja, het is een soort lijst dus we gaan ook een Python-list gebruiken als onderliggende structuur. In de initializer zetten we dus een lijst klaar voor het geval we `enqueue` en `dequeue` gaan aanroepen:

    def __init__(self):
        self._data = []

Hoe zullen we dan `enqueue` implementeren? Python-lists hebben de method `append`, dus die ligt voor de hand om hier te gebruiken. Daarmee wordt `enqueue` niet veel meer dan een alias voor `append`:

    def enqueue(self, element):
        self._data.append(element)

Hiermee hebben we dus al een half-werkende queue! Eentje die data kan aannemen, maar teruggeven kan nog niet.

Omdat we ervoor hebben gekozen `append` te gebruiken voor `enqueue`, komen de elementen aan de **achterkant** (rechterkant) van de lijst terecht. Dat heeft consequenties voor `dequeue`, want als je die gebruikt moeten de elementen van de andere kant komen, dus de **voorkant**.

Ook voor het opvragen en verwijderen van een element aan de voorkant van een lijst is er gelukkig een methode ingebouwd in Python. We kunnen in de documentatie vinden dat de methode `pop()` willekeurige elementen kan verwijderen. Geven we aan `pop` het argument `0`, dan zal altijd het meest linkse element worden verwijderd. Roepen we `pop` aan, dan geeft deze bovendien het element terug dat zojuist verwijderd is. Het enige dat dequeue nog hoeft te doen is het doorsturen van die waarde.

    def dequeue(self):
        return self._data.pop(0)

Testen we de klasse nu met onze zelfbedachte testcode, dan hebben we een eerste indicatie dat de klasse goed werkt.

Al met al hebben we een klasse voorzien van de volgende functionaliteit:

- De initializer zet een lege lijst klaar die dient als onderliggende structuur voor de opslag van gegevens
- De `enqueue`-functie voegt een element toe op de "queue-manier"
- De `dequeue`-functie verwijdert een element op de "queue-manier" en geeft dit terug

Daarmee kunnen we ook een compleet diagram tekenen van de klasse:

![](queue-diagram.png)

Bovenaan staat de naam van de klasse; in het tweede vak staan de attributen, maar die is leeg, omdat het niet de bedoeling is dat er direct veranderingen worden gedaan aan de lijst waarin we onze waarden opslaan; en in het derde vak staan juist de methodes die nodig zijn om de queue op de "juiste manier" te bedienen.

## Encapsulation

Hierboven hebben we besloten dat **in** een queue gebruik wordt gemaakt van een lijst voor het opslaan van de gegevens. In Python bouw je vaak je datastructuren op de datastructuren die Python zelf al aanbiedt. De ingebouwde structuren zijn **set**, **tuple**, **dictionary**, en **list**. Afhankelijk van de klasse die je wil bouwen kies je voor zo'n structuur om de data in op te slaan.

* Een **set** is echt een hele snelle manier om willekeurig elementen toe te voegen en weer weg te halen uit een verzameling. De volgorde is niet relevant, dus als je een element uit een set haalt weet je vooraf niet welke. Voor een queue is dat natuurlijk wel belangrijk, zodat het fifo-principe aangehouden kan worden.

* Een **tuple** is een lijst-element (eigenlijk een soort struct) waar je geen veranderingen in kan aanbrengen. Je kunt geen elementen toevoegen of verwijderen. Dat is één van de essentiële functies van een queue, dus ook een tuple valt af.

* Een **dictionary** is niet zozeer een lijst, als wel een "mapping van keys naar values". Dat betekent dat je heel efficiënt aan een dict kan vragen: hier heb je X, geef me de bijbehorende Y. Bij een queue is de enige associatie de volgorde van invoeren van de elementen, dus dit principe past niet.

* Een **list** is misschien wel de simpelste, en heeft als voornaamste eigenschap dat elementen op volgorde bewaard worden, en ook op nummer opgevraagd kunnen worden. Een list is wel wat langzamer dan bijvoorbeeld een set voor het toevoegen en verwijderen van elementen, maar biedt als enige structuur de operaties die we nodig hebben om een queue te bouwen.

Meer informatie over snelheid van de operaties die je op de standaard-datastructuren kunt toepassen vind je in de [Python Wiki](https://wiki.python.org/moin/TimeComplexity). Overigens vind je daar ook een verwijzing naar de `dequeue` die bij Python wordt meegeleverd. Je zou dus niet eens zelf een queue hoeven implementeren, maar daarover later meer.

## Privé-variabelen

Het is je misschien al opgevallen dat er een underscore staat voor de variabele `_data`. Dat is om te laten zien dat het een privé-element is, dat het niet van "buitenaf" aangepast moet worden. Je moet de queue alleen maar aanpassen door "enqueue" en "dequeue" aan te roepen. Zolang je dat doet weet je ook zeker dat het fifo-principe gehandhaafd blijft.

## UML

Hierboven hebben we al plaatjes (diagrammen) getekend van classes en objecten. Het is zeer gebruikelijk om klasse-diagrammen te tekenen volgens de UML-standaard (unified modeling language). Hier nog even de onderdelen:

![](queue-impl-dia.png)

- In het eerste blok heb je de klasse-**naam**, `Queue` in dit geval.

- Dan heb je een blokje met de verschillende **attributen**. In dit geval hebben we het privé-attribuut `_data` ook vermeld, hoewel het niet relevant is om de werking van de klasse te kunnen begrijpen.

- In het onderste blokje staan de verantwoordelijkheden van het geheel, ofwel de **methodes**.

- Het tweede en derde blokje samen noem je de **members** van de klasse: de onderdelen.

## Cards

Een ander voorbeeld is een kaartspel. Dat zijn objecten die in de echte wereld ook voor kunnen komen en die we kunnen beschrijven met classes. In dit geval hebben we een "Card"-klasse waarin één enkele speelkaart wordt beschreven en we hebben een "Deck"-klasse waarin een compleet kaartspel van 52 kaarten wordt beschreven.

### Data class

`Card` zou er bijvoorbeeld zo uit kunnen zien.

![](card.png)

De attributen zijn `suit` en `value`, ofwel de kleur en de waarde van de kaart. Er is een methode genaamd `description()`.

`Card` is een **data-klasse**. Dat betekent dat we juist geen methodes definiëren voor manipulatie, maar dat het de bedoeling is direct de attributen van de klasse aan te passen. In dit geval gaat het om twee strings die samen de speelkaart beschrijven.

### Full class

De `Deck`-klasse heeft juist geen attributen, maar een heleboel methods, in dit geval om te schudden (`shuffle`), om een kaart af te geven (`deal`) en wederom de `description`. Deze klasse is dus helemaal **encapsulated**, dat betekent dat we niet van buitenaf kunnen zien hoe het Deck kaarten wordt opgeslagen en we kunnen niet zien wat de volgorde is.

### Implementation details

Wat voor Python-datastructuur zouden we kunnen gebruiken voor de `Deck`-klasse?

- Bij een kaartspel is volgorde in zekere zin wel belangrijk, want je schudt het, maar daarna moet het wel in volgorde blijven, dus een set valt wederom af. 

- Er worden steeds kaarten afgegeven, dus een tuple valt ook af omdat je hier geen wijzigingen in kan aanbrengen.

- De kaarten staan op zich, dus een dictionary is ook niet voor de hand liggend.

- En een lijst is de handige keuze, omdat volgorde weer een rol speelt.

## Relaties in UML

In UML-diagrammen kunnen we niet alleen klassen specificeren, maar ook de **relaties** tussen de verschillende klassen. In dit geval weten we dat een kaartspel diverse kaarten bevat. We noemen dat vaak een "has-many relation". Dat wordt weergegeven met een pijl:

![](relations.png)

De pijl loopt **van** de klasse die het onderwerp is van de relatie, en **naar** de klasse die het lijdend voorwerp is van de relatie.

Er zijn een aantal standaardrelaties die je kunt beschrijven zoals "has one" en "belongs to". Je kunt het ook zelf verzinnen als dat nodig is om helemaal duidelijk te maken wat de precieze relatie is.

## Abstractie

In bovenstaande en andere voorbeelden hebben we het vaak over objecten uit de "echte wereld". Vergeet niet dat we daarbij ook altijd een heleboel informatie weglaten, zoals bijvoorbeeld:

- Kaarten in een kaartspel hebben altijd een zeker ontwerp op de achterkant staan. Het uiterlijk van de kaarten is echter niet relevant voor de werking van kaartspelletjes, dus die laten we nu weg.

- Als je een kaartspel speelt in het echt, dan wil je vaak meerdere keren spellen. Zodra het spel afgelopen is verzamel je alle kaarten, schud je ze, en dan kan het opnieuw beginnen. In code kun je dan net zo goed een "nieuw" kaartspel aanmaken en het oude weggooien.

Zo zijn er allerlei overwegingen om elementen van de echte wereld wel of niet op te nemen in het model dat je met code aan het bouwen bent. En je zult soms ook weer aanpassingen gaan maken aan je classes om nieuwe toepassingen mogelijk te maken. Maar uiteindelijk blijven je classes altijd een abstractie van de werkelijkheid.

## Conclusie

Objectgeoriënteerd programmeren heeft nog een heleboel andere aspecten, maar die heb je niet nodig op dit moment. Belangrijk is dat je weet:

- hoe je methodes kan schrijven, 
- hoe methodes iets te maken hebben met de verantwoordelijkheden van classes en objecten, 
- wat het verschil is tussen een klasse en een object, en
- hoe je "self" moet gebruiken.
