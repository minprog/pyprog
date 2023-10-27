# Oefententamen

Het doel van dit tentamen is dat je kunt laten zien hoe breed en diep je kennis over programmeren in Python gaat. We kijken daarbij naar alle onderwerpen die zijn langsgekomen, maar zeker naar:

- Goed gebruik van type hints om vast te leggen wat de intentie is van het programma (week 1)
- Uitgebreid gebruik van doctests om zo scherp mogelijk te controleren of de code werkt (week 1)
- Sterke functionele decompositie (opdeling), in samenspel met goede namen voor functies (week 2)
- Goed gebruik van parameters om informatie door te geven binnen het programma (week 2)
- Zorgvuldig inlezen en verwerken van databestanden, en manipulatie van strings (week 5)
- Gebruik van ingebouwde Python-collections zoals list, dict, set, tuple (week 6)
- Gebruik van list comprehensions om bewerkingen van lijsten te doen in weinig code (week 6)
- Code opdelen in classes, met een duidelijke taak, die goed onderling samenwerken (week 7)
- Netheid van de code, naamgeving, layout, alles wat je bij code review geleerd hebt (week 1)

Het is aan jou om in je code te laten zien welke delen van het programmeren je beheerst. Daarvoor wordt alle **werkende** code die je hebt in z'n totaal beoordeeld. Je scoort een voldoende als je voldoende code werkend hebt gekregen en voldoende laat zien Python-constructies te beheersen.

Als voorbeeld: als je wil laten zien dat je list comprehensions beheerst, dan hoef je zeker niet in elke opdracht list comprehensions te gebruiken. Sommige opdrachten lenen zich beter voor gebruik van list comprehensions dan andere.

Een ander voorbeeld: je kunt Python goed beheersen zonder de stof van week 7 (classes) goed te kennen. Red je het niet om die stof tot je te nemen, dan kun je nog steeds zeer goede oplossingen schrijven voor de meeste (of zelfs alle) opdrachten.

Uitgangspunt is altijd dat wat je inlevert ook werkt, en dat types en doctests worden goedgekeurd in de automatische check. Alle code die je maakt moet getest worden. Wat je niet werkend krijgt moet je uitcommenten zodat de code die wél werkt goed getest kan worden.


## Hulp krijgen in Python

Bij dit tentamen gebruik je geen externe bronnen zoals websites, het boek of je oude code. Je mag wel gebruik maken van de hulpfunctie van Python om informatie op te zoeken.

- Start Python met het commando `python` of `python3`
- Heb je hulp nodig met een ingebouwde functie zoals `ord`? Tik dan in `help(ord)`
- Heb je hulp nodig met een ingebouwde methode zoals `str.startswith`? Tik dan in `help(str.startswith)`
- Wil je weten welke methodes worden ondersteund door een (ingebouwde) class zoals `dict`? Tik dan in `help(dict)`


## Niet gebruiken

Zorg dat je alleen constructies gebruikt die expliciet zijn behandeld in de cursus. Wat je op internet hebt gevonden is niet zomaar toegestaan. In ieder geval moet je geen reguliere expressies gebruiken en de meeste `import` libraries zijn off-limits (`import string` is prima).

Als je wil weten of iets mag, dan moet je dit niet vragen tijdens de les maar een mail sturen naar <python@proglab.nl> voor een officieel antwoord. Anders telt het niet.


## Controleren van je eigen werk

Het allerbelangrijkste is dat je met hulp van doctests aantoont dat je geschreven functies en classes goed werken. Alleen dan kan er een beoordeling plaatsvinden.

- Een typecheck kun je starten met `mypy --strict --ignore-missing-imports programma.py`.
- Doctests kun je starten met `python3 -m doctest -v programma.py`.

Zorg dat je deze tools geinstalleerd hebt en weet hoe je ze moet runnen. Zorg ook dat je je computer niet upgrade vlak voor het tentamen! :-)

Je mag ook testcode schrijven naast de doctests, maar deze testcode **moet** in `if __name__ == '__main__'` staan. Bij de beoordeling baseren we ons op de doctests.


## Submit in één bestand

Je moet alle code in één bestand zetten. Zorg dat je de verschillende uitwerkingen markeert met het volgende comment, waarbij je een korte name/samenvatting van het probleem invult:

    # -------------------------------------------------------------------------
    # Opdracht: <naam van opdracht(en)>


## Opdrachten

De opdrachten hieronder zijn enigszins los beschreven. Je kunt daarom soms zelf kiezen hoe je een zin in een opdracht interpreteert, als je maar voldoende interessante code kunt schrijven om het probleem op te lossen.


## Vakantie

*Minimale ingrediënten: expressies en ifs (deze opdracht is echt om even in te komen, want je kunt er maar heel weinig Python-kennis mee demonstreren)*

Je wil in je eentje op vakantie naar een mooie accommodatie in Frankrijk. De kosten van de reis naar het verblijf zijn afhankelijk van het gebruikte vervoersmiddel. Met het vliegtuig kost het je 250 euro, met de trein kost het 100 euro, en met de auto kost het 150 euro. Het verblijf zelf kost 60 euro per nacht. Bovendien betaal je nog 3% servicekosten over de totale kosten (dus vermenigvuldig totaal met 0.03), afhankelijk dus van hoeveel nachten je verblijft. De servicekosten worden wel naar **beneden** afgerond op hele euro's vóórdat ze bij het totaalbedrag worden opgeteld!

Schrijf een functie die berekent hoeveel je vakantie kost op basis van het aantal dagen dat je op vakantie gaat en met welk vervoersmiddel je gaat. Voor het vervoersmiddel kun je een string accepteren, bijvoorbeeld 'vliegtuig' of afgekort 'v'.

Als voorbeeld: 1 nacht, reizen met vliegtuig is 319 euro. 10 nachten, reizen met trein is 721 euro.


## Hoofdletters

*Minimale ingrediënten: loops, ifs, string indexing, string-functies (deze opdracht is echt om even in te komen, want je kunt er vrij weinig Python-kennis mee demonstreren)*

Tekstanalyse is een veelgebruikte toepassing. Hoewel dit vaak gebeurt op basis van technieken uit de AI, kunnen eenvoudige statistieken soms heel verhelderend zijn.

Schrijf een functie die telt hoeveel woorden in een tekst met een hoofdletter beginnen. De functie returnt het aantal als een `int`.

- "Er zijn geen goede schrijvers." -> 1 woord begint met een hoofdletter
- "Obi-Wan Kenobi nam zijn taak vrij serieus" -> 2 woorden beginnen met een hoofdletter
- "bell hooks wrote on race, feminism and class." -> geen woorden beginnen met een hoofdletter


## Email-validator

*Minimale ingrediënten: loops, ifs, string indexing en/of slicing, string-functies (met deze opdracht heb je al meer mogelijkheden om je Python-kennis te demonsteren)*

Mensen hebben nogal eens de neiging om een niet-bestaande waarde in te voeren in de computer, bijvoorbeeld als om hun mailadres gevraagd wordt. Of ze begrijpen het gewoon niet.

Daarom gebruiken websites vaak een email-validator om te controleren of de invoer **redelijk OK** is. Zo'n validator is niet gegarandeerd compleet, maar voorkomt een aantal fouten.

Schrijf een email-validator-functie, ten minste op basis van de volgende regels:

- Er moet een `@` in zitten
- Vóór de `@` moet minstens één letter staan (A-Z of a-z)
- Na de `@` moet tenminste één `.` staan.

Test ook met vreemdere fouten (is `@` een geldig mailadres? nee).


## Strings & Files

*Minimale ingrediënten: loops, ifs, string indexing en/of slicing, string-functies, files*

-   Schrijf een functie die bepaalt of argument `string1` een prefix is van argument `string2`. Gebruik geen bestaande string-functies of -methoden behalve de mogelijkheid om te indexeren.

-   Schrijf een functie die voor een willekeurig opgegeven bestand de *checksum* berekent. De checksum is de optelsom van alle characters in het bestand. Gebruik de ingebouwde Python-functie `ord()` om de waarde van een letter te berekenen; zo is `ord('B')` gelijk aan `66`.

-   Schrijf een functie die het aantal tekens, woorden en regels in een opgegeven file telt en teruggeeft.

-   Elk uur werd er een meting gedaan van het C02-gehalte in de lucht in een programmeerlokaal op het Science Park. Deze metingen zijn opgeslagen in `C02.txt`. Dit bestand bevat twee kolommen aan data. De eerste kolom is het uur van de meting, en de tweede kolom het ppm (parts per million) C02 in de lucht. Na tien metingen ziet `C02.txt` er zo uit:

        0,512
        1,640
        2,593
        3,580
        4,581
        5,613
        6,840
        7,889
        8,863
        9,891

    Schrijf enkele functies die 1) een lijst van meetwaardes kunnen geven 2) het gemiddelde van de meetwaardes kan geven 3) het uur van de grootste stijging in meetwaarde kan geven.

    Een mogelijk beter alternatief voor losse functies is om een class te implementeren die al deze mogelijkheden biedt.

## Classes

*Minimale ingrediënten: loops, ifs, string-functies, classes, lijsten (oefen deze opdracht pas als je week 7 af hebt)*

-   Maak een class `SecretMessage` waarvan de initializer een geheime code en een geheime boodschap meekrijgt. Maak ook de methoden `open` (waarmee het met de juiste code geopend kan worden en de boodschap teruggeeft) en `changeCode` (waarmee de code aangepast kan worden; natuurlijk alleen als de juiste originele code wordt opgegeven).

-   Maak een class `Student`, waarin worden opgeslagen: naam, studentnummer en status. Status is het studiejaar van de student: mogelijkheden 1 t/m 4 (of hoger). Schrijf code om automatisch 20 studenten te genereren (genaamd "Student1" enzovoort) met random studentnummer en status (opslaan in een lijst!). Schrijf vervolgens code om alleen de eerstejaars hiervan uit te printen.


## Comprehensions

*Minimale ingrediënten: string-functies, lijsten, comprehensions (oefen deze opdracht pas als je week 6 af hebt)*

-   Gegeven een list met daarin integers, schrijf een functie die deze omzet in een string met alle getallen en daartussen komma's. De lijst `[1, 2, 3]` wordt de string `"1,2,3"`. Gebruik hiervoor een list comprehension.


## Users

*Minimale ingrediënten: string-functies, files, collections (oefen deze opdracht pas als je week 6 af hebt)*

Gegeven het volgende bestand `passwd` waarin gebruikersgegevens van een UNIX-systeem worden opgeslagen:

    nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
    root:*:0:0:System Administrator:/var/root:/bin/sh
    daemon:*:1:1:System Services:/var/root:/usr/bin/false
    joedoe:*:1000:1000:Joe Dough:/Users/joe:/bin/zsh

Zoals je ziet zijn de kolommen (fields) geschreven door dubbele punten. De kolommen zijn als volgt beschreven:

1. De username
2. Het wachtwoord (dit is altijd `*`)
3. Het user id
4. Het group id
5. De naam of omschrijving van de gebruiker
6. De home directory
7. De gebruikte shell

De volgende opdrachten zijn gebaseerd op zo'n wachtwoorden-bestand.

1. Schrijf een functie `load()` die de naam van het bestand aanneemt, en een `dict` oplevert waarin de keys de username zijn en de values steeds een lijst met daarin de overige gegevens van de gebruiker.

2. Schrijf een functie `users()` die de user dict meekrijgt en een lijst teruggeeft met daarin de alleen usernames van alle gebruikers.

3. Schrijf een functie `priviliged_users()` die de user dict meekrijgt en een lijst teruggeeft met daarin de usernames van geprivilegieerde gebruikers (die hebben een user id tussen 0 en 100, inclusief).

4. Schrijf een functie `chpass()` die de user dict meekrijgt, een username, het wachtwoord van die user, en een nieuw wachtwoord. Als username en oude wachtwoord kloppen dan wordt het wachtwoord veranderd naar het nieuwe wachtwoord.

5. Schrijf een functie `chsh()` die de user dict meekrijgt, een username en een nieuwe shell. De shell van de user wordt veranderd naar de opgegeven waarde. Er moet wel eerst gecontroleerd worden of de nieuwe shell voorkomt in een lijst van toegestane shells (deze lijst kun je zelf definiëren gebaseerd op de voorbeelden in het bestand hierboven).

Uitbreidingsmogelijkheden (met deze uitbreidingen kun je laten zien dat je een bepaald deel van Python beheerst, zoals het gebruik van classes; het zijn maar ideeën):

1. Gebruik een dict met de username als key, en daarbij als value ook weer een dict met de overige gegevens van de gebruiker.

2. Gebruik een class `User` waarin alle eigenschappen van één gebruiker staan en de lijst gebruikers is een dict waarin steeds een username gekoppeld is aan een User object.

3. Gebruik een `User` class en maak ook een `UserList` class waarin alle `User`-instanties worden opgeslagen. Alle hierboven geschreven functies moeten worden geïmplementeerd als methods van die classes, in plaats van als losse functies.


## Afronding

Vergeet niet je doctests goed te schrijven zodat zichtbaar is dat alles werkt, en vergeet niet om alle relevante type hints te plaatsen zodat `mypy` tevreden is!


## Nakijken en analyseren

Als je zelf de opdrachten hebt geprobeerd (en nog eens geprobeerd) dan kun je je uitwerkingen vergelijking met de van ons. Maar er zijn vele uitwerkingen mogelijk! Ga dus niet leren dat je een vraag precies op onze manier (bijv. met dictionaries) moet doen. Analyseer de verschillen, kijk wat je goed begrijpt en bedenk welke oplossingsstrategiën voor jou persoonlijk handig zijn bij het tentamen.

- [Uitwerkingen deel 1](https://raw.githubusercontent.com/minprog/pyprog/2022/tentamen/oefententamen/voorbeelden-oefententamen1.py)
- [Uitwerkingen deel 2](https://raw.githubusercontent.com/minprog/pyprog/2022/tentamen/oefententamen/voorbeelden-oefententamen2.py)


## Meer oefenen

Heb je meer oefening nodig? Dan zijn er wellicht oude opdrachten die je eerder niet af hebt gekregen. Die kunnen nuttig zijn om nog uit te werken.
