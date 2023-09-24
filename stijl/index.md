# Stijlgids

Programmacode is bij voorkeur goed leesbaar, niet alleen voor jezelf, maar ook voor een ander met wie je samenwerkt. Bij deze cursus is het belangrijk om niet alleen te kijken naar de functionaliteit van de code ("hoe maak ik dit") maar ook naar de kwaliteit ("hoe goed is dit leesbaar"). Eerder hebben we al kort een aantal richtlijnen genoemd voor het gebruiken van commentaar bij stukjes code. Maar er zijn meer aspecten, die je hieronder kunt vinden. Later in je programmeercarrière zul je zien dat je wel eens afwijkt van deze richtlijnen. Aanvankelijk is het echter beter de regels te volgen: leer ze goed kennen zodat je na deze cursus goed kunt beoordelen wanneer je ze effectief kunt breken en hoe je je code leesbaarder maakt voor iedereen, inclusief jezelf.

## Terminologie

Om te beginnen een paar dingen over terminologie:

- We hebben het vaak over "programma's". Een *programma* is een op zichzelf staand geheel, een stuk software dat een taak kan uitvoeren. Denk aan een rekenmachine op je telefoon. Of Microsoft Word. Visual Studio Code is ook een programma, waarin je schrijft in de 'programmeertaal' Python. Jij zal in deze cursus een heleboel verschillende bestanden aanmaken die een taak uitvoeren, dat zijn ook allemaal programma's.

- We hebben het ook vaak over "code". Een stuk *code* is een fragment, vaak onderdeel van een programma. Het woord code is niet telbaar, dat wil zeggen dat je niet kunt spreken van "een code" of "twee codes". Je kunt wel zeggen "mijn code werkt niet", dan gaat het kennelijk over het stuk code dat je zojuist geschreven hebt.

- Een programma bestaat uit "regels" code (geen lijnen).


## Taalkeuze

In code op internet zul je zien dat de code en commentaar doorgaans in het Engels gesteld zijn. In deze cursus werken we met code in het Engels, maar comments in het Nederlands. Het is hoe dan ook belangrijk om de taalkeuze goed intern af te stemmen, zodat alles snel te begrijpen is. Zorg dus dat je de stijl van de aangeleverde code consistent volgt.


## Naamgeving

Veel elementen in je code hebben een *naam*. Het gaat dan vooral om functies en variabelen. We geven hier een aantal richtlijnen voor het kiezen van namen.

### Functies

De namen van functies mogen best lang zijn, als het maar redelijk blijft. In dit geval is het belangrijk dat het doel van de functie zo duidelijk en precies mogelijk omschreven wordt.

    def gebruiker_gemiddelde_huidig_jaar():
        ...

Deze naam is behoorlijk lang, en als deze functie heel vaak wordt gebruikt op andere plekken in het programma, dan is het misschien logisch om voor een kortere naam te kiezen. Maar gebruik je deze functie maar een enkele keer, dan is de naam prima. Het is een afweging die je zelf maakt, met in het achterhoofd de leesbaarheid van de code.

Je ziet dat in de naam meerdere woorden staan, die gescheiden zijn met een underscore (`_`). Dit is gebruikelijk in Python: alle functienamen met meerdere woorden zijn geschreven met kleine letters en met underscores ertussen. Zorg dat je deze conventie volgt.

### Variabelen

Namen van variabelen hou je het liefst net wat korter dan functienamen, omdat ze doorgaans vaker voorkomen. Denk dan aan één of twee woorden. Een paar voorbeelden:

    hoogte_muur = 2.34
    omtrek_aarde = 40007.86
    totale_neerslag = 823.3

Woorden afkorten is meestal niet de bedoeling. Hiervan wordt je code een stuk lastiger te lezen (een erg luie programmeur zou bovenstaande variabelen wellicht `hm`, `omtra` en `t_nrslg` hebben genoemd, maar hoe moet je nog achterhalen wat daar bedoeld wordt?).

Er zijn uitzonderingen. Je programma gaat namelijk weleens over een bepaald onderwerp waar afkortingen gebruikelijk zijn. Wiskunde en natuurkunde zitten vol afkortingen, zoals degene hieronder.

    v_konijn = 0.002          <-- v staat voor snelheid
    x_konijn = 23.11          <-- x staat voor plaats
    
    for i in range(N):        <-- gebruik i, j of k als iteratie-variabele en N als grens
        ...
    
    for x_i in range(x_0, x_N):  <-- als je iteratie-variable bv. een plaats is
        ...

Het is aan te raden afkortingen die in wis- en natuurkunde gebruikelijk zijn ook te gebruiken bij dit vak, want dan is op basis van wiskunde-kennis duidelijk wat er bedoeld wordt. Komt een afkorting hier niet vandaan of is een afkorting alsnog mogelijk onduidelijk voor de gebruiker, dan is uitleg waarschijnlijk nodig.

Maar buiten de wiskunde en natuurkunde is het een goed idee om afkortingen zoveel mogelijk te vermijden.

Mocht een regel code veel onderdelen of informatie bevatten, dan kun je besluiten om deze onderdelen tot aparte variabelen samen te trekken.

    # dit is vrij lang
    E_totaal = 0.5 * m * (v_1 + v_2)**2 + m * g * (h_1 + h_2)
    
    # dit is overzichtelijker en bovendien een gebruikelijke opdeling in natuurkunde
    E_kinetisch = 0.5 * m * (v_1 + v_2)**2
    E_potentieel = m * g * (h_1 + h_2)
    E_totaal = E_kin + E_pot

Het kiezen van logische, beschrijvende namen van je variabelen en functies is een van de beste dingen die je kunt doen in programmeren. Op deze manier begrijpt een ander namelijk direct wat je aan het doen bent en hoef je minder commentaar toe te voegen. Misschien is het allerbelangrijkste nog wel dat door logische naamgeving je ook sneller gaat programmeren! In je hoofd is wat je variabelen opslaan en wat je functies doen namelijk duidelijk en niet een grote wirwar van informatie (bv. a = , b = , p = , q =,  etc.) die je hoofd constant moet bijhouden.


## Groeperen

Naarmate een stukje code langer wordt dreigt het onoverzichtelijker te worden. Er zijn diverse manieren om te zorgen dat de code relatief makkelijk te begrijpen blijft. Eén manier is om stukjes code te *groeperen*. Dit betekent dat je het opdeelt in kleinere delen die logisch samenhangen. Je gebruikt *witregels* om deze delen te onderscheiden. Hieronder zie je dat er eerst een stuk is om de input te verzorgen, en daarna een stuk om een beslissing te nemen en afhankelijk van de uitkomst iets te printen.

    x = int(input("x: "))
    y = int(input("y: "))
                                           <-- witregel
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else
        print("x is equal to y")


## Commentaar

Het is net zo makkelijk om te veel commentaar in je code te schrijven als te weinig. Om te bepalen waar commentaar nou echt nodig is, moeten we ons een beetje verplaatsen in de lezer van de code. Dat kan iemand anders zijn, iemand die jouw code hergebruikt om een ander programma te schrijven. Maar je kunt het ook zelf zijn, een paar maanden later, wanhopig proberend om nog een beetje kaas te maken van hoe het ook alweer in elkaar zat. Die lezer, wat heeft die nodig?

- Samenvattingen van stukjes code. Meestal heb je je programma's of functies gegroepeerd in functionele blokjes. Misschien zijn het maar een paar regels code. Het is vaak niet zo moeilijk om van zo'n blokje code samen te vatten wat de bedoeling is.

- Waarschuwingen voor potentiële problemen. Misschien heb je voor een bepaald stuk code een tijdelijke oplossing bedacht, waarvan je weet dat die niet in alle gevallen gaat werken (maar voor nu is het wel goed zo). Dan is het handig dat te documenteren door middel van een comment.

- Uitleg van erg complexe algoritmen. Soms is het gewoonweg niet anders dan dat je een behoorlijk complex systeem aan het schrijven bent. In dat geval kun je uitleg geven, of zelfs maar een link naar meer informatie.

- Bronvermelding. Om niet van plagiaat beschuldigd te worden is het natuurlijk belangrijk altijd een bron te vermelden als je een stuk code geheel of gedeeltelijk overneemt van iemand anders. Zelfs als je het nog flink verbouwt hoort dat erbij.

Elk commentaar dat je plaats is een afweging waard: hoe draagt het bij aan de begrijpelijkheid van het programma?

### Voorbeeld 1

Wanneer hoeft het nou bijvoorbeeld niet? Als je variabelenamen erg duidelijk zijn, dan hoef je misschien geen commentaar te schrijven. Maar soms kun je toch nog wat toevoegen:

    # bereken gemiddelde cijfer voor deze student
    gemiddelde = som / aantal_opdrachten + 1

(Nu weten we dat het niet zomaar om een gemiddelde gaat, maar om een cijfer. Afhankelijk van de rest van het programma heeft dit commentaar toegevoegde waarde.) Merk dus op dat je door je variabelenamen goed te kiezen commentaar kunt weglaten en dus een kortere, overzichtelijke code krijgt.

Let ook op de schrijfwijze: geen hoofdletter, geen punt, zinnen in codetaal (lidwoorden worden bv. weggelaten) en een spatie na het hekje `#`. Het commentaar staat *boven* de regel waar het over gaat.

### Voorbeeld 2

Het is gebruikelijk om bovenaan programma's wat algemene informatie op te nemen. Meestal gaat het om de namen van de auteurs, en een samenvatting van het doel van het programma.

    # naam: Ivo van Vulpen
    # in samenwerking met: Martijn Stegeman
    #
    # Dit programma berekent de gemiddelde waarden van een reeks
    # getallen gegeven door de gebruiker.

Let ook hier even op de schrijfwijze. De samenvatting in het commentaar hierboven is toch wat te lang om op één enkele regel op te nemen. In dat geval moeten we het expliciet over meerdere regels verdelen. Gewoon een regel toevoegen met een `#` ervoor. Omdat we in zo'n samenvatting volzinnen gebruiken is het wel goed om hoofdletters en punten te gebruiken om de zin overzichtelijk te maken.

We hebben ervoor gekozen om het nu na ongeveer 65 tekens af te kappen. De bedoeling is dat regels een redelijke lengte hebben: lezen gaat het prettigst als regels zo'n 45--90 tekens lang zijn, net als in boeken.

### Voorbeeld 3

Hier keren we terug naar de gegroepeerde code van hierboven. We voegen comments toe die de functionaliteit samenvatten:

    # vraag om twee gehele getallen
    x = int(input("x: "))
    y = int(input("y: "))

    # vergelijk de waardes en print uitkomst
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else
        print("x is equal to y")

Deze stijl van samenvattende comments laat het toe om alléén de comments te lezen en de code helemaal niet. Dit helpt met de begrijpelijkheid van het programma. Wil de lezer de details kennen, dan kan deze na het commentaar ook de code lezen.


## Indentatie

Indentatie (inspringen) gaat over het toevoegen van witruimte aan het begin van een regel. In Python is het in veel gevallen noodzakelijk om een regel te beginnen met spaties, bijvoorbeeld als je een functie definieert:

    def som(x, y):
        resultaat = x + y
        return resultaat

Let wel op! Je kunt de extra witruimte invullen met zogeheten tabs of met spaties. In heel veel gevallen is een tab zichtbaar als 4 spaties, maar soms ook als 8 of 2. Hoe dan ook, de bedoeling is dat je spaties gebruikt en geen tabs. Deze conventie moet je volgen.

Oh, en misschien goed om nog even te herhalen. Als een regel eindigt op een dubbele punt (`:`), dan moeten alle regels eronder geïndenteerd worden. Tenminste, de regels die er inderdaad bij horen.

    # sommeert de waarden van een lijst getallen
    def sum(lijst_getallen):
        resultaat = 0
        for getal in lijst_getallen:
            resultaat = resultaat + getal
        return resultaat

Hier zie je dat de regel `resultaat = resultaat + getal` bij de `for`-loop hoort. De `return` staat echter weer een stukje naar links, waardoor je weet dat deze niet bij de `for`-loop hoort.

Strikt genomen is dit geen stijlmiddel, want als je een regel code verkeerd indenteert dan zal deze ook verkeerd werken (in andere talen dan Python is dit niet zo).

Ook comments moet je indentatie geven, om duidelijk te maken welk comment waarbij hoort. Kijk naar dit voorbeeld:

    def print_is_het_fruit(naam_van_eten: str):
        # bepaal of het fruit is
        antwoord = False
        for fruitsoort in fruitsoorten:
            if fruitsoort == naam_van_eten:
                antwoord = True
        
        # print het resultaat
        if antwoord:
            print(f"{naam_van_eten} is fruit")
        else:
            print(f"{naam_van_eten} is geen fruit")


## Witruimte

Net als in andere media waarin tekst een belangrijke rol speelt, kan in programma's witruimte worden ingezet om de leesbaarheid te vergroten. Je hebt eerder al gezien dat je witregels kunt gebruiken om code te groeperen.

### Spaties rondom operatoren

"Operatoren" zoals `+`, `==`, `%` en `**` zijn veelgebruikt in formules en vergelijkingen. Het is de bedoeling om hier heel bewust spaties rondom de operatoren te plaatsen, zodat de formules goed leesbaar blijven.

    i = i + 1 (of i += 1)
    uren = uren % 24 (of uren %= 24)
    hypotenusa_kwadraat = x * x + y * y
    c = (a + b) * (a - b)

Let ook op dat we in het voorbeeld van de energieën bij "Variabelen" ("tegen de regels in") `(v_1 + v_2)**2` schrijven in plaats van '(v_1 + v_2) ** 2'. Dit hebben we gedaan om meer eenheid te creëren in dit onderdeel van de vergelijking. Soms is het handig om dit te doen, omdat het de leesbaarheid van de vergelijking ten gunste kan komen. Naarmate je beter wordt in programmeren en meer code hebt gezien, zul je steeds handiger worden in het maken van keuzes in dit soort grijze gebieden.


## Complexiteit (en functies)

Hierboven heb je al geleerd dat je langere stukken code kunt opdelen door te groeperen. Maar dat verandert niets aan de complexiteit van je code. Soms wordt een stuk zo lang dat het eigenlijk niet meer overzichtelijk te krijgen is.

Een belangrijke manier om de complexiteit te "temmen" is om extra functies toe te voegen aan de code. Daarmee verplaats je een stukje functionaliteit naar een eigen blok. Dit maakt wezenlijk verschil met groeperen, omdat je de functie een *naam* kunt geven. Deze naam

In deze cursus krijg je bij de meeste opdrachten al een template waarin een aantal verplichte functies staan. Dat komt omdat je in deze cursus nog moet leren hoe functies werken. Maar zodra je er aan toe bent kun je overwegen extra functies te definiëren en te gebruiken om de complexiteit van je programma te verminderen.

Twijfel je of je van iets een aparte functie moet maken? Overleg eens met je buren of met één van de docenten. Of probeer het en kijk of je programma er misschien overzichtelijker van wordt.


## Opschonen

Er zijn een aantal elementen die niet thuishoren in code die "af" is. Of in ieder geval die ingeleverd wordt:

- stukjes code die "uitgecomment" zijn en niet meer actief
- stukjes code, bijvoorbeeld functies, die niet meer gebruikt worden
- imports die niet nodig zijn omdat je de library niet gebruikt
