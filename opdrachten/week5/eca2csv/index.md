# Preprocessing

![](temperature.png)

Laten we een steentje bijdragen aan de klimaatdiscussie en data analyseren die door de ECA (European Climate Assessment) [beschikbaar](https://www.ecad.eu/dailydata/predefinedseries.php) wordt gemaakt in grote databestanden. We beperken ons tot data die de maximumtemperatuur beschrijft voor elke dag in De Bilt sinds 1901.

Werp eerst eens een blik op [`climate.txt`](climate.txt) en lees bovenin hoe de data gecodeerd is. Het bestand heeft geen standaard-formaat maar een door de ECA bedachte indeling. Daarom moet er een voorbewerking (preprocessing) plaatsvinden voordat we er analyses mee kunnen doen.

We willen de data graag in het CSV-formaat krijgen. Dat is een standaard-formaat dat je makkelijk kunt importeren in Excel, maar je kunt het ook goed inlezen in veel programmeertalen. De naam *comma-separated values* zegt het al: alle gegevens in dit formaat zijn gescheiden door een komma. 

Het gewenste formaat van een CSV-bestand ziet er als volgt uit. De eerste regel moet de **namen** van alle kolommen bevatten, gescheiden door een komma. De volgende regels moeten alle datapunten bevatten, elk op één regel, waarbij alle waardes weer gescheiden worden door een komma. Hier zie je een CSV-file met twee kolommen:

![](telefoon.png)

Let op: de operaties in deze opdracht lijken soms op de voorbeelden uit het boek, maar het zijn zeker geen copy-paste-opdrachten. Eén verschil is bijvoorbeeld dat je hieronder 4 functies moet schrijven die elk twee files openen en weer sluiten. In het het boek worden de files al geopend in de `main`. Dat is hier dus niet de bedoeling. Ook werken we niet met `StringIO` maar alleen maar met databestanden.

## Header verwijderen

Voordat we onze data definitef op kunnen slaan in als CSV, kijken we eerst zorgvuldig naar de data. Bestudeer hiervoor het bestand `climate.txt`. Wat meteen opvalt is dat het bestand begint met een header-tekstje. Dit tekstje komt van pas voor mensen die willen begrijpen hoe het bestand in elkaar steekt. Het bevat informatie over waar de data vandaan komt, maar ook over de betekenis van de variabelen in de data. Voor een computer is deze tekst verwarrend, in die zin dat begin en eind niet duidelijk zijn aangegeven. We besluiten daarom de header-tekst weg te halen, zodat het bestand voortaan begint met de kolomnamen en dan meteen de data.

![](step1.png)

**Opdracht**

- Schrijf in een bestand genaamd `eca2csv.py` een functie die een **bron**bestand opent, de data inleest, de header overslaat, en het resultaat wegschrijft naar een **doel**bestand.

- Parameters van de functie zijn de namen van bron- en doelbestand, en het aantal regels dat verwijderd moet worden. De naam van de functie en de parameters kun je zelf verzinnen.

- Bij dataverwerking is het niet aan te raden om de complete data in te lezen in een variabele. Bij hele grote databestanden is het zelfs onmogelijk omdat deze groter zijn dan het werkgeheugen van de computer. Zorg dus dat je dit niet doet.

- Zorg dat je de voorbeelden uit het boek goed bestudeerd hebt. Gebruik een `with`-statement om de twee bestanden samen te openen.

- Schrijf in de `main` een stukje testcode dat de functie aanroept met als bron `climate.txt` en als doel `climate-noheader.txt`. Run je programma en inspecteer of het resultaat klopt.

## Data filteren
​
Wie goed naar de bestanden kijkt ziet dat de data van het jaar 2020 niet compleet is. Als we dat jaar meenemen bij het berekenen van statistieken krijgen we mogelijk een vertekend beeld. Als je bijvoorbeeld de gemiddelde temperatuur berekent, dan zal 2020 naar verwachting flink koude uitvallen doordat alleen gegevens over de eerste 3 maanden bekend zijn. We gaan dus een functie schrijven die een deel van de data kan verwijderen (in onze tests is dat het jaar 2020).
​
![](step2.png)

**Opdracht**

- Schrijf een functie die een bestand inleest van het bovenstaande formaat en een nieuw bestand opslaat waar de gegevens uit een opgegeven jaartal verwijderd zijn. De functie die jij schrijft moet werken voor elk willekeurig jaartal, dus dat is een parameter van de functie.

- Het jaartal staat in de eerste vier tekens van een regel data.

- De functie moet wederom zelf de nodige bestanden openen en weer sluiten.

- Schrijf in de `main` een stukje testcode dat de functie aanroept met als bron `climate-noheader.txt` en als doel `climate-noheader-no2020.txt`. Run je programma en inspecteer of het resultaat klopt.

## Opschonen missende waarden

Het bestand bevat een aantal "missing values": datums waarvoor geen gegevens bekend zijn. In het oorspronkelijke databestand krijgen deze datums een TX-waarde van 9999. Deze gevallen kunnen de boel behoorlijk verstoren omdat ze een vertekend beeld kunnen geven als je statistieken wil berekenen. We lossen dat in dit geval op door de ontbrekende waarden te vervangen door de gemiddelde waarde van de volgende dag en de vorige dag (afgerond middels de `round`-functie).

De indicator voor een missing value verschilt per databestand; soms is dat een `-1`, soms een `0`, afhankelijk van de waarden die 'natuurlijk' in de data voorkomen. In het geval van deze data wordt `9999` gebruikt als indicator voor een missing value. Een veilige keuze, omdat de kans dat er een temperatuur van 999,9 graden gemeten wordt niet zo groot is.

![](step3.png)

**Opdracht**

- Schrijf een functie die een bestand inleest van het bovenstaande formaat en een nieuw bestand opslaat waar de ontbrekende waarden zijn vervangen door het hierboven aangegeven gemiddelde.

- Je mag ervan uitgaan dat er altijd maar één missende waarde op een rij is, dus nooit twee achter elkaar.

- De functie moet een parameter hebben om aan te geven welke waarde een "missing value" is. De functie kan dan worden aangeroepen met bijvoorbeeld `9999`.

- De functie moet wederom zelf de nodige bestanden openen en weer sluiten.

- Schrijf in de `main` een stukje testcode dat de functie aanroept met als bron `climate-noheader-no2020.txt` en als doel `climate-cleaned.txt`. Run je programma en inspecteer of het resultaat klopt.

Hints:

- Dit is een wat ingewikkelder probleem dan de rest. Je kunt de "readline-technique" uit het boek gebruiken (pagina 181), maar om de missende waarden uit te rekenen heb je toegang nodig tot *drie achtereenvolgende regels*.

- Dat betekent dat je zoals gebruikelijk steeds één regel moet inlezen, maar dat je elke keer de één-na-laatste regel gaat bekijken en zonodig aanpassen. Ook de twee-na-laatste regel heb je hiervoor nodig.

- Je kunt "oude" regels opslaan in variabelen elke keer als je een nieuwe regel inleest.

- Ontwikkel je algoritme hiervoor op papier en analyseer goed of het zou moeten kloppen door te bedenken hoe het door een bestand van 6 regels zou lopen. **Kom langs in het college om met ons aan het algoritme te werken. We zorgen dat je met een werkende strategie aan de slag kunt.**

## Omzetten naar komma's

Tot slot zijn de gegevens in het bestand niet afgescheiden door komma's (`,`) maar door puntkomma's (`;`). Dit is op zich geen groot probleem, maar wij willen specifiek komma's hebben.

**Opdracht**

- Schrijf een functie die een bestand inleest van het bovenstaande formaat en een nieuw bestand opslaat waar de puntkomma's zijn vervangen door komma's.

- De functie moet wederom zelf de nodige bestanden openen en weer sluiten.

- Schrijf in de `main` een stukje testcode dat de functie aanroept met als bron `climate-cleaned.txt` en als doel `climate.csv`. Run je programma en inspecteer of het resultaat klopt.

## Testen

De testcode voor alle functies moet in de `main` staan. Als je het programma runt zouden uiteindelijk alle bestanden `climate-noheader.txt`, `climate-noheader-no2020.txt`, `climate-cleaned.txt` en `climate.csv` achtereenvolgens moeten worden aangemaakt.

We hebben hierboven niet opgegeven hoe je functies moeten heten. Bij de automatische checks gaan we de functies dus niet los testen zoals voorheen, maar we gaan het programma runnen en kijken of de juiste output-bestanden worden aangemaakt. We gebruiken daarvoor de hierboven aangeleverde `climate.txt` maar ook nog een ander testbestand, om te kijken of je programma ook goed werkt als bijvoorbeeld de "missing values" niet met 9999 maar met -9999 worden aangegeven (en andere variaties).

Daarnaast worden alle types gecheckt. Doctests zijn niet zinvol omdat de data uit bestanden wordt gelezen. De doctests worden dus ook niet gecheckt.
