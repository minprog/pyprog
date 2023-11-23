# Sets

Sets zijn een efficiënte manier om een verzameling unieke elementen op te slaan en zijn nauw verwant aan dictionaries. Net als dictionaries zijn het verzamelingen *zonder volgorde* en vereisen ze dat alle opgeslagen elementen te "hashen" zijn. Sets slaan echter alleen losse elementen op en maken geen koppeling tussen keys en values zoals een dictionary. In plaats daarvan ondersteunen ze enkele andere veelvoorkomende operaties zoals de doorsnede.

Leer meer over sets met deze video:

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_u96n1ef6&flashvars[streamerType]=auto&flashvars[localizationCode]=en_US&flashvars[leadWithHTML5]=true&flashvars[sideBarContainer.plugin]=true&flashvars[sideBarContainer.position]=left&flashvars[sideBarContainer.clickToClose]=true&flashvars[chapters.plugin]=true&flashvars[chapters.layout]=vertical&flashvars[chapters.thumbnailRotator]=false&flashvars[streamSelector.plugin]=true&flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&flashvars[dualScreen.plugin]=true&flashvars[hotspots.plugin]=1&flashvars[Kaltura.addCrossoriginToIframe]=true&&wid=0_1k2dy7ii)

Laten we eens kijken naar enkele sets in de praktijk.

Het maken van een set kan worden gedaan met dezelfde accolades als bij een dictionary:

    >>> s = {'dit', 'is', 'een', 'set'}
    >>> s
    {'een', 'set', 'is', 'dit'}

Zoals je ziet, zijn sets ongeordend, net als dictionaries. De elementen in een set moeten ook uniek zijn, dus als we elementen proberen toe te voegen die al in de set zitten,

    >>> s.add('dit')
    >>> s.add('ook')
    >>> s.add('dit')
    >>> s
    {'is', 'set', 'een', 'dit', 'ook'}

zal de set nog steeds slechts één kopie van elk van die elementen bevatten.

De meest voorkomende toepassing voor sets is het maken van een verzameling unieke elementen door ze om te zetten naar een set.

    >>> l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    >>> l
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    >>> set(l)
    {1, 2, 3, 4, 5, 6, 9}
    >>> list(set(l))
    [1, 2, 3, 4, 5, 6, 9]

Dus, het omzetten van een lijst naar een set zal eventuele duplicaatelementen verwijderen. Je kunt vervolgens de set terug omzetten naar een lijst als je de gegevens in lijstvorm nodig hebt in plaats van als een set. Dit wordt over het algemeen beschouwd als de eenvoudigste manier om een lijst uniek te maken. Let op dat de volgorde in de lijst wel verandert, omdat sets ongeordend zijn, dus de oorspronkelijke volgorde van de lijst gaat verloren bij deze conversie.

Zoals je misschien hebt opgemerkt, delen sets veel eigenschappen met dictionaries. Net als dictionaries werken ze ook op basis van **hashing**, wat betekent dat controleren of een element in een set zit ook een constante tijd van $$O(1)$$ is.

    >>> 'een' in s
    True

Dus, ongeacht hoeveel elementen er in de set zitten, zal het controleren of elementen aanwezig zijn snel zijn. Het feit dat sets werken met hashing betekent ook dat ze alleen hashbare elementen kunnen bevatten, dus we kunnen geen lijst toevoegen als element:

    >>> s.add([3, 4])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

Al dit efficiënt controleren of elementen in sets zitten, wordt ook gebruikt om de klassieke setbewerkingen zeer efficiënt te maken. Setbewerkingen, zoals beschreven in de verzamelingenleer (een tak van de wiskundige logica), gaan over welke elementen worden gedeeld tussen 2 sets. Laten we beginnen met het maken van twee sets.

    >>> b = {3, 5, 7, 8, 12, 16, 21}
    >>> b = {16, 24, 21, 8, 9, 1, 2}
    >>> a
    {3, 5, 7, 8, 12, 16, 21}
    >>> b
    {1, 2, 8, 9, 16, 21, 24}

De eerste bewerking die we zullen bekijken is unie, wat een nieuwe set construeert met de unieke elementen gecombineerd uit beide sets.

    >>> a.union(b)
    {1, 2, 3, 5, 7, 8, 9, 12, 16, 21, 24}
    >>> a | b
    {1, 2, 3, 5, 7, 8, 9, 12, 16, 21, 24}
    >>> b | a
    {1, 2, 3, 5, 7, 8, 9, 12, 16, 21, 24}

We kunnen de unie-bewerking toepassen met de functie `.union()` op de sets of door de `|` operator te gebruiken tussen de twee sets. Let op dat de volgorde van de operanden er niet toe doet, omdat de unie nemen tussen `a` en `b` hetzelfde is als de unie nemen tussen `b` en `a`.

Hierna proberen we intersectie, wat je ook al hebt gezien in de introductie. Het construeert een nieuwe set met de unieke elementen die in _beide_ sets voorkomen.

    >>> a.intersection(b)
    {

8, 16, 21}
    >>> a & b
    {8, 16, 21}
    >>> b & a
    {8, 16, 21}

We kunnen de intersectie-bewerking toepassen met de functie `.intersection()` of door de `&` operator te gebruiken. Net als bij unie doet de volgorde tussen de operanden er niet toe, omdat de intersectie tussen `a` en `b` hetzelfde is als de intersectie tussen `b` en `a`.

Ten slotte kijken we naar het verschil tussen sets:

    >>> a.difference(b)
    {3, 12, 5, 7}
    >>> a - b
    {3, 12, 5, 7}
    >>> b - a
    {24, 1, 2, 9}

Dus het verschil tussen `a` en `b` creëert een nieuwe set met alle elementen van `a` die **niet** aanwezig zijn in `b`. Let op dat de volgorde van de operanden hier _wel_ uitmaakt.

We kunnen ook controleren of sets deelverzamelingen of supersets van elkaar zijn, wat betekent dat de ene _alle_ elementen van de andere bevat.

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

Dit kan worden gedaan met de functies `.issubset()` en `.issuperset()` of de `<=` en `>=` operators. Er zijn ook de `<` en `>` operators voor _strikt_ deelverzamelingen, wat betekent dat de twee sets niet gelijk kunnen zijn.

Dit concludeert deze introductie tot sets.

# Oefenen met sets

> Als er een oefening is die je niet weet op te lossen, bekijk de theorie dan opnieuw. Als dat niet helpt, bespreek de oefening dan met een andere student en/of de leraar.

Test je begrip met de volgende oefeningen. Gebruik je gebruikelijke code-editor en maak een bestand genaamd `sets.py` aan.

**Oefening 1** Maak twee sets `eersteSet` en `tweedeSet` met de getallen 23, 42, 65, 57, 78, 83, en 29, en 57, 83, 29, 67, 73, 43, en 48 respectievelijk.

**Oefening 2** Haal de intersectie van de sets en sla het resultaat op in `derdeSet`. Maak een andere set `vierdeSet` die het verschil bevat tussen `eersteSet` en `tweedeSet`, het verschil zijnde alle elementen in `eersteSet` die niet in `tweedeSet` zitten.

**Oefening 3** Voeg het getal 67 toe aan `derdeSet`.

**Oefening 4** Controleer of `derdeSet` een subset is van `eersteSet` en als dat het geval is, print dan de tekst "subset!", print anders "geen subset".

**Oefening 5** Ten slotte, gegeven de lijst met dubbele items genaamd `dubbelen`. Filter voor unieke items met behulp van een set en sla de oplossing op als een lijst in de variabele `unieken`.

    dubbelen = ["tennis", "badminton", "roeien", "voetbal", "tennis", "judo", "judo", "karate", "voetbal"]
    unieken = # Jouw oplossing hier
