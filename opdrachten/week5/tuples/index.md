# Tuples

Ook de "tuple" is een collectie-datatype, dus een manier om meerdere elementen samen in één variabele op te slaan.

De belangrijkste eigenschap van een tuple is dat je de inhoud niet kunt veranderen nadat de tuple is aangemaakt. De tuple is **immutable**, net zoals een string. Verder lijkt een tuple behoorlijk op een list.

## Video

Bekijk deze video om meer te leren over tuples:

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_wlxgk3ja&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_dztdpgtv)

## Uitleg

Tuples lijken sterk op lijsten omdat je ze gebruikt om rijtjes van elementen op te slaan. Ze worden vaak op een heel andere manier gebruikt.

Doordat tuples immutable (onveranderlijk) zijn ondersteunen ze enkele operaties die lijsten niet ondersteunen en andersom. We zullen dieper ingaan op dit verschil door naar enkele voorbeelden te kijken.

Een tuple maken lijkt erg op het maken van een lijst, behalve dat we ronde haken gebruiken in plaats van blokhaken:

    >>> t = (42, 'hello', 3.1415)
    >>> t
    (42, 'hello', 3.1415)

We kunnen elementen uit een tuple opvragen via een index, net als bij een lijst:

    >>> t[1]
    'hello'

Maar wanneer we proberen een waarde toe te kennen via een index, zoals bij een lijst, krijgen we een foutmelding.

    >>> t[1] = 9
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

Dit is het eerste teken dat de tuple inderdaad onveranderlijk is; het is niet mogelijk om een waarde op een specifieke index te wijzigen. Daarnaast kunnen we ook geen dingen aan het eind van een tuple toevoegen met `append`:

    >>> t.append('world')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'tuple' object has no attribute 'append'

Kortom, zodra een tuple is gemaakt kunnen we de inhoud niet meer veranderen. Dit is wat "immutable" betekent; het *kan niet worden gewijzigd*.

Met al deze beperkingen lijkt het misschien alsof een tuple veel minder doet dan een lijst, maar immutability heeft ook enkele voordelen.

## Packing

Een van de meest voorkomende manieren waarop een tuple wordt gebruikt, is door meerdere waarden vanuit een functie terug te geven.

    >>> def find_max_index(l):
    ...     max_ind = 0
    ...     max_val = 0
    ...     for i in range(len(l)):
    ...         if l[i] > max_val:
    ...             max_val = l[i]
    ...             max_ind = i
    ...     
    ...     return (max_ind, max_val)
    ...
    >>> list_of_values = [4.14, 8.1, 9.7, 2.0]
    >>> find_max_index(list_of_values)
    (2, 9.7)

Deze functie probeert de maximale waarde in een lijst te vinden. De functie geeft niet alleen de maximale waarde terug, maar daarbij ook de index van die maximale waarde. Beide waarden worden samen teruggegeven in een tuple.

Als je meerdere dingen combineert met komma's ertussen, worden ze automatisch een tuple, zelfs zonder de ronde haken eromheen. Dit wordt *tuple-packing* genoemd. De laatste regel van de functie had dus ook kunnen zijn `return max_ind, max_val`. Dat is ook de vorm die je vaker zult zien.

## Unpacking

We kunnen zien dat hetzelfde ook omgekeerd werkt, bij het toewijzen aan variabelen. Hier wijzen we in slechts 1 regel toe aan 2 nieuwe variabelen, `maximum_index` en `maximum_value`:

    >>> maximum_index, maximum_value = find_max_index(list_of_values)
    >>> maximum_index
    2
    >>> maximum_value
    9.7

Dit wordt *tuple-unpacking* genoemd en wijst de waarden uit de tuple toe aan de variabelen in dezelfde volgorde als waarin ze in de tuple stonden.

Het aantal elementen moet precies overeenkomen met hoeveel variabelen je probeert uit te pakken:

    >>> t
    (42, 'hello', 3.1415)
    >>> a, b = t
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: too many values to unpack (expected 2)
    >>> a, b, c, d = t
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: not enough values to unpack (expected 4, got 3)
    >>> a, b, c = t
    >>> a
    42

Bij het uitpakken van een tuple moet het aantal elementen exact overeenkomen en geven we elk element een andere variabelenaam. 

## Keuze tussen lijst en tuple

Bovenstaande zou je al een idee moeten geven van het gebruik van tuples ten opzichte van lijsten. 

Als we een groot aantal items van *hetzelfde type* hebben dan zou je ze in een lijst opslaan. Op die manier kun je nieuwe elementen toevoegen, over elk element loopen en ze allemaal op dezelfde manier verwerken.

Als je een klein aantal items bij elkaar wilt opslaan, ongeacht het type, dan zou je een tuple gebruiken. Je kunt deze items dan gezamenlijk retourneren, doorgeven aan een functie of zelfs meerdere verschillende tuples in een lijst opslaan.

## Hashing

Er is nog één andere belangrijke toepassing van tuples die we nog niet hebben besproken. "Hashing" is de onderliggende magie die dictionaries zo efficiënt maakt.

In de uitleg over dictionaries hebben we gesproken over het feit dat opzoeken via keys een zeer efficiënte operatie is. Dat komt omdat de keys van een dictionary via een *hash-functie* worden omgezet naar een getal, waarmee direct de juiste plek in de dictionary gevonden kan worden.

Keys mogen alleen bestaan uit waarden die immutable zijn. Lijsten zijn mutable (de losse elementen zijn aanpasbaar), en als je probeert een lijst te gebruiken als key dan krijg je een foutmelding:

    >>> phonebook = {}
    >>> john = ['John', 'Smith']
    >>> phonebook[john] = 5551234
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

In dit voorbeeld proberen we een telefoonboek te maken waarin we iemand kunnen opzoeken op basis van hun voornaam en achternaam, en hun telefoonnummer terug kunnen krijgen. Maar door de voornaam en achternaam samen in een lijst op te slaan, hebben we mutable type (een list) gebruikt.

Als we deze key veranderen naar een tuple dan kunnen we toch de twee namen samen als sleutel gebruiken:

    >>> john = tuple(john)
    >>> john
    ('John', 'Smith')
    >>> phonebook[john] = 5551234
    >>> phonebook
    {('John', 'Smith'): 5551234}

Enkele losse waarden samen opslaan als een sleutel in een dictionary is vrij gebruikelijk in Python-code. Dit is nog zo'n toepassing waar tuples essentieel zijn.
