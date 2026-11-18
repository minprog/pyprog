# Tutorial: Cyclomatic Complexity

Je programma's werken, maar werkende code is niet altijd *leesbare* code. In deze
tutorial leer je code herkennen die te ingewikkeld is en haal je die stap voor
stap uit elkaar. Als maat gebruik je de **Cyclomatic Complexity**: het aantal
verschillende routes door een stuk code.

**Hoe het werkt.** In de editor staan drie bestanden klaar: `hangman.py`,
`cinema.py` en `dictionary.txt`. Je hoeft dus niets te kopiëren. Je werkt aan
`hangman.py`; de bioscoop (`cinema.py`) is een extra opdracht voor als je tijd
over hebt.

Nieuw is de knop **complexity**. Die rekent voor het bestand dat je op dat
moment open hebt de Cyclomatic Complexity van elke functie uit, en klaagt over
elke functie die hoger uitkomt dan 3. Met de knop **run** draai je het
programma in de terminal.

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
        return "good"
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
Cyclomatic Complexity is te berekenen, en daar zit de knop **complexity** voor.
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
een woord uit `dictionary.txt`, jij raadt letter voor letter.

Klik op **run** en speel een spelletje. Kies een woordlengte tussen 3 en 10,
want zulke woorden staan in `dictionary.txt`.

Let goed op hoe de output eruit ziet: welke vragen het programma stelt, wat het
na elke gok print, en wat er aan het eind staat. Dit is ook precies hoe jouw
aangepaste programma moet blijven werken.

Lees daarna de code helemaal door. Je ziet dat alles in één grote functie staat,
met commentaarregels als scheiding tussen de onderdelen. Die commentaarregels
zijn een hint: waar de programmeur een kopje nodig had om uit te leggen wat er
gebeurt, zit vaak een functie verstopt.

{% next "Verder: de opdracht" %}

## 5. De opdracht

Aan jou de taak om `hangman.py` zo te verbeteren dat geen enkele functie een
Cyclomatic Complexity hoger dan 3 heeft. De knop **complexity** mag dus niet
meer klagen.

Dat kan op twee manieren:

1. De code opbreken in kleinere functies.
2. De code zelf eenvoudiger maken, zodat er minder routes mogelijk zijn.

De spelregels:

* De output van het programma moet **exact** hetzelfde blijven, inclusief alle
  teksten en leestekens.
* Alle code blijft in één bestand: `hangman.py`.
* Alle code mag worden gewijzigd.
* Geen enkele functie mag een Cyclomatic Complexity hoger dan 3 hebben.
* De type hints moeten blijven kloppen. Klik af en toe op **typecheck**.

En de werkwijze, want dit is het belangrijkste van de hele tutorial: werk **één
functie per keer**. Haal een stukje code uit `hangman_game`, zet het in een
eigen functie, roep die functie aan op de plek waar de code stond, en draai het
programma om te kijken of het nog hetzelfde doet. Pas daarna ga je verder met
het volgende stukje. Als je in één keer alles verbouwt, weet je bij een fout
niet meer waar die zit.

{% next "Verder: de eerste functie" %}

## 6. Stap 1: vragen om invoer

Begin bovenaan. Het programma vraagt om een woordlengte en blijft vragen tot het
antwoord klopt:

```
    word_length = int(input("What length of word would you like to play with?\n"))
    while word_length > 44 or word_length <= 0:
        word_length = int(input("Invalid word length! Please enter a length between 1 and 44.\n"))
```

Dat zijn vier regels die samen één ding doen: een geldig getal ophalen. Zet ze
in een eigen functie en roep die aan:

```
def ask_word_length() -> int:
    word_length = int(input("What length of word would you like to play with?\n"))
    while word_length > 44 or word_length <= 0:
        word_length = int(input("Invalid word length! Please enter a length between 1 and 44.\n"))
    return word_length
```

In `hangman_game` blijft dan één regel over:

```
    word_length = ask_word_length()
```

Let op twee dingen. De teksten in de `input`-aanroepen laat je precies staan
zoals ze waren, anders verandert de output. En de `while`-loop is nu uit
`hangman_game` verdwenen, dus de score van `hangman_game` gaat met 1 omlaag.

Doe dit nu zelf, draai het programma, en klik daarna op **complexity**. Je
hoort te zien dat `hangman_game` nog steeds te complex is, maar met een lager
getal dan 17. De nieuwe functie `ask_word_length` heeft een Cyclomatic
Complexity van 2 en is dus prima.

{% next "Verder: nog een keer vragen" %}

## 7. Stap 2: hetzelfde patroon herkennen

Iets verderop staat bijna dezelfde code, nu voor het aantal pogingen:

```
    number_guesses = int(input("How many guesses are allowed?\n"))
    while number_guesses <= 0:
        number_guesses = int(input("Negative or zero guesses make no sense.\n"))
```

Maak hier ook een functie van, bijvoorbeeld `ask_number_guesses`. Draai het
programma en meet opnieuw.

Je ziet nu twee functies die hetzelfde *patroon* hebben: vraag iets, blijf
vragen zolang het antwoord niet klopt, geef het antwoord terug. Alleen de
teksten en de voorwaarde verschillen. Later, bij de bioscoop, kom je daar op
terug: zulke herhaling kan je vaak samenvoegen in één functie met parameters.
Hier mag je het ook gewoon twee losse functies laten.

{% next "Verder: het woordenboek" %}

## 8. Stap 3: de woorden inlezen

Het volgende blok leest het woordenboek in en houdt alleen de woorden van de
juiste lengte over:

```
    words: set[str] = set()
    with open('dictionary.txt', "r") as file:
        for line in file:
            word = line.rstrip()
            if len(word) == word_length:
                words.add(word)
```

Hier zitten een `for` en een `if` in, dus dit blok is alleen al 3 routes waard.
Dat is precies het soort stuk dat je wil wegzetten in een eigen functie.

De functie heeft `word_length` nodig om te weten welke woorden hij moet houden,
en levert de woorden op. Het begin ziet er dus zo uit:

```
def load_words(word_length: int) -> set[str]:
    ...
```

Schrijf deze functie, roep hem aan in `hangman_game`, en draai het programma.
Meet opnieuw. `load_words` zelf komt uit op 3: precies op de grens, dus de knop
**complexity** klaagt er niet over.

{% next "Verder: het patroon printen" %}

## 9. Stap 4: het woord met strepen

Nu de binnenkant van het spel. Na elke gok bouwt het programma de weergave van
het woord op: de letters die geraden zijn en een `_` voor de rest.

```
            current_pattern = ''
            for letter in word:
                if letter in correct_guesses:
                    current_pattern += letter
                else:
                    current_pattern += '_'
            print(current_pattern)
```

Dit is een mooi voorbeeld van een functie die je een naam kan geven die uitlegt
wat er gebeurt. Maak een functie die van een woord en de geraden letters de
weergave maakt:

```
def pattern(word: str, correct_guesses: set[str]) -> str:
    ...
```

Merk op dat de `print` buiten de functie blijft. De functie *maakt* de tekst,
`hangman_game` *laat hem zien*. Zo kan je de functie ook los testen, zonder het
hele spel te spelen: er bestaat precies één goed antwoord per invoer.

Schrijf de functie en gebruik hem in het spel:

```
            print(pattern(word, correct_guesses))
```

Draai het spel en controleer of de strepen er nog precies zo uitzien als
eerst.

{% next "Verder: is het woord geraden?" %}

## 10. Stap 5: tweemaal dezelfde vraag

Twee keer in het programma staat bijna letterlijk dezelfde code, één keer in de
spel-loop en één keer aan het eind:

```
            guessed_all = True
            for letter in word:
                if letter not in correct_guesses:
                    guessed_all = False
                    break
```

Dat stuk beantwoordt een vraag met ja of nee: zijn alle letters van het woord
geraden? Zo'n functie geeft een `bool` terug:

```
def is_guessed(word: str, correct_guesses: set[str]) -> bool:
    ...
```

Dit stuk kan ook korter dan het origineel. Je hebt de variabele `guessed_all`
niet nodig: zodra je een letter vindt die niet geraden is, weet je het antwoord
al en mag je meteen `return False` doen. Na de loop weet je dat alle letters
geraden zijn, dus dan `return True`. Zo verdwijnt de `break` en houd je een
`for` met een `if` over: een score van 3.

Vervang nu beide plekken door een aanroep van `is_guessed`. Let op de
tweede plek, aan het eind van het spel: daar staat

```
        if guessed_all:
            print("Whoa, you won!!!")
```

en dat wordt

```
        if is_guessed(word, correct_guesses):
            print("Whoa, you won!!!")
```

Draai het spel, win een keer en verlies een keer, en meet opnieuw.

{% next "Verder: de rest" %}

## 11. Stap 6: de rest van het spel

Nu komt het stuk dat je zelf moet uitzoeken. Klik op **complexity** en kijk
hoeveel `hangman_game` nog is. Waarschijnlijk zit je nog boven 3, want de
functie bevat nog steeds: de buitenste `while True`, de loop die om letters
vraagt, de controle op een geldige letter, en de `if`/`else` voor een goede of
foute gok.

Zoek de groepen die bij elkaar horen. Een paar vragen om je op weg te helpen:

* Het vragen om één letter is weer datzelfde patroon van "vraag tot het klopt".
  Welke informatie heeft dat stukje nodig, en wat levert het op?
* Het verwerken van één gok (is de letter goed, wat wordt er geprint, gaat het
  aantal pogingen omlaag) is een afgerond stukje werk.
* Eén heel spel spelen is ook een afgerond stukje werk. Als `play_game` één spel
  speelt, wat blijft er dan nog over in `hangman_game`?
* Ook het slot van het spel, waar "gewonnen" of "verloren" geprint wordt, kan
  een eigen functie zijn.

Een paar dingen om op te letten:

* Een functie met een loop én een `if` erin zit al snel op 3. Zit je erboven,
  dan moet er nog een stukje uit.
* Functies die iets aanpassen aan een `set` die ze meekrijgen (zoals
  `guesses.add(letter)`) werken gewoon: de aanroeper ziet die verandering. Maar
  een `int` zoals `current_guesses` werkt niet zo. Als een functie dat aantal
  verlaagt, moet je het nieuwe aantal `return`'en en in de aanroeper weer
  opslaan.
* Blijf na elke stap het spel draaien. Je hebt de output van het originele
  programma gezien; er mag niets veranderd zijn.

Werk door tot de knop **complexity** niets meer te klagen heeft.

{% next "Verder: hangman klaar" %}

## 12. Hangman klaar

Klik nog één keer op **complexity** en op **typecheck**. Als er geen klachten
meer zijn, is `hangman.py` af.

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

## 13. Extra: de bioscoop

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
hints.

{% next "Verder: hints voor de bioscoop" %}

## 14. Hints voor de bioscoop

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

**Testen.** Test de randgevallen: een ongeldige dag, een uur dat net op de grens
zit (11, 12, 17, 18), een leeftijd precies op de grens tussen twee categorieën,
en een gezelschap van 4 personen met een baby erbij.

{% next "Verder: klaar!" %}

## Klaar

Je bent klaar als de knop **complexity** over `hangman.py` niets meer te klagen
heeft en het spel nog precies hetzelfde doet als in het begin. Heb je ook
`cinema.py` onder de 3 gekregen, dan heb je het extra werk ook gedaan.

Wat je hier geleerd hebt, kan je op al je eigen programma's toepassen. Draai de
knop **complexity** eens op een programma dat je eerder hebt ingeleverd, en kijk
waar hij aanwijst dat het ingewikkeld wordt. Vaak is dat precies de plek waar je zelf de
weg kwijtraakt als je je code een week later weer openslaat.
