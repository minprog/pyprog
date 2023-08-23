# Stijlgids

> Let op: deze stijlgids wordt nog verder uitgewerkt vóór de eerste code review plaatsvindt.

Programmacode is bij voorkeur goed leesbaar, niet alleen voor jezelf, maar ook voor een ander met wie je samenwerkt. Bij deze cursus is het belangrijk om niet alleen te kijken naar de functionaliteit van de code ("hoe maak ik dit") maar ook naar de kwaliteit ("hoe goed is dit leesbaar"). Eerder hebben we al kort een aantal richtlijnen genoemd voor het gebruiken van commentaar bij stukjes code. Maar er zijn meer aspecten, die je hieronder kunt vinden. Later in je programmeercarrière zul je zien dat je wel eens afwijkt van deze richtlijnen. Aanvankelijk is het echter beter ze te volgen: leer ze goed zodat je ze later effectiever kunt breken en je code goed leesbaar wordt voor iedereen, inclusief jezelf.

## Terminologie

Om te beginnen een paar dingen over terminologie:

- We hebben het vaak over "programma's". Een *programma* is een op zichzelf staand geheel, een stuk software dat een taak kan uitvoeren. Denk aan een rekenmachine op je telefoon. Of Microsoft Word. Visual Studio Code is ook een programma, waarin je schrijft in de 'programmeertaal' Python. Jij zal in deze cursus een heleboel verschillende bestanden aanmaken die een taak uitvoeren, dat zijn ook allemaal programma's.

- We hebben het ook vaak over "code". Een stuk *code* is een fragment, vaak onderdeel van een programma. Het woord code is niet telbaar, dat wil zeggen dat je niet kunt spreken van "een code" of "twee codes". Je kunt wel zeggen "mijn code werkt niet", dan gaat het kennelijk over het stuk code dat je zojuist geschreven hebt.

- Een programma bestaat uit "regels" code.

## Taalkeuze

Op het internet zul je zien dat de code en commentaar doorgaans in het Engels gesteld zijn. In deze cursus werken we vaak in het Nederlands. Het is hoe dan ook belangrijk om de taalkeuze goed af te stemmen: variabelenamen en commentaar beide in het Nederlands óf beide in het Engels, maar niet door elkaar heen.

## Naamgeving

Veel elementen in je code hebben een *naam*. Het gaat dan vooral om functies en variabelen. We geven wat richtlijnen.

### Functies

De namen van functies mogen zo lang zijn als je wilt, mits redelijk. In dit geval is het belangrijk dat het doel van de functie zo duidelijk en precies mogelijk omschreven wordt.

    def gebruiker_gemiddelde_huidig_jaar():
        ...

Je ziet dat in de naam meerdere woorden staan, die gescheiden zijn met een underscore (`_`). Dit is gebruikelijk in Python, alle functienamen met meerdere woorden zijn geschreven met kleine letters en met underscores ertussen.

### Variabelen

Namen van variabelen hou je het liefst net wat korter dan functienamen, omdat ze meestal vaker voorkomen. Denk dan aan één of twee woorden. Een paar voorbeelden:

    muur_hoogte = 2.34
    aarde_omtrek = 40007.86
    totale_neerslag = 823.3

Woorden afkorten is meestal niet de bedoeling. Hiervan wordt je code een stuk lastiger te lezen (een erg luie programmeur zou bovenstaande variabelen wellicht `mh`, `aomtr` en `t_nrslg` hebben genoemd, maar hoe moet je nog achterhalen wat daar bedoeld wordt?).

Er zijn uitzonderingen. Je programma gaat namelijk weleens over een bepaald onderwerp waar afkortingen gebruikelijk zijn. Wiskunde en natuurkunde zitten vol afkortingen, zoals degene hieronder.

    v_konijn = 0.002          <-- v staat voor snelheid
    x_konijn = 23.11          <-- x staat voor plaats
    
    for i in range(N):        <-- gebruik i, j of k als iteratie-variabele en N als grens
        ...
    
    for x_i in range(x_0, x_N):  <-- als je iteratie-variable bv. een plaats is
        ...

Het is aan te raden afkortingen die in wis- en natuurkunde gebruikelijk zijn ook te gebruiken bij dit vak, want iedereen snapt dan wat je bedoelt. Komt een afkorting hier niet vandaan of is een afkorting alsnog mogelijk onduidelijk voor de gebruiker, dan is uitleg waarschijnlijk nodig. Over het algemeen is het een goed idee om de afkortingen zoveel mogelijk te vermijden tenzij het evident is wat bedoeld wordt.

Mocht je regel code veel onderdelen of informatie bevatten, dan kun je besluiten om deze onderdelen tot aparte variabelen samen te trekken.

    # dit is vrij lang
    E_tot = 0.5 * m * (v_1 + v_2)**2 + m * g * (h_1 + h_2)
    
    # dit is overzichtelijker en bovendien een gebruikelijke opdeling in natuurkunde
    E_kin = 0.5 * m * (v_1 + v_2)**2
    E_pot = m * g * (h_1 + h_2)
    E_tot = E_kin + E_pot

Het kiezen van logische, beschrijvende namen van je variabelen en functies is een van de beste dingen die je kunt doen in programmeren. Op deze manier begrijpt een ander namelijk direct wat je aan het doen bent en hoef je minder commentaar toe te voegen. Misschien is het allerbelangrijkste nog wel dat door logische naamgeving je ook sneller gaat programmeren! In je hoofd is wat je variabelen opslaan en wat je functies doen namelijk duidelijk en niet een grote wirwar van informatie (bv. a = , b = , p = , q =,  etc.) die je hoofd constant moet bijhouden.

## Commentaar

Het is net zo makkelijk om te veel commentaar in je code te schrijven als te weinig. Om te bepalen waar commentaar nou echt nodig is, moeten we ons een beetje verplaatsen in de lezer van de code. Dat kan iemand anders zijn, iemand die jouw code gebruikt om een gaaf programma te schrijven. Maar je kunt het ook zelf zijn, een paar maanden later, wanhopig proberend om nog een beetje kaas te maken van hoe het ook alweer in elkaar zat. Die lezer, wat heeft die nodig?

- Samenvattingen van stukjes code. Meestal heb je je programma's of functies opgedeeld in functionele blokjes. Misschien zijn het maar een paar regels code. Het is vaak niet zo moeilijk om van zo'n blokje code samen te vatten wat de bedoeling is.

- Waarschuwingen voor potentiële problemen. Misschien heb je voor een bepaald stuk code een tijdelijke oplossing bedacht, waarvan je weet dat die niet in alle gevallen gaat werken (maar voor nu is het wel goed zo). Dan is het handig dat te documenteren door middel van een comment.

- Uitleg van erg complexe algoritmen. Soms is het gewoonweg niet anders dan dat je een behoorlijk complex systeem aan het schrijven bent. In dat geval kun je uitleg geven, of zelfs maar een link naar meer informatie.

- Bronvermelding. Om niet van plagiaat beschuldigd te worden is het natuurlijk belangrijk altijd een bron te vermelden als je een stuk code geheel of gedeeltelijk overneemt van iemand anders. Zelfs als je het nog flink verbouwt hoort dat erbij.

### Voorbeeld 1

Wanneer hoeft het nou bijvoorbeeld niet? Als je variabelenamen erg duidelijk zijn, dan hoef je misschien geen commentaar te schrijven. Maar soms kun je toch nog wat toevoegen:

    # bereken gemiddelde cijfer voor deze student
    gemiddelde = som / aantal_opdrachten + 1

(Nu weten we dat het niet zomaar om een gemiddelde gaat, maar om een cijfer. Afhankelijk van de rest van het programma heeft dit commentaar toegevoegde waarde.) Merk dus op dat je door je variabelenamen goed te kiezen commentaar kunt weglaten en dus een kortere, overzichtelijke code krijgt.

#### Schrijfwijze

Let ook op de schrijfwijze: geen hoofdletter, geen punt, zinnen in codetaal (lidwoorden worden bv. weggelaten) en een spatie na het hekje `#`. Het commentaar staat *boven* de regel waar het over gaat.

### Voorbeeld 2

Het is gebruikelijk om bovenaan programma's wat algemene informatie op te nemen. Meestal gaat het om de namen van de auteurs, en een samenvatting van het doel van het programma.

    # naam: Ivo van Vulpen
    # in samenwerking met: Martijn Stegeman
    #
    # Dit programma berekent de gemiddelde waarden van een reeks
    # getallen gegeven door de gebruiker.

#### Schrijfwijze

Let ook hier even op de schrijfwijze. De samenvatting in het commentaar hierboven is toch wat te lang om op één enkele regel op te nemen. In dat geval moeten we het expliciet over meerdere regels verdelen. Gewoon een regel toevoegen met een `#` ervoor. Omdat we in zo'n samenvatting volzinnen gebruiken is het wel goed om hoofdletters en punten te gebruiken om de zin overzichtelijk te maken.

We hebben ervoor gekozen om het nu na ongeveer 65 tekens af te kappen. De bedoeling is dat regels een redelijke lengte hebben: lezen gaat het prettigst als regels zo'n 45--90 tekens lang zijn, net als in boeken. De regellengte kun je in VScode rechts onderaan in de editor aflezen.

### Voorbeeld 3

Een commentaarregel wordt bijna altijd bovenaan een 'blokje' code gezet. Dit doe je bijvoorbeeld bij het definiëren van een functie. Let erop dat een regel commentaar boven een functie niet precies zegt wat de titel van de functie ook al zegt, of vermeldt dat het een functie is, want dat begrijpt de lezer al. Denk goed na wat voor commentaar de code prettiger leesbaar en/of begrijpelijker maakt.

Wanneer functies meerdere variabelen hebben worden die altijd gescheiden met een spatie. Het is gebruikelijk om de variabelen van een functie toe te lichten in een commentaarregel boven de functie. Het lijkt soms of dit niet in één regel past maar als je met codetaal goed je best doet kan dit vrijwel altijd.

    # bereken de hypotenusa met Pythagoras gegeven zijden a en b
    def hypotenusa(a, b):
        c = (a ** 2 + b ** 2) ** (1/2)
        return c

## Indentatie

Indentatie (inspringen) gaat over het toevoegen van witruimte aan het begin van een regel. In Python is het in veel gevallen noodzakelijk om een regel te beginnen met spaties, bijvoorbeeld als je een functie definieert:

    def som(x, y):
        resultaat = x + y
        return resultaat

Let wel op! Je kunt de extra witruimte invullen met tabs of met spaties. In heel veel gevallen is een tab zichtbaar als 8 spaties, maar soms ook als 4 of 2. Hoe dan ook, het wordt een probleem als je tabs en spaties door elkaar gaat gebruiken, want dan is onduidelijk wat de bedoeling is.

    def som(x, y):
        resultaat = x + y         <-- vier spaties
            return resultaat      <-- 1 tab is hier 8 spaties geworden

De `return` staat een stukje extra naar rechts, maar in feite is het één tab. Het resultaat is dat het een stuk moeilijker leesbaar is. Bovendien begrijpt Python er ook niet zoveel meer van. Je krijgt al snel een foutmelding als je zoiets doet. Gebruik dus alleen maar spaties, of alleen maar tabs om te indenteren.

Oh, en misschien goed om nog even te herhalen. Als een regel eindigt op een dubbele punt (`:`), dan moeten alle regels eronder geïndenteerd worden. Tenminste, de regels die er inderdaad bij horen.

    # sommeert de waarden van een lijst getallen
    def sum(lijst_getallen):
        resultaat = 0
        for getal in lijst_getallen:
            resultaat = resultaat + getal
        return resultaat

Hier zie je dat de regel `resultaat = resultaat + getal` bij de `for`-loop hoort. De `return` staat echter weer een stukje naar links, waardoor je weet dat deze niet bij de `for`-loop hoort.

Ook comments moet je een indentatie geven. Kijk naar dit voorbeeld:

    def print_is_het_fruit(naam_van_eten):
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

## Witregels en extra spaties

Net als in andere media waarin tekst een belangrijke rol speelt, kan in programma's witruimte worden ingezet om de leesbaarheid te vergroten.

### Witregels

Zoals hierboven beschreven bij "Commentaar", en zoals toegepast bij "Indentatie" kun je je programma vaak opdelen in blokjes code. Hiermee kun je bijvoorbeeld de verschillende stappen beschrijven in een algoritme. Zie hier een programma dat in drieën gesplitst is.

    # getal-invoer
    getal = int(input("Voer een getal in: "))
    while getal < 0:
        getal = int(input("Voer een *positief* getal in: "))

    # checkt of het getal even is
    if getal % 2 == 0:
        even = 'Ja!'
    else:
        even = 'Nee!'

    # output (print een ValueError als het ingevoerde getal een float is)
    print(f"Is het getal even? {even}")

De drie onderdelen zijn respectievelijk: de gebruikersinvoer, de berekening, en de uitvoer. Die onderdelen kom je wel vaker tegen natuurlijk. Let ook op de aanwijzingen die we in het commentaar hebben toegevoegd: eerst uitleg van complex algoritme, daarna een waarschuwing dat het misschien niet altijd werkt (en vooral: wanneer!).

We zien hier een belangrijke vuistregel in actie: splits de code op in blokjes, gescheiden door een witregel met één regel commentaar per blokje, die bovenaan het blokje staat. Alleen bij bijvoorbeeld de functie in het voorbeeld bij "indentatie" is het logischer om de comment onder de functie-definitie te plaatsen, omdat door de logische titel van de functie commentaar overbodig is geworden. Dit is echter een grote uitzondering.

### Spaties rondom operatoren

"Operatoren" zoals `+`, `==`, `%` en `**` zijn veelgebruikt in formules en vergelijkingen. Het is de bedoeling om hier heel bewust spaties rondom de operatoren te plaatsen, zodat de formules goed leesbaar blijven.

    i = i + 1 (of i += 1)
    uren = uren % 24 (of uren %= 24)
    hypotenusa_kwadraat = x * x + y * y
    c = (a + b) * (a - b)

Let ook op dat we in het voorbeeld van de energieën bij "Variabelen" ("tegen de regels in") `(v_1 + v_2)**2` schrijven in plaats van '(v_1 + v_2) ** 2'. Dit hebben we gedaan om meer eenheid te creëren in dit onderdeel van de vergelijking. Soms is het handig om dit te doen, omdat het de leesbaarheid van de vergelijking ten gunste kan komen. Naarmate je beter wordt in programmeren en meer code hebt gezien, zul je steeds handiger worden in het maken van keuzes in dit soort grijze gebieden.
