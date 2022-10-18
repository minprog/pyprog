# Tentamen

Het doel van dit tentamen is dat je kunt laten zien hoe breed en diep je kennis over programmeren in Python gaat. We kijken daarbij naar alle onderwerpen die zijn langsgekomen, maar vooral naar:

- Sterke functionele decompositie (opdeling) in samenspel met goede namen voor functies
- Goed gebruik van variabelen en parameters om informatie door te geven binnen het programma
- Gebruik van type hints om vast te leggen wat de intentie is van het programma
- Gebruik van doctests om zo scherp mogelijk te controleren of de code werkt
- Gebruik van ingebouwde Python-collections zoals list, dict, set, tuple
- Zorgvuldig inlezen en verwerken van databestanden en manipulatie van strings
- Gebruik van list comprehensions om bewerkingen van lijsten te doen in weinig code
- Code opdelen in classes, met een duidelijke taak, die goed onderling samenwerken

Je hoeft zeker niet alles "perfect" toe te passen om een voldoende te halen voor het tentamen. Het moet vooral duidelijk worden dat je over voldoende niveau beschikt om binnen redelijke tijd werkende code te schrijven en dat je de juiste basiskennis hebt opgebouwd over Python-onderdelen. Zo kun je goed verder met de volgende vakken waarin geprogrammeerd wordt.

## Hulp krijgen in Python

Bij dit tentamen gebruik je geen externe bronnen zoals websites, het boek of je oude code. Je mag wel gebruik maken van de hulpfunctie van Python om informatie op te zoeken.

- Start Python met het commando `python` of `python3`
- Heb je hulp nodig met een ingebouwde functie zoals `ord`? Tik dan in `help(ord)`
- Heb je hulp nodig met een ingebouwde methode zoals `str.startswith`? Tik dan in `help(str.startswith)`
- Wil je weten welke methodes worden ondersteund door een (ingebouwde) class zoals `dict`? Tik dan in `help(dict)`

## Checks

- Een typecheck kun je starten met `mypy --strict --ignore-missing-imports programma.py`.
- Doctests kun je starten met `python -m doctest -v programma.py`.

## Submit in één bestand

Je moet alle code in één bestand zetten. Zorg dat je de verschillende uitwerkingen markeert met het volgende comment, waarbij je een korte name/samenvatting van het probleem invult:

    # -------------------------------------------------------------------------
    # Problem: <naam van probleem>

## Strings & Files

-   Schrijf een functie die bepaalt of argument `string1` een prefix is van argument `string2`. Gebruik geen bestaande string-functies of -methoden behalve de mogelijkheid om te indexeren.

-   Schrijf een functie die voor een willekeurig opgegeven bestand de *checksum* berekent. De checksum is de optelsom van alle characters in het bestand. Gebruik de ingebouwde Python-functie `ord(a)` om de waarde van een letter te berekenen; zo is `ord('B')` gelijk aan `66`.

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

    Schrijf enkele functies die 1) een lijst van meetwaardes kunnen geven 2) het gemiddelde van de meetwaardes kan geven 3) het uur van de grootste stijging in meetwaarde kan geven. Een beter alternatief voor losse functies is om een class te implementeren die al deze mogelijkheden biedt.

## Classes

-   Maak een class `SecretMessage` waarvan de initializer een geheime code en een geheime boodschap meekrijgt. Maak ook de methoden `open` (waarmee het met de juiste code geopend kan worden en de boodschap teruggeeft) en `changeCode` (waarmee de code aangepast kan worden; natuurlijk alleen als de juiste originele code wordt opgegeven).

-   Maak een class `Student`, waarin worden opgeslagen: naam, studentnummer en status. Status is het studiejaar van de student: mogelijkheden 1 t/m 4 (of hoger). Schrijf code om automatisch 20 studenten te genereren (genaamd "Student1" enzovoort) met random studentnummer en status. Schrijf vervolgens code om alleen de eerstejaars hiervan uit te printen.

## Comprehensions

-   Gegeven een list met daarin integers, schrijf een functie die deze omzet in een string met alle getallen en daartussen komma's. De lijst `[1, 2, 3]` wordt de string `"1,2,3"`. Gebruik hiervoor een list comprehension.

## Types & Collections

-   Wat wordt er geprint na het uitvoeren van dit stukje code?

        data = [1,2,3,1,2,1,2,3]
        x = {}
        for datum in data:
            if datum in x:
                x[datum] += 1
            else:
                x[datum] = 1
        print(x)

-   Het volgende stukje code geeft een error. Hoe kan je ervoor zorgen dat in variabele `S` de door de gebruiker ingevoerde string komt te staan, met als eerste letter een "C"?

        >>> S = input("What is your name?")
        Jasper
        >>> S[0] = "C"
        TypeError: ’str’ object does not support item assignment

## Case study

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

Uitbreidingsmogelijkheden:

1. Gebruik een dict met de username als key, en daarbij als value ook weer een dict met de overige gegevens van de gebruiker.

2. Gebruik een class `User` waarin alle eigenschappen van één gebruiker staan en de lijst gebruikers is een dict waarin steeds een username gekoppeld is aan een User object.

3. Gebruik een `User` class en maak ook een `UserList` class waarin alle `User`-instanties worden opgeslagen. Alle hierboven geschreven functies moeten worden geïmplementeerd als methods van die classes, in plaats van als losse functies.

## Afronding

Vergeet niet je doctests zo goed mogelijk te schrijven en alle relevante type hints te plaatsen! 
