# Tuples

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_wlxgk3ja&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_dztdpgtv)

## Referentie

Tuples lijken sterk op lijsten omdat ze sequenties van elementen opslaan, maar ze worden vaak op een heel andere manier gebruikt. Het belangrijke verschil voor tuples is dat ze immutable (onveranderlijk) zijn, wat betekent dat ze enkele operaties ondersteunen die lijsten niet ondersteunen en andersom. We zullen dieper ingaan op dit verschil door naar enkele voorbeelden te kijken.

Een tuple maken lijkt erg op het maken van een lijst, behalve dat we ronde haken gebruiken in plaats van vierkante haken.

```python
t = (42, 'hallo', 3.1415)
t
```

We kunnen elementen uit een tuple opvragen via een specifieke index met vierkante haken, net als bij een lijst.

```python
t[1]
```

Maar wanneer we proberen een waarde toe te kennen aan een index, zoals bij een lijst, krijgen we een foutmelding.

```python
t[1] = 9
```

Dit is het eerste teken dat de tuple inderdaad onveranderlijk is; het is *niet* mogelijk om een waarde op een specifieke index te wijzigen. Daarnaast kunnen we ook geen dingen aan een tuple toevoegen.

```python
t.append('wereld')
```

Dus, zodra een tuple is gemaakt, kunnen we de elementen die het bevat niet veranderen of meer elementen toevoegen. Dit is wat het betekent om onveranderlijk te zijn; het *kan niet worden gewijzigd*.

Met al deze beperkingen lijkt het misschien alsof een tuple veel minder doet dan een lijst, maar onveranderlijkheid heeft ook enkele voordelen.

Een van de meest voorkomende manieren waarop een tuple wordt gebruikt, is door meerdere waarden vanuit een functie terug te geven.

```python
def vind_max_index(l):
    max_ind = 0
    max_val = 0
    for i in range(len(l)):
        if l[i] > max_val:
            max_val = l[i]
            max_ind = i
    return (max_ind, max_val)

lijst_van_waarden = [4.14, 8.1, 9.7, 2.0]
vind_max_index(lijst_van_waarden)
```

Deze functie probeert de maximale waarde in een lijst te vinden. Het geeft echter niet alleen de maximale waarde terug, maar ook de index van die maximale waarde in de lijst. Beide waarden worden samen teruggegeven in een tuple.

Als je meerdere dingen combineert met komma's ertussen, worden ze automatisch een tuple, zelfs zonder de ronde haken eromheen. Dit wordt *tuple-packing* genoemd. De laatste regel van de functie had dus ook kunnen zijn `return max_ind, max_val`, wat de vorm is die je vaker zult zien.

```python
maximum_index, maximum_value = vind_max_index(lijst_van_waarden)
maximum_index
maximum_value
```

We kunnen zien dat hetzelfde ook omgekeerd werkt, bij het toewijzen aan variabelen. Hier wijzen we in slechts 1 regel toe aan 2 nieuwe variabelen, `maximum_index` en `maximum_value`. Dit wordt *tuple-unpacking* genoemd en wijst de waarden uit de tuple toe aan de variabelen in dezelfde volgorde als waarin ze in de tuple stonden.

Het aantal elementen moet daarom overeenkomen met hoeveel variabelen je probeert uit te pakken.

```python
t
(a, b, c) = t
```

Bij het uitpakken van een tuple moet het aantal elementen exact overeenkomen en geven we elk element een andere variabelenaam. Dit zou je een idee moeten geven van hoe en wanneer tuples worden gebruikt ten opzichte van lijsten. Als we een groot aantal van hetzelfde type ding hebben, allemaal samen opgeslagen, zou je ze in een lijst opslaan. Op die manier kun je nieuwe elementen toevoegen, over elk element itereren en ze allemaal op dezelfde manier verwerken.
Als je echter een klein vast aantal verschillende dingen samen wilt opslaan, zoals een maximale waarde en de bijbehorende index, dan zou je een tuple gebruiken. Je kunt deze dingen dan retourneren, doorgeven aan een functie of zelfs meerdere ervan in een lijst opslaan, maar de items blijven samen, onveranderd, in de tuple.
Dingen die samen in een tuple zijn opgeslagen, moeten altijd kunnen worden uitgepakt; je moet precies weten hoeveel elementen je verwacht in de tuple en welke verschillende dingen op elke index zijn opgeslagen.

Het belangrijkste doel van tuples is daarom het opslaan van een klein vast aantal verschillende dingen samen in één structuur. Er is nog één andere belangrijke toepassing van tuples die we nog niet hebben besproken; **hashing**. Hashing is de onderliggende magie die dictionaries zo efficiënt maakt. In de vorige tekst hebben we gesproken over het feit dat zoeken naar sleutels in dictionaries bijna altijd een constante tijd $$O(1)$$ operatie is. Dictionaries bereiken dit door een proces genaamd *hashing* van de sleutel, wat een berekening is die de computer vertelt waar in de dictionary gezocht moet worden naar de sleut

el. In Python is de hashbewerking alleen toegestaan bij **onveranderlijke** elementen omdat, als we een sleutel zouden kunnen wijzigen, hashing mogelijk een andere locatie zou geven om naar te zoeken nadat een sleutel is gewijzigd, waardoor het onmogelijk is om terug te vinden. Als we proberen een dictionary te maken met een lijst als sleutel, die natuurlijk veranderlijk is, krijgen we een foutmelding:

```python
telefoonboek = {}
jan = ['Jan', 'Jansen']
telefoonboek[jan] = 5551234
```

In dit voorbeeld proberen we een telefoonboek te maken waarin we iemand kunnen opzoeken op basis van hun voornaam en achternaam, en hun telefoonnummer terug kunnen krijgen. Maar door de voornaam en achternaam samen in een lijst op te slaan, hebben we een veranderlijke sleutel gemaakt die niet gehasht kan worden. Als we dit echter veranderen in een tuple, die onveranderlijk is, *kunnen* we de twee namen samen als sleutel gebruiken.

```python
jan = tuple(jan)
jan
telefoonboek[jan] = 5551234
telefoonboek
```

Verschillende dingen samen opslaan als een sleutel in een dictionary is vrij gebruikelijk en is nog een situatie waarin je echt een tuple nodig hebt en geen lijst kunt gebruiken.

Dit sluit deze inleiding over tuples af.
