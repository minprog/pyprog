# Priemgetallen

> **Studeertip.** De challenges zijn alleen voor studenten die het erg makkelijk vinden tot nu toe. Als je een challenge hebt gemaakt, klop dan bij het laptopcollege bij je docent aan om 'm door te spreken.

## Achtergrond

Een computer is geweldig in het snel uitvoeren van een heleboel "domme" stappen. Een voorbeeld waar een computer zóveel effectiever is dan een enkele persoon, is het uitrekenen van priemgetallen. De definitie van een priemgetal is niet al te ingewikkeld. Maar bepalen hoeveel delers een willekeurig getal heeft kan ontzettend veel tijd kosten. Python to the rescue!

## Deel 1: Het zoveelste priemgetal

Implementeer een programma dat op verzoek het $$N$$-de priemgetal genereert.

    Naar het hoeveelste priemgetal bent u op zoek? 1000
    7919

### Specificatie

- Vraag de gebruiker om de *rangorde* van het priemgetal (het hoeveelste) in te voeren. Dit moet dus een geheel en positief getal zijn.

- Als de gebruiker een rangorde invult die niet toegestaan is, dan vraag je de gebruiker opnieuw naar de rangorde. En herhalen tot de gebruiker een geldige rangorde invult. Omdat je niet weet hoe vaak dat zal zijn, moet het een `while`-loop worden.

- Ofschoon je moet controleren of het om een positief getal gaat, mag je er wel vanuit gaan dat een geheel getal wordt ingevoerd (en geen kommagetal). Dat hoef je dus niet te controleren.

- Zodra de rangorde bekend is, bereken het juiste priemgetal en rapporteer dit terug aan de gebruiker.

- Zorg dat het programma niets anders uitvoert dan dit getal, zoals in het voorbeeld bovenaan de opdracht!

- Het programma moet drie functies met de gegeven namen bevatten die alle stappen zoals onder beschreven uitvoeren.

### Probleemanalyse

Neem vóór je gaat programmeren eerst een paar minuten om met **pen en papier** te schetsen hoe je zelf het probleem aan zou pakken, hoe je het probleem kunt opdelen in overzichtelijke stappen. De specificatie hierboven geeft al wat hints daarvoor.

Bij deze opdracht nemen we je aan de hand door een aantal stappen te geven om te doorlopen tijdens het ontwikkelen van de juiste oplossing.

### Stap 1: priem-check

Een belangrijk deel van de omschrijving hierboven is dat het om priemgetallen gaat. Wat is een priemgetal? Dat moeten we in Python zien uit te drukken.

Definieer dus eerst een functie `is_priem()` met één argument die van een bepaald getal, het argument, onderzoekt of het een priemgetal is of niet. De functie moet een `bool` returnen.

Begin zo simpel mogelijk. Gebruik een `for`-loop en `%` (modulo) om te bepalen hoeveel getallen een deler zijn van het argument. Als je dit bijhoudt in de loop (tellen!), kun je na afloop van de loop bepalen of het getal een priemgetal is of niet.

### Stap 2: check een hele partij getallen

We gaan een stap verder. We kunnen de code nu hergebruiken (dus de functie aanroepen) en voor *elk* getal onder de 100 bepalen of het een priemgetal is of niet.

Definieer een functie `print_priemen_tot()` met één argument, `N`. Maak in deze functie een `for`-loop om alle getallen onder de `N` langs te loopen en bepaal voor elk van deze "kandidaat-priemgetallen" of het wel of niet een priemgetal is door de functie `is_priem` aan te roepen.

Schrijf deze procedure en maak deze goed werkend. De functie moet niets returnen, maar moet wel ieder gevonden priemgetal printen.

Klopt je antwoord? Check op internet of de geprinte getallen overeenkomen!

### Stap 3: het zoveelste priemgetal

We gaan nu terug naar het eerder beschreven doel: op zoek naar het $$N$$-de priemgetal. We geven een voorzetje voor de strategie van het programma:

- Nu zoeken we het `N`-de priemgetal; we willen niet weten of `N` een priemgetal is (zie je het verschil met stap 2?) Je kunt dus niet meer met een `for`-loop simpelweg tot `N` loopen. Immers, bij een `for`-loop weet je van tevoren hoe vaak er geïtereerd wordt en dat weten we nu niet. Je moet dus in je programma gaan bijhouden *hoeveel* priemgetallen je al gevonden hebt. Gebruik hiervoor een variabele, net als bij het bijhouden van de hoeveelheid delers in Stap 1. Merk op dat dit bijhouden van informatie in een variabele (bv. een 'teller') nu al een paar keer handig blijkt. We zullen dit meerdere keren terug zien komen bij de rest van het vak, dus oefen er goed mee!

- Definieer een functie `zoveelste_priem()`, met één argument: `N`. De functie moet vervolgens het `N`de priemgetal returnen.

- Zoals bovenaan beschreven moet bij het runnen van je programma de gebruiker om input worden gevraagd tot een geheel getal wordt gegeven. Doe dit opvragen buiten de functie en geef de input als argument aan je functie.

- Begin klein. Zorg dat je programma eerst de priemgetallen tot 10 kan vinden. Dat is klein genoeg om te zien of het programma precies doet wat de bedoeling is, en kun al snel ontdekken wat er mis gaat.

- Problemen? Print bij elke kandidaat-priem wat informatie, zodat je weet waar je bent in de berekening en je ziet of de computer ook echt jouw bedoelde strategie volgt.

### Stap 4: werkt het echt?

Loop nu de specificatie bovenaan de opdracht goed door en zorg dat je programma precies zo werkt als daar beschreven is.

### Stap 5: kleine optimalisaties

Deze stap is volledig optioneel, dus hoeft niet ingeleverd te worden. Wel goed om over na te denken en te proberen als je tijd over hebt.

We zijn hierboven zo simpel mogelijk begonnen, zodat we snel tot een *correct* programma zijn gekomen. Maar met behulp van wat wiskundig inzicht kunnen we kleine optimalisaties doen, waardoor het programma sneller wordt.

- Behalve 2 zijn *even* getallen nooit een priemgetal (dit vraagt slechts een hele kleine aanpassing van je code).

- Als je een deler vindt hoef je niet verder te zoeken omdat je dan gelijk weet dat het geen priemgetal is.

### Hints

Je kunt dit programma schrijven met alleen de Python-onderdelen die je tot nu toe hebt geleerd + loops!





## Deel 2: reeks niet-priemgetallen

Schrijf een programma dat de *langste aaneengesloten reeks niet-priemgetallen* bepaalt onder de 10,000 en daar een korte samenvatting van geeft.

    # python reeks.py
    De langste reeks niet-priemgetallen onder de 10,000 begint op ... en eindigt bij ...
    De reeks is ... lang.

Lees goed wat er gevraagd wordt: de begin en eindpunten zijn zelf dus *geen* priemgetallen. Onder het getal 100 moet het antwoord zijn:

    # python reeks.py
    De langste reeks niet-priemgetallen onder de 100 begint op 90 en eindigt bij 96
    De reeks is 7 lang.

De opdracht luidt om de langste reeks te vinden onder het getal 10,000.

### Achtergrond

Bepaal altijd met pen en papier je strategie en ga dus niet gelijk tikken. De 5--10 minuten die je hieraan besteedt verdien je dik terug tijdens het omzetten naar programmacode.

Om het idee van de reeks niet-priemgetallen goed te begrijpen, schrijf je bijvoorbeeld de eerste tien priemgetallen op papier en bekijk steeds de onderlinge afstand: tussen 2 en 3 is het verschil maar één, terwijl het verschil tussen 13 en 17 vier is (wat dus betekent dat er 3 opeenvolgende getallen tussen zitten die niet-priem zijn, namelijk 14, 15 en 16).

### Specificatie

- Maak een programma genaamd `reeks.py` en zorg dat het volgens bovenstaand voorbeeld de juiste informatie uitprint.

- Zet bovenaan je programma `from priemgetal import is_priem` zodat je de functie `is_priem` van de vorige opgave kunt gebruiken.

- Zorg dat je programma twee functies definieert:

    1. `zoek_langste_reeks()`, een functie met één argument, `N`, die de langste reeks niet-priemgetallen onder `N` vindt en de grenzen teruggeeft. Gebruik `return onder, boven` om de onder- en bovengrens te returnen.
    2. `print_boodschap()`, een functie met als argumenten de eerder gedefinieerde `N` plus een reeds gevonden onder- en bovengrens. De functie doet niets anders dan de uitslag printen zoals in het voorbeeld bovenaan.

- De functies mogen geen lijsten gebruiken.

- Stap (loop) door alle priemgetallen heen en bepaal telkens hoe lang de reeks niet-priemgetallen is tussen het huidige en het vorige priemgetal. Houd bij wat de langste reeks is in een aparte variabele.

- Roep in je `main`-code de functie `zoek_langste_reeks()` aan met als argument `10000`. Daarna geef je de uitkomst door aan `print_boodschap()`. Zorg dat je output er netjes uitziet en dat we als gebruiker iets aan de informatie hebben.

### Testen

Loop nu de specificatie bovenaan de opdracht goed door en zorg dat je programma precies zo werkt als daar beschreven is. Test zelf met 100 en met 10,000.





## Deel 3: Het vermoeden van Goldbach

Schrijf een programma dat laat zien dat het vermoeden van Goldbach correct is voor de even getallen (groter dan 2) tot en met 1000.

    # python goldbach.py
    16 = ...
    18 = 5 + 13
    20 = 3 + 17
    22 = 5 + 17
    24 = ...

### Achtergrond

Het vermoeden van Goldbach is een van de oudste onopgeloste problemen in de wiskunde. Goldbach stelde:

*"Elk even getal groter dan 2 kan geschreven worden als de som van twee priemgetallen."*

Een priemgetal mag hierbij ook twee keer gebruikt worden (6 = 3 + 3). Hoewel dit vermoeden inderdaad blijkt te kloppen voor alle getallen tot $$4\cdot10^{18}$$ is er nog altijd geen analytisch bewijs voor het vermoeden.

Misschien onverwacht: een computer blijkt ongeschikt om het vermoeden te bewijzen (je kunt immers niet tot oneindig tellen); maar je zou het vermoeden wel kunnen ontkrachten door een even getal te identificeren dat niet te schrijven is als de som van twee priemgetallen. Dat zou een tegenbewijs zijn. Spoiler: ook dat is nog niet gevonden.

We gaan ons steentje bijdragen in deze zoektocht door systematisch de even getallen door te nemen en te kijken of de stelling van Goldbach klopt voor elk getal.

### Specificatie

Laat met een programma **goldbach.py** zien dat alle even getallen tot en met 1000 inderdaad te schrijven zijn als de som van twee priemgetallen. Concreet: laat voor elk even getal ook *expliciet* zien (op het scherm) dat het te schrijven is als de som van twee priemgetallen, zoals in het voorbeeld hierboven. Schrijf je programma in een functie die je aanroept onderaan je code.

Nog belangrijker is natuurlijk als je een getal vindt dat *niet* aan het vermoeden van Goldbach voldoet. Zorg dat jouw programma zo'n ontdekking duidelijk op het scherm aangeeft. Bingo!

### Hints

- Bepaal altijd met pen en papier je strategie en ga dus niet gelijk tikken. De 5-10 minuten die je hieraan besteedt verdien je dik terug tijdens het omzetten naar programmacode.

- Gebruik in ieder geval de functie `is_priem()` via een `import`, zoals bij de vorige opgave.

- Het is daarnaast de bedoeling om je programma in verschillende functies op te delen.

- Zet in je `main` alleen maar de opdracht om een functie aan te roepen met het getal `1000` als argument, zodat de betreffende functie stopt na 1000 even getallen. De functie zou echter ook moeten werken als we 1010 getallen willen nalopen, of een ander aantal.

### Testen

Loop nu de specificatie bovenaan de opdracht goed door en zorg dat je programma precies zo werkt als daar beschreven is.


# Inleveren

Als je je uitwerkingen inlevert worden ze gecheckt.
