# Tutorial: Cyclomatic Complexity

Je programma's werken, maar werkende code is niet altijd *leesbare* code. In deze
tutorial leer je code herkennen die te ingewikkeld is en haal je die stap voor
stap uit elkaar. Als maat gebruik je de **Cyclomatic Complexity**: het aantal
verschillende routes door een stuk code.

**Hoe het werkt.** In de editor staan de bestanden al klaar, je hoeft dus niets
te kopiëren. Je werkt aan `hangman.py`; de bioscoop (`cinema.py`) is een extra
opdracht voor als je tijd over hebt. Verder staan er `dictionary.txt` met de
woorden voor het spel, en `hangman_original.py` en `cinema_original.py`.

Die laatste twee zijn kopieën van de originele programma's, en daar blijf je
vanaf. Ze staan er zodat je altijd kan terugkijken, en zodat de knop **compare**
kan controleren of jouw versie nog precies dezelfde output geeft.

Nieuw zijn twee knoppen. **complexity** rekent voor het bestand dat je op dat
moment open hebt de Cyclomatic Complexity van elke functie uit, en klaagt over
elke functie die hoger uitkomt dan 3. **compare** vergelijkt de output van jouw
versie met die van het origineel. Met **run** draai je het programma zelf.

Werk de pagina's op volgorde door.

{% next "Beginnen" %}

## 1. Wat is Cyclomatic Complexity?

Het idee is vrij simpel: elke **beslissing** maakt een functie complexer. Een
`if`/`else`-statement of een `for`/`while`-loop zorgt voor een splitsing in de
weg. Het maakt een extra route mogelijk waarmee je door de code kunt lopen. Hoe
meer van zulke routes er bestaan, hoe ingewikkelder het is om de code te
begrijpen.

Cyclomatic Complexity meet het aantal verschillende routes door een stuk code.
Het resultaat is een getal van 1 of meer. Neem bijvoorbeeld deze functie:

```
def join(string: str, items: list[str]) -> str:
    """
    Return a string which is the concatenation of the strings in items.
    The separator between elements is the string.
    """
    if len(items) == 0:
        return ""

    result = items[0]

    for item in items[1:]:
        result += string + item

    return result
```

In deze functie zitten twee controlestructuren, dus twee keuzepunten. Dat maakt
drie mogelijke unieke routes:

* De conditie van de `if` is waar, dan zijn we direct klaar.
* De conditie van de `if` is niet waar, `items[1:]` is leeg en de `for`-loop
  wordt daarom niet uitgevoerd, dan ook klaar.
* De conditie van de `if` is niet waar, `items[1:]` is niet leeg, dan wordt de
  `for`-loop uitgevoerd en daarna zijn we klaar.

De Cyclomatic Complexity van deze functie is daarom 3.

Een handige vuistregel: begin bij 1 en tel 1 op voor elke `if`, elke `elif`,
elke `for` en elke `while`. Een `else` is geen extra beslissing, want die hoort
bij de `if` die je al geteld hebt.

{% next "Verder: zelf tellen" %}

## 2. Zelf routes tellen

Reken voor de hand uit wat de Cyclomatic Complexity van deze functie is:

```
def grade(points: int, bonus: bool) -> str:
    if points < 0:
        return "invalid"
    if bonus:
        points += 1
    for _ in range(3):
        points += 0
    if points >= 8:
        return "great"
    elif points >= 6:
        return "pass"
    else:
        return "fail"
```

Tel eerst zelf, ga daarna naar de volgende pagina voor het antwoord.

{% next "Verder: het antwoord" %}

Je begint bij 1 en telt op: de eerste `if` (2), de tweede `if` (3), de `for`
(4), de derde `if` (5) en de `elif` (6). De `else` telt niet mee. De Cyclomatic
Complexity is dus **6**.

Een score van 6 is nog te overzien, maar je ziet al waar het heen gaat: alle
beslissingen in een functie tellen bij elkaar op. Zet je tien beslissingen in
één functie, dan moet je bij het lezen al die routes tegelijk in je hoofd
houden.

Wat is nou "te hoog"? Daar bestaat geen harde grens voor, maar in deze tutorial
houden we een strenge grens aan: **maximaal 3** per functie. Dat dwingt je om
functies te schrijven die één ding doen.

{% next "Verder: meten" %}

## 3. Meten met de knop complexity

Tellen met de hand is leerzaam, maar je hoeft het niet zelf te doen. De
Cyclomatic Complexity is goed automatisch te berekenen. In deze tutorial is daar de **complexity** knop voor.
Die rekent voor elke functie in het bestand dat je open hebt de score uit, en
noemt elke functie die boven 3 uitkomt.

Open `hangman.py` in de editor en klik op **complexity**. Je hoort dit te zien:

    hangman.py:4: 'hangman_game' heeft een Cyclomatic Complexity van 17

Oftewel: in de functie `hangman_game`, die op regel 4 begint, zitten 17
verschillende routes.

Probeer de knop ook eens op een programma dat je zelf eerder geschreven hebt.
Als het goed is wijst hij de ingewikkelde punten in je programma aan.

{% next "Verder: het spel" %}

## 4. Kennismaken met Hangman

In `hangman.py` staat een werkend spelletje Hangman (galgje). De computer kiest
een woord uit `dictionary.txt` en vervolgens raad jij letter voor letter het woord.

Klik op **run** en speel een spelletje. Kies een woordlengte tussen 3 en 10,
want zulke woorden staan in `dictionary.txt`.

Let goed op hoe de output eruit ziet: welke vragen het programma stelt, wat het
na elke gok print, en wat er aan het eind staat. Dit is ook precies hoe jouw
aangepaste programma moet blijven werken.

Lees daarna de code helemaal door. Je ziet dat alles in één grote functie staat,
met commentaarregels als scheiding tussen de onderdelen.

{% next "Verder: vergelijken met het origineel" %}

## 5. Vergelijken met het origineel

Je gaat de code flink verbouwen, en bij elke stap kan er iets kleins veranderen
in wat het programma print: een punt die wegvalt, een regel die er twee keer
staat, een melding die niet meer komt. Daarom staat `hangman_original.py` in de
editor: dat is dezelfde code als `hangman.py`, maar die versie laat je zoals hij
is. **Pas `hangman_original.py` dus niet aan.**

Daar is de knop **compare** voor. Die draait jouw versie en het origineel
allebei, met dezelfde antwoorden, en vergelijkt regel voor regel wat ze printen.
Klik er nu eens op. Omdat je nog niets veranderd hebt, hoor je dit te zien:

    Test 1: output is precies gelijk.
    Test 2: output is precies gelijk.
    Test 3: output is precies gelijk.
    Test 4: output is precies gelijk.

    Alle 4 tests geven dezelfde output als hangman_original.py.

De vier tests spelen een spel dat verloren gaat, een spel dat gewonnen wordt,
een spel met allerlei ongeldige invoer (een woordlengte van 0, een gok van twee
letters, twee keer dezelfde letter) en een kort woord met één poging.

Verandert er straks iets aan de output, dan wijst de knop de eerste regel aan
die niet klopt:

    Test 1: VERSCHIL op regel 5
        origineel: "Guess a letter (6 left): It's in the word! :)"
        bij jou:   "Guess a letter (6 left): It's in the word! :-)"
        antwoorden: 5 6 a e i o u b c d f g h j k l m n p q r s t v w x y z

Onder `antwoorden` staan de antwoorden die de test heeft ingetypt, in die
volgorde. Zo kan je het spel zelf met **run** naspelen en kijken wat er gebeurt.

Klik dus na elke stap op **compare**. Zo weet je precies bij welke verandering
de output stuk ging, en hoef je niet achteraf te zoeken.

Twee dingen om te weten:

* De knoppen **compare** en **complexity** kijken naar het bestand dat je op dat
  moment open hebt. Werk je aan de bioscoop, open dan `cinema.py`.
* Klik je ze aan terwijl `hangman_original.py` voor je staat, dan vergelijkt
  **compare** het origineel met zichzelf (altijd gelijk) en klaagt
  **complexity** nog steeds over de complexiteit. Dat hoort zo.

{% next "Verder: de opdracht" %}

## 6. De opdracht

Aan jou de taak om `hangman.py` zo te verbeteren dat geen enkele functie een
Cyclomatic Complexity hoger dan 3 heeft. De knop **complexity** mag dus niet
meer klagen.

Dat kan op twee manieren:

1. De code opbreken in kleinere functies.
2. De code zelf eenvoudiger maken, zodat er minder routes mogelijk zijn.

De spelregels:

* De output van het programma moet **exact** hetzelfde blijven, inclusief alle
  teksten en leestekens. Vergelijk met `hangman_original.py`.
* Alle code blijft in één bestand: `hangman.py`.
* `hangman_original.py` blijft onaangeroerd.
* Alle code mag worden gewijzigd.
* Geen enkele functie mag een Cyclomatic Complexity hoger dan 3 hebben.
* De type hints moeten blijven kloppen. Klik af en toe op **typecheck**.

En de werkwijze, want dit is het belangrijkste van de hele tutorial: werk **één
functie per keer**. Haal een stukje code uit `hangman_game`, zet het in een
eigen functie, roep die functie aan op de plek waar de code stond, en draai het
programma om te kijken of het nog hetzelfde doet. Pas daarna ga je verder met
het volgende stukje. Als je in één keer alles verbouwt, weet je bij een fout
niet meer waar die zit.

{% next "Verder: aan de slag" %}

## 7. Aan de slag

Nu ga je zelf op zoek naar de plekken om te knippen. Lees `hangman_game` van
boven naar beneden en bepaal waar een onderdeel begint en eindigt. De
commentaarregels zijn daarbij een hint: waar de programmeur een kopje nodig had
om uit te leggen wat er gebeurt, zit vaak een functie verstopt. Vertrouw er niet
blind op, want soms hoort er meer bij elkaar en soms zitten er twee dingen in
één blok.

Een paar vragen die je bij elk stukje kan stellen:

* **Kan ik in één zin zeggen wat dit stukje doet?** Die zin is de naam van je
  functie. Lukt het niet om een naam te vinden, dan heb je waarschijnlijk op de
  verkeerde plek geknipt.
* **Wat heeft dit stukje nodig, en wat levert het op?** Dat zijn de parameters
  en de `return`-waarde. Een stukje dat van alles uit de rest van de functie
  nodig heeft, is meestal nog niet goed afgebakend.
* **Staat deze code ergens anders ook (bijna)?** Dan is dat één functie die je
  twee keer aanroept.
* **Hoeft dit stukje echt te printen?** Een functie die een waarde uitrekent of
  opbouwt en die teruggeeft, kan je los uitproberen zonder het hele spel te
  spelen. Laat de `print` dan buiten de functie staan.

En een paar dingen om op te letten:

* Een functie met een loop én een `if` erin zit al snel op 3. Zit je erboven,
  dan moet er nog een stukje uit.
* Soms is korter ook eenvoudiger. Zodra je binnen een loop het antwoord al weet,
  mag je meteen `return`'en. Dan heb je geen hulpvariabele en geen `break` meer
  nodig, en dat is ook weer een route minder.
* De teksten in de `input`- en `print`-aanroepen laat je precies staan zoals ze
  waren, anders verandert de output.
* Functies die iets toevoegen aan een `set` die ze meekrijgen (zoals
  `guesses.add(letter)`) werken gewoon: de aanroeper ziet die verandering. Maar
  een `int` werkt niet zo. Verlaagt een functie het aantal pogingen, dan moet je
  het nieuwe aantal `return`'en en in de aanroeper weer opslaan.
* Klik na elke stap op **compare**. Zo merk je het meteen als de output
  verandert, en weet je ook door welke verandering dat gebeurde.

Werk zo door tot de knop **complexity** niets meer te klagen heeft. Kom je er
niet uit, vraag dan een assistent om mee te kijken.

{% next "Verder: hangman klaar" %}

## 8. Hangman klaar

Klik nog één keer op **compare**, op **complexity** en op **typecheck**. Zijn
alle tests gelijk en is er geen klacht meer, dan is `hangman.py` af.

Kijk nu eens naar het bestand als geheel. Je hebt geen regel functionaliteit
toegevoegd, en toch is het programma veel beter te begrijpen: bovenaan staat een
korte `hangman_game` waarin je in een paar regels ziet wat het spel doet, en
daaronder staan de details, elk met een naam die uitlegt waar het stukje voor
is.

Dit is ook precies waarom Cyclomatic Complexity nuttig is als maat: een hoge
score betekent veel routes door de code, en veel routes betekent veel
testgevallen voordat je zeker weet dat alles werkt. Code met lage scores is
beter te lezen én beter te testen.

Ben je hier tijdens het werkcollege aangekomen, dan heb je het belangrijkste
gehad. De volgende pagina's zijn extra.

{% next "Verder: extra opdracht bioscoop" %}

## 9. Extra: de bioscoop

Deze opdracht is optioneel, voor als je tijd over hebt. Hij is een stuk minder
gestuurd: je krijgt hints, maar geen stappenplan.

In `cinema.py` staat de kassa van een bioscoop. Je geeft de dag, het tijdstip,
of het een 3D-film is en het aantal kaartjes in. Daarna geef je voor ieder
kaartje de leeftijd van de bezoeker op en krijg je de prijs te zien. Aan het
einde volgt het totaalbedrag. Dit zijn de regels:

* Een kaartje kost (in euro's) 0,00 tot en met 2 jaar (`infant`), 6,00 tot en
  met 11 jaar (`child`), 10,00 tot en met 64 jaar (`adult`) en 7,50 vanaf 65
  jaar (`senior`).
* Een volwassene met een studentenkaart krijgt 1,50 korting (`student`).
* Kaartjes voor `infant`s zijn altijd gratis, toeslagen en kortingen gelden
  niet.
* Op zaterdag en zondag is een kaartje 1,00 duurder, op dinsdag 2,00 goedkoper.
* Begint de film voor 12 uur dan is een kaartje 1,00 goedkoper, vanaf 18 uur
  1,50 duurder.
* Een 3D-film kost 2,00 extra per kaartje.
* Bij 4 kaartjes of meer is er 10% groepskorting op het totaalbedrag.

Zo ziet een voorbeeld eruit:

    WELCOME TO THE CINEMA
    Which day? (monday-sunday)
    saturday
    At what hour does the movie start? (0-23)
    20
    3D movie? (y/n)
    y
    How many tickets?
    2
    Age of visitor 1?
    30
    Student card? (y/n)
    n
    Ticket 1: adult 14.50
    Age of visitor 2?
    8
    Ticket 2: child 10.50
    Total: 25.00

Open `cinema.py`, klik op **run** en probeer een paar kaartjes uit. Klik daarna
op **complexity**:

    cinema.py:1: 'cinema' heeft een Cyclomatic Complexity van 21

De opdracht is dezelfde als bij hangman: zorg dat geen enkele functie boven 3
uitkomt, met exact dezelfde output, alles in `cinema.py`, en met kloppende type
hints. Ook hier staat het origineel klaar, in `cinema_original.py`, en ook dat
bestand laat je zoals het is. De knop **compare** werkt hier precies zo, met
vier eigen tests: het voorbeeld hierboven, een bezoek met een baby, een senior,
een student en groepskorting, een gratis kaartje, en een paar leeftijden en
tijden die precies op de grens zitten. Open wel eerst `cinema.py`, want de
knoppen kijken naar het bestand dat je open hebt.

{% next "Verder: hints voor de bioscoop" %}

## 10. Hints voor de bioscoop

Bij hangman kwam je een heel eind met code uitknippen en in een functie zetten.
Hier is dat niet genoeg: dit programma zit vol losse beslissingen, en een paar
daarvan kan je beter helemaal anders opschrijven.

**Herhaalde code.** Het programma vraagt een paar keer om een getal binnen een
bereik, en een paar keer om een ja/nee-antwoord. Zoek die herhaling op en maak
er functies van die je meerdere keren kan gebruiken, bijvoorbeeld

```
def ask_int(prompt: str, error: str, low: int, high: int) -> int:
    ...
```

Let op dat de teksten van de prompts precies hetzelfde blijven. Je geeft ze nu
mee als argument.

**`if`/`elif`-ketens.** Een lange `if`/`elif`-keten die een waarde uitkiest op
basis van een andere waarde, is eigenlijk een opzoektabel. Dat kan vaak veel
korter met een `dict` of met een tuple van tuples. Een `dict` heeft bovendien
`.get(key, default)`, waarmee je zelfs de "anders"-situatie niet met een `if`
hoeft op te lossen.

**Stap voor stap rekenen.** Het uitrekenen van de prijs van één kaartje is een
apart stukje werk: leeftijd erin, prijs eruit. Hetzelfde geldt voor het bepalen
van de toeslag voor het tijdstip of voor de dag. Als functies maar één ding
doen, hoeven ze ook niet veel keuzes te maken.

**Testen.** De knop **compare** dekt een aantal gevallen, maar niet alles. Speel
met **run** ook zelf een paar bezoeken na: een ongeldige dag, een uur dat net op
de grens zit (11, 12, 17, 18), een leeftijd precies op de grens tussen twee
categorieën, en een gezelschap van 4 personen met een baby erbij.

{% next "Verder: klaar!" %}

## Klaar

Je bent klaar als de knop **complexity** over `hangman.py` niets meer te klagen
heeft en de knop **compare** alle tests gelijk vindt. Heb je ook
`cinema.py` onder de 3 gekregen, dan heb je het extra werk ook gedaan.

Wat je hier geleerd hebt, kan je op al je eigen programma's toepassen. Draai de
knop **complexity** eens op een programma dat je eerder hebt ingeleverd, en kijk
waar hij aanwijst dat het ingewikkeld wordt. Vaak is dat precies de plek waar je zelf de
weg kwijtraakt als je je code een week later weer openslaat.
