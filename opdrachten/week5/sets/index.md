# Sets

De "set" is wederom een collectie-datatype, waarmee je meerdere elementen samen in één variabele op kunt slaan. Net als tuples lijken sets nogal op lijsten, want ook hier kun je diverse losse elementen opslaan.

Sets zijn gebaseerd op het principe van verzamelingen, waarin hetzelfde gegeven *niet* meermaals kan voorkomen. Items in een set moeten bovendien immutable zijn, zoals de keys van een dictionary. Dit zorgt ervoor dat sets vooral heel goed zijn in bepalen of een element **in** de collectie zit of niet.

## Video

Bekijk deze video om meer te leren over sets:

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_u96n1ef6&flashvars[streamerType]=auto&flashvars[localizationCode]=en_US&flashvars[leadWithHTML5]=true&flashvars[sideBarContainer.plugin]=true&flashvars[sideBarContainer.position]=left&flashvars[sideBarContainer.clickToClose]=true&flashvars[chapters.plugin]=true&flashvars[chapters.layout]=vertical&flashvars[chapters.thumbnailRotator]=false&flashvars[streamSelector.plugin]=true&flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&flashvars[dualScreen.plugin]=true&flashvars[hotspots.plugin]=1&flashvars[Kaltura.addCrossoriginToIframe]=true&&wid=0_1k2dy7ii)

## Uitleg

Het maken van een set kan worden gedaan met dezelfde accolades als bij een dictionary:

    >>> s = {'dit', 'is', 'een', 'set'}
    >>> s
    {'een', 'set', 'is', 'dit'}

Zoals je ziet zijn sets "ongeordend": de volgorde blijft niet per se behouden. De elementen in een set moeten bovendien uniek zijn, dus als we elementen proberen toe te voegen die al in de set zitten, dan zal de set nog steeds één kopie van elk element bevatten:

    >>> s.add('dit')
    >>> s.add('ook')
    >>> s.add('dit')
    >>> s
    {'is', 'set', 'een', 'dit', 'ook'}

## Ontdubbelen

De meest voorkomende toepassing van sets is het verwijderen van dubbele elementen.

    >>> lijst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    >>> lijst
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    >>> set(lijst)
    {1, 2, 3, 4, 5, 6, 9}
    >>> list(set(lijst))
    [1, 2, 3, 4, 5, 6, 9]

Het omzetten van een lijst naar een set zal dus de dubbele elementen verwijderen. En eventueel kun je de set terug omzetten naar een lijst, bijvoorbeeld als je de gegevens echt als list nodig hebt. 

Dit wordt over het algemeen beschouwd als de eenvoudigste manier om een lijst uniek te maken. Let op dat de volgorde in de lijst wel verandert, omdat sets ongeordend zijn, dus de oorspronkelijke volgorde van de lijst gaat verloren bij deze conversie.

## In

Zoals je misschien hebt opgemerkt delen sets veel eigenschappen met dictionaries. Net als dictionaries werken ze ook op basis van hashing. Daardoor is het controleren of een item onderdeel is een efficiënte operatie:

    >>> 'een' in s
    True

Ongeacht hoeveel elementen er in de set zitten zal het controleren of een element aanwezig is even snel zijn.

Het feit dat sets werken met hashing betekent ook dat ze alleen hashbare en dus onveranderbare (immutable) elementen kunnen bevatten, dus we kunnen geen lijst toevoegen als element:

    >>> s.add([3, 4])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

## Vereniging

Al dit efficiënt controleren of elementen in sets zitten, wordt ook gebruikt om de klassieke bewerkingen op verzamelingen efficiënt te maken. Bewerkingen zoals beschreven in de verzamelingenleer gaan over welke elementen worden gedeeld tussen twee sets.

Laten we beginnen met het maken van twee sets:

    >>> b = {3, 5, 7, 8, 12, 16, 21}
    >>> b = {16, 24, 21, 8, 9, 1, 2}
    >>> a
    {3, 5, 7, 8, 12, 16, 21}
    >>> b
    {1, 2, 8, 9, 16, 21, 24}

De eerste bewerking die we zullen bekijken is de union (vereniging), die een nieuwe set geeft met daarin de gecombineerde unieke elementen van beide sets.

    >>> a.union(b)
    {1, 2, 3, 5, 7, 8, 9, 12, 16, 21, 24}
    >>> a | b
    {1, 2, 3, 5, 7, 8, 9, 12, 16, 21, 24}
    >>> b | a
    {1, 2, 3, 5, 7, 8, 9, 12, 16, 21, 24}

We kunnen deze bewerking toepassen met de functie `.union()` of door de `|`-operator te gebruiken. Let op dat de volgorde van de twee originele set er niet toe doet, omdat de vereniging van `a` en `b` hetzelfde is als de vereniging van `b` en `a`.

## Doorsnede

Een andere operatie uit de verzamelingenleer is de doorsnede. Deze operatie construeert een nieuwe verzameling met daarin de unieke elementen die in *beide* sets voorkomen.

    >>> a.intersection(b)
    {8, 16, 21}
    >>> a & b
    {8, 16, 21}
    >>> b & a
    {8, 16, 21}

We kunnen de doorsnede toepassen met de functie `.intersection()` of door de `&` operator te gebruiken. Net als bij vereniging doet de volgorde tussen de originele sets er niet toe, omdat de doorsnede van `a` en `b` dezelfde is als de doorsnede van `b` en `a`.

## Verschil

Het verschil tussen twee sets:

    >>> a.difference(b)
    {3, 12, 5, 7}
    >>> a - b
    {3, 12, 5, 7}
    >>> b - a
    {24, 1, 2, 9}

Deze operatie geeft op basis van set `a` en `b` een nieuwe set met daarin alleen de elementen van `a` die *niet* aanwezig zijn in `b`. Merk op dat de volgorde van `a` en `b` hier wel degelijk uitmaakt voor het resultaat.

## Subsets

We kunnen controleren of sets deelverzamelingen danwel supersets van elkaar zijn. In dat geval bevat de ene set minstens alle elementen die in de andere voorkomen, of juist andersom.

    >>> c = a & b
    >>> c
    {8, 16, 21}
    >>> c.issubset(a)
    True
    >>> c <= a
    True
    >>> c.issuperset(a)
    False
    >>> c >= a
    False
    >>> a >= c
    True

Je ziet dat er wordt gewerkt met de functies `.issubset()` en `.issuperset()` of de operators `<=` en `>=`. Er zijn ook de `<` en `>` operators voor strikte deelverzamelingen, vooral als de twee sets niet gelijk mogen zijn.

# Oefenen met sets

> Als er een oefening is die je niet weet op te lossen, bekijk de theorie dan opnieuw. Als dat niet helpt, bespreek de oefening dan met een andere student en/of de leraar.

Test je begrip met de volgende oefeningen. Maak een bestand genaamd `sets.py` aan.

**Oefening 1** Maak twee sets `eersteSet` en `tweedeSet` met de getallen 23, 42, 65, 57, 78, 83, en 29, en 57, 83, 29, 67, 73, 43, en 48 respectievelijk.

**Oefening 2** Sla de intersectie van deze sets op in de variabele `derdeSet`. Maak een andere set `vierdeSet` die het verschil bevat tussen `eersteSet` en `tweedeSet`, dus alle elementen in `eersteSet` die niet in `tweedeSet` zitten.

**Oefening 3** Voeg het getal 67 toe aan `derdeSet`.

**Oefening 4** Controleer of `derdeSet` een subset is van `eersteSet` en als dat het geval is, print dan de tekst "subset!", print anders "geen subset".

**Oefening 5** Gegeven is de lijst hieronder met dubbele items genaamd `dubbelen`. Verwijder de dubbele elementen met behulp van een set en sla de oplossing op als een lijst in de variabele `unieken`.

    dubbelen = ["tennis", "badminton", "roeien", "voetbal", "tennis", "judo", "judo", "karate", "voetbal"]
    unieken = # Jouw oplossing hier
