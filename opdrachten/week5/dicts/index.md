# Dictionaries

De "dictionary" is een fundamentele datastructuur van Python. Samen met lijsten vallen ze onder de categorie van *collecties*: de datatypes waarmee je meerdere elementen samen in één variabele op kunt slaan.

Bij een list kun je een waarde opvragen door de index te gebruiken. Met dictionaries gaan we een stap verder: je kunt zelf een **key** (sleutel) kiezen waaronder je een waarde opslaat. Via de key krijg je efficiënt en direct toegang tot deze waarde.

## Video

Bekijk deze video om meer te leren over dictionaries:

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_80k74cvx&flashvars[streamerType]=auto&flashvars[localizationCode]=en_US&flashvars[leadWithHTML5]=true&flashvars[sideBarContainer.plugin]=true&flashvars[sideBarContainer.position]=left&flashvars[sideBarContainer.clickToClose]=true&flashvars[chapters.plugin]=true&flashvars[chapters.layout]=vertical&flashvars[chapters.thumbnailRotator]=false&flashvars[streamSelector.plugin]=true&flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&flashvars[dualScreen.plugin]=true&flashvars[hotspots.plugin]=1&flashvars[Kaltura.addCrossoriginToIframe]=true&&wid=0_zmx8rsom)

## Waarden opvragen

Het verschil tussen dictionaries en lijsten is dat we in plaats van een getal als index te gebruiken, een "key" of sleutel gebruiken om elementen op te zoeken. In plaats van een getal kun je bijvoorbeeld de string `'maandag'` gebruiken. Andere soorten keys zijn ook mogelijk.

Dat je zelf keys kunt kiezen is de belangrijkste reden waarom dictionaries zo vaak worden gebruikt. Door dit verschil kun je dictionaries gebruiken voor heel andere toepassingen dan lijsten. Bovendien zijn dictionaries zo geprogrammeerd dat het opvragen zeer efficiënt is.

Eén manier waarvoor we een dictionary kunnen gebruiken is een eenvoudig woordenboek. Een Nederlands-Spaans-woordenboek kun je zien als een lijst van associaties tussen Nederlandse en Spaanse woorden.

| Key (sleutel) | Value (waarde) |
| ------------- | -------------- |
| Ja            | Sí             |
| Nee           | No             |
| Alsjeblieft   | Por favor      |
| Dank je       | Gracias        |

Elk gegeven in een dictionary kun je ook een *key-value pair* noemen: een paar bestaande uit een sleutel (voor het opvragen) en een waarde.

Door de key te gebruiken kunnen we direct een Spaanse vertaling opzoeken in het woordenboek. In Python zou de dictionary er zo uitzien:

    >>> woordenboek = { 'Ja': 'Sí', 'Nee': 'No', 'Alsjeblieft': 'Por favor', 'Dank je': 'Gracias' }
    >>> woordenboek['Ja']
    Sí

De koppeling hier is van een string naar een andere string (de vertaling). Dit is een goed voorbeeld van hoe dictionaries in Python worden gebruikt. Laten we hieronder eens goed kijken naar  verdere syntax voor dictionaries in Python en enkele andere gevallen waarin we dictionaries kunnen gebruiken.

## Dictionaries maken

Een nieuw voorbeeld is een fruitmand waarin we bijhouden hoeveel van elke soort fruit aanwezig zijn. Het gebruik van dictionaries op deze manier, als een koppeling van elementen naar een telling (of een score), is nog zo'n manier om dictionaries te gebruiken.

    >>> mandje = {'appel': 4, 'banaan': 7, 'sinaasappel': 2}
    >>> mandje
    {'appel': 4, 'banaan': 7, 'sinaasappel': 2}

## Elementen ophalen

Als we willen weten hoeveel appels er in de fruitmand zitten, kunnen we weer schrijven:

    >>> mandje['appel']
    4

Hier hebben we de **key** `'appel'` gebruikt om de **value** `4` te vinden. Deze syntax lijkt erg op het gebruik van blokhaken om elementen uit een _lijst_ te halen, maar in plaats van de index te gebruiken om het element op te halen dat op die plaats in de lijst is opgeslagen, gebruiken we de key om de overeenkomstige waarde uit de dictionary op te halen.

## Items toevoegen

Een nieuw _key-value pair_ toevoegen gaat als volgt:

    >>> mandje['aardbei'] = 10
    >>> mandje
    {'appel': 4, 'banaan': 7, 'sinaasappel': 2, 'aardbei': 10}

We kunnen deze syntax ook gebruiken om een bestaand paar te wijzigen. Laten we zeggen dat we een van de bananen hebben gegeten, dan kunnen we de dictionary bijwerken door te schrijven

    >>> mandje['banaan'] -= 1
    >>> mandje
    {'appel': 4, 'banaan': 6, 'sinaasappel': 2, 'aardbei': 10}

Elke key in een dictionary moet **uniek** zijn, dus als we proberen een key toe te voegen die al bestaat, zullen we de overeenkomstige waarde *overschrijven*. Als we bijvoorbeeld een andere key voor appels proberen toe te voegen:

    >>> mandje['appel'] = 6
    >>> mandje
    {'appel': 6, 'banaan': 6, 'sinaasappel': 2, 'aardbei': 10}

Let daarnaast op de volgorde van de elementen: bij dictionaries blijft de volgorde behouden waarin items zijn ingevoegd, net zoals bij lijsten.

## Errors

Dictionaries werken alleen van key naar value werken, en niet andersom. Dit is zodat waarden niet uniek hoeven zijn. Maar dat betekent ook dat je niet kunt zoeken op waarde: dit zal een `KeyError` opleveren:

    >>> mandje[2]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 2

De key `2` bestaat niet in ons mandje. De value `2` komt natuurlijk wel voor in ons mandje, opgeslagen onder de key `'sinaasappel'`:

    >>> mandje['sinaasappel']
    2

Als we proberen het aantal mango's op te halen, die helemaal niet in de mand zitten, krijgen we ook een `KeyError`:

    >>> mandje['mango']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'mango'

## De get-methode

Het zou in ons voorbeeld handig zijn als je de waarde `0` krijgt als je zoekt op de naam van fruit dat niet in het mandje zit. Hiervoor kunnen we de functie `get()` gebruiken in plaats van de blokhaken. We geven dan als argument welke waarde we willen krijgen als de key niet aanwezig is in de dictionary:

    >>> mandje.get('mango', 0)
    0

Nu weten we dat onze fruitmand helaas `0` mango's bevat, en dat is handiger dan een foutmelding in deze situatie.

Als een item gewoon aanwezig is in de dictionary, gedraagt `get()` zich precies hetzelfde als de blokhaken:

    >>> mandje.get('appel', 0)
    6
    >>> mandje['appel']
    6

Het is ook belangrijk om te realiseren dat `get()` geen items aan de dictionary toevoegt. Na het gebruik van `get()` ziet het mandje er nog steeds hetzelfde uit:

    >>> mandje.get('mango', 0)
    0
    >>> mandje
    {'appel': 6, 'banaan': 6, 'sinaasappel': 2, 'aardbei': 10}

## De in-operatie

We kunnen vragen of een key *aanwezig* is in de dictionary met behulp van `in`:

    >>> if 'banaan' in mandje:
    ...   print("We hebben bananen!")
    ...
    We hebben bananen!

Dit werkt precies zoals bij lijsten. Maar wederom kun je alleen kijken of een *key* aanwezig is. Een *value* kun je zo niet vinden. Er is trouwens een belangrijk verschil tussen het gebruik van `in` met dictionaries en het gebruik van `in` met lijsten: bij dictionaries is `in` veel sneller.

## Itereren

Dictionaries worden voornamelijk gebruikt voor opzoekoperaties, maar soms je over alle elementen in de dictionary itereren. Dictionaries ondersteunen veel van dezelfde operaties als lijsten. Zo kun je bijvoorbeeld `len` gebruiken om te vragen hoeveel paren (key-value pairs) er aanwezig zijn:

    >>> len(mandje)
    4

We kunnen ook `for`-loops gebruiken met dictionaries:

    >>> for fruit in mandje:
    ...   print(fruit)
    ...
    appel
    banaan
    sinaasappel
    aardbei

Dit zal alleen over de keys van de dictionary itereren, maar we kunnen met elk van die keys eventueel de waarden ophalen:

    >>> for fruit in mandje:
    ...   print(fruit, mandje[fruit])
    ...
    appel 6
    banaan 6
    sinaasappel 2
    aardbei 10

We kunnen tot slot `items()` gebruiken om meteen de keys én de values te krijgen. Let op de syntax met de komma in de for-loop:

    >>> for fruit, hoeveelheid in mandje.items():
    ...   print(fruit, hoeveelheid)
    ...
    appel 6
    banaan 6
    sinaasappel 2
    aardbei 10

## Oefeningen

> Als er een oefening is die je niet weet op te lossen, bekijk de theorie dan opnieuw. Als dat niet helpt, bespreek de oefening met een andere student en/of de docent.

Maak een bestand genaamd `dictionaries.py`. Je hoeft geen functies te schrijven: het gaat hier om het oefenen met de operaties die je op dictionaries kunt toepassen.

**Oefening 1** Maak net als in de video een dictionary genaamd `mijn_klas` met studenten en cijfers. Gebruik de namen Ralph, Diana, Jordi, en Michele met hun respectievelijke cijfers: 4, 8, 7 en 5.

**Oefening 2** Voeg een student Gretel toe aan de bovenstaande dictionary met een cijfer 9. Print de dictionary `mijn_klas` om te controleren of Gretel inderdaad aan de dictionary is toegevoegd.

**Oefening 3** Schrijf een stuk code dat de gebruiker vraagt om een naam in te voeren en in de dictionary `mijn_klas` kijkt of de student bestaat. Print de boodschap "[naam] is een student in deze klas en heeft het cijfer: [cijfer]." of "[naam] is geen student in deze klas.", afhankelijk van of de student wel of niet in de dictionary `mijn_klas` staat. Voorbeeldgebruik:

    python dictionaries.py
    Voer een naam in: Jordi
    Jordi is een student in deze klas en heeft het cijfer: 7.

Gebruik de `in`-operator voor deze oefening. Gebruik geen `get()`.

**Oefening 4** Gebruik de volgende lijst studenten:

    studenten = ["Michele", "Diana", "Maria", "Ralph", "Jacobus"]

Schrijf een loop die elke student opzoekt in de `mijn_klas`-dictionary en dan voor elke student een regel print van het formaat "[naam]: [cijfer]". Als de student niet voorkomt in `mijn_klas` dan moet de naam gewoon geprint worden maar "n/a" voor het cijfer. Het ziet er dan zo uit:

    Michele: 5
    Diana: 8
    Maria: n/a
    Ralph: 4
    Jacobus: n/a

Gebruik `get()` en géén `if`-statement.
