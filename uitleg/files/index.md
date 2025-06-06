# Werken met databestanden in Python

Voor veel toepassingen worden databestanden gebruikt. Hierin staan gegevens opgeslagen van bijvoorbeeld een onderzoek, of simpele statistieken over het weer.

Een bestand wordt over het algemeen opgeslagen op de harddisk van een computer. Als je een Python-programma uitvoert heeft dat toegang tot de bestanden van diezelfde computer. Het is ook mogelijk om bijvoorbeeld gegevens van internet te downloaden in je programma en zo verder te verwerken. Maar bij deze uitleg gaat het om bestanden op de harddisk.

## Voorbeeldbestand

Laten we een bestand genaamd `data.txt` aanmaken met de volgende inhoud:

    naam,telefoon
    Wak,+31602282791
    Reff,+31601739128
    Am,+31602739142

Dit bestand heeft een *header*-regel waarin de betekenis van de inhoud staat beschreven (namen, telefoonnummers). Dit is niet standaard, er kunnen ook databestanden zijn zonder header-regel. Ook zijn de gegevens opgedeeld in regels, voor elke persoon een regel, kennelijk. Tot slot is elke regel opgedeeld met komma's. Dit is ook niet standaard, de indeling van een file wordt bepaald door degene die de file aanmaakt. Soms zien ze eruit als bovenstaande, soms niet.

Zorg dat het databestand in dezelfde map (directory) staat als je Python-bestanden.

## Bestanden openen en weer sluiten

Als je een bestand wil inlezen dan moet je dit openen en naderhand weer sluiten. Dat is nodig omdat de toegang tot een bestand vaak geblokkeerd wordt zodra een programma het opent. In Python heb je de beschikking over de constructie `with ... as ...`, waarin je code kunt plaatsen om een file in te lezen. Als het blok code klaar is, wordt het bestand automatisch gesloten.

    with open("data.txt", "r") as data_file:
        all_data = data_file.read()
        print(all_data)
        # na deze regel wordt de file gesloten

In dit geval zie je ook dat het bestand in z'n geheel wordt ingelezen en geprint (bestudeer de commando's en probeer het uit). In dit geval gaat het om een klein bestand. Maar databestanden zijn vaak heel groot en in zo'n geval is het niet efficiënt om het hele bestand in te lezen met de methode `read()`. In de opdrachten van deze cursus doe je dat dus niet.

Er staat hierboven een onderdeel dat misschien niet heel duidelijk is: de string `"r"` die wordt meegegeven aan de functie `open()`. Die `r` staat voor "for **r**eading", wat betekent dat de file geopend wordt door het programma en dan alleen gelezen kan worden. Schrijven mag niet.

Gebruik altijd een `with ... as ...` om files te openen.

## Cursor

Zodra je een bestand hebt geopend houdt Python bij *waar je bent in de file*. Dit heet een cursor. Een bestand inlezen is vrij kostbaar, dus je kunt niet simpelweg vragen om een bepaalde regel uit een bestand, zoals je bij een string wel kunt vragen om een character op een bepaalde plek.

Wat wél kan is een file van boven naar beneden uitlezen:

    with open("data.txt", "r") as data_file:
        print(data_file.readline().rstrip())
        print(data_file.readline().rstrip())

Als je dit uitprobeert zul je zien dat de eerste twee regels van het bestand worden uitgeprint en **niet** twee keer de eerste regel.

De methode `readline()` leest een stuk uit de file tot en met de eerste newline (`\n`) en geeft het terug als string. Die string bevat ook de newline aan het eind. Met de methode `rstrip()` halen we die eraf.

## Regels lezen

Met de volgende constructie kun je het bestand regel voor regel tot het einde verwerken. We printen daarme de namen uit het bestand op een nette manier uit:

    with open("data.txt", "r") as data_file:
        for line in data_file:
            naam, telefoon = line.rstrip().split(',')
            print(naam)

In de loop wordt aan de variabele `line` steeds de inhoud van de volgende regel toegekend. Net als bij `readline()` staat de newline erbij, dus ook hier gebruiken we `rstrip()`.

Hiermee kun je de data in het bestand efficiënt verwerken, want er staat steeds één regel aan data in de variabele `line`. Als de regel verwerkt is wordt `line` overschreven met de inhoud van de volgende regel.

In het voorbeeld hierboven verwerken we de inhoud van de regel door te splitsen, en vervolgens printen we steeds de naam uit (en niet het telefoonnummer).

## Files schrijven

Om een file te schrijven kun je die openen "for **w**riting" met het argument `"w"`.

    with open("new_data.txt", "w") as data_file:
        data_file.write("book_title,isbn\n")

De file wordt dan *gewist* en geopend. Dat betekent dat alle oude data uit de file wordt weggegooid!

Wil je geen gegevens weggooien maar alleen nieuwe toevoegen aan het einde, open de file dan "for **a**ppending" met het argument `"a"`:

    with open("new_data.txt", "a") as data_file:
        data_file.write("If He Had Been with Me,9781728205489\n")

Merk op dat als wij `write()` aanroepen, we de output eindigen met een newline. Als je dat niet doet dan zullen er geen regels worden gemaakt in de file, maar komt alles achter elkaar op één regel. Python voegt dus niet automatisch newlines toe.

## Data analyseren

Als je data wil analyseren kun je ook de verschillende methoden combineren. Je kunt bijvoorbeeld regels overslaan door ze simpelweg in te lezen maar er niets mee te doen. Daarna staat de cursor op de volgende regel, en dan kun je *vanaf daar* de data verwerken. Zie dit voorbeeld:

    with open("data.txt", "r") as data_file:
        # gooi eerste regel weg door in te lezen
        data_file.readline()
    
        # verwerk volgende regels tot einde
        for line in data_file:
            ...

## Lezen en schrijven

Wil je een bestand inlezen en aangepast wegschrijven, dan kun je twee bestanden in één keer openen:

    with open("data.txt", "r") as input_file, open("new_data.txt", "w") as output_file:
        # pas header-regel aan
        first_line = input_file.readline().rstrip()
        output_file.write(f"{first_line},counter\n")
    
        counter = 1
        for line in input_file:
            # voeg komma en teller toe aan einde van regel
            line = line.rstrip() + f",{counter}\n"
            # schrijf aangepaste regel
            output_file.write(line)
            # update teller
            counter += 1

Hier passen we de file aan door aan het eind van elke getal een teller toe te voegen. Als het goed is ziet het bestand `new_data.txt` er nu zo uit:

    naam,telefoon,counter
    Wak,+31602282791,1
    Reff,+31601739128,2
    Am,+31602739142,3

Let op dat je in feite files niet kunt aanpassen! Omdat we met een cursor werken is het bijvoorbeeld niet mogelijk om tekens of zelfs regels in te voegen of te verwijderen. Daarom werken we bijna altijd met een input-bestand en een apart output-bestand onder een andere naam.

## Data bijhouden tijdens de analyse

Als je door een bestand leest kun je de informatie regel voor regel verwerken. Als je variabelen klaarzet kun je daarin informatie bijhouden tijdens de analyse.

Hieronder staat een stukje code dat het telefoonnummer opzoekt van de persoon van wie de naam het eerst in het alfabet staat:

    with open("data.txt", "r") as data_file:
        # gooi eerste regel weg
        data_file.readline()

        # variabelen voor analyse
        gevonden_naam = ''

        # verwerk volgende regels tot einde
        for line in data_file:

            # losse gegevens
            naam, telefoon, teller = line.rstrip().split(',')

            # naam eerder in alfabet of dit is de eerste die we vinden
            if naam < gevonden_naam or gevonden_naam == '':
                # overschrijf gevonden_naam en telefoon met nieuw gevonden
                gevonden_naam = naam
                gevonden_telefoon = telefoon

        # als eerste_naam een waarde bevat hebben we een naam gevonden
        if gevonden_naam != '':
            print(gevonden_telefoon)
