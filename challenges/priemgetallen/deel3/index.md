# Goldbach

Schrijf een programma dat laat zien dat het vermoeden van Goldbach correct is voor de even getallen (groter dan 2) tot en met 1000.

	# python goldbach.py
	16 = ...
	18 = 5 + 13 
	20 = 3 + 17 
	22 = 5 + 17
	24 = ...

## Achtergrond

Het vermoeden van Goldbach is een van de oudste onopgeloste problemen in de wiskunde. Goldbach stelde:

*"Elk even getal groter dan 2 kan geschreven worden als de som van twee priemgetallen."*

Een priemgetal mag hierbij ook twee keer gebruikt worden (6 = 3 + 3). Hoewel dit vermoeden inderdaad blijkt te kloppen voor alle getallen tot $$4\cdot10^{18}$$ is er nog altijd geen analytisch bewijs voor het vermoeden. 

Misschien onverwacht: een computer blijkt ongeschikt om het vermoeden te bewijzen (je kunt immers niet tot oneindig tellen); maar je zou het vermoeden wel kunnen ontkrachten door een even getal te identificeren dat niet te schrijven is als de som van twee priemgetallen. Dat zou een tegenbewijs zijn. Spoiler: ook dat is nog niet gevonden.

We gaan ons steentje bijdragen in deze zoektocht door systematisch de even getallen door te nemen en te kijken of de stelling van Goldbach klopt voor elk getal.

## Specificatie

Laat met een programma **goldbach.py** zien dat alle even getallen tot en met 1000 inderdaad te schrijven zijn als de som van twee priemgetallen. Concreet: laat voor elk even getal ook *expliciet* zien (op het scherm) dat het te schrijven is als de som van twee priemgetallen, zoals in het voorbeeld hierboven. Schrijf je programma in een functie die je aanroept onderaan je code.

Nog belangrijker is natuurlijk als je een getal vindt dat *niet* aan het vermoeden van Goldbach voldoet. Zorg dat jouw programma zo'n ontdekking duidelijk op het scherm aangeeft. Bingo!

## Hints

- Bepaal altijd met pen en papier je strategie en ga dus niet gelijk tikken. De 5-10 minuten die je hieraan besteedt verdien je dik terug tijdens het omzetten naar programmacode.

- Gebruik in ieder geval de functie `is_priem()` via een `import`, zoals bij de vorige opgave.

- Het is daarnaast de bedoeling om je programma in verschillende functies op te delen.

- Zet in je `main` alleen maar de opdracht om een functie aan te roepen met het getal `1000` als argument, zodat de betreffende functie stopt na 1000 even getallen. De functie zou echter ook moeten werken als we 1010 getallen willen nalopen, of een ander aantal.

## Testen

Loop nu de specificatie bovenaan de opdracht goed door en zorg dat je programma precies zo werkt als daar beschreven is.

Nu ben je klaar om te testen:

	checkpy goldbach
