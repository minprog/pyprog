# Reeks

Schrijf een programma dat de *langste aaneengesloten reeks niet-priemgetallen* bepaalt onder de 10,000 en daar een korte samenvatting van geeft.

	# python reeks.py
	De langste reeks niet-priemgetallen onder de 10,000 begint op ... en eindigt bij ...
	De reeks is ... lang.

Lees goed wat er gevraagd wordt: de begin en eindpunten zijn zelf dus *geen* priemgetallen. Onder het getal 100 moet het antwoord zijn:

	# python reeks.py
	De langste reeks niet-priemgetallen onder de 100 begint op 90 en eindigt bij 96
	De reeks is 7 lang.

De opdracht luidt om de langste reeks te vinden onder het getal 10,000.

## Achtergrond

Bepaal altijd met pen en papier je strategie en ga dus niet gelijk tikken. De 5--10 minuten die je hieraan besteedt verdien je dik terug tijdens het omzetten naar programmacode.

Om het idee van de reeks niet-priemgetallen goed te begrijpen, schrijf je bijvoorbeeld de eerste tien priemgetallen op papier en bekijk steeds de onderlinge afstand: tussen 2 en 3 is het verschil maar één, terwijl het verschil tussen 13 en 17 vier is (wat dus betekent dat er 3 opeenvolgende getallen tussen zitten die niet-priem zijn, namelijk 14, 15 en 16).

## Specificatie

- Maak een programma genaamd `reeks.py` en zorg dat het volgens bovenstaand voorbeeld de juiste informatie uitprint.

- Zet bovenaan je programma `from priemgetal import is_priem` zodat je de functie `is_priem` van de vorige opgave kunt gebruiken.

- Zorg dat je programma twee functies definieert:

	1. `zoek_langste_reeks()`, een functie met één argument, `N`, die de langste reeks niet-priemgetallen onder `N` vindt en de grenzen teruggeeft. Gebruik `return onder, boven` om de onder- en bovengrens te returnen.
	2. `print_boodschap()`, een functie met als argumenten de eerder gedefinieerde `N` plus een reeds gevonden onder- en bovengrens. De functie doet niets anders dan de uitslag printen zoals in het voorbeeld bovenaan.

- De functies mogen geen lijsten gebruiken.

- Stap (loop) door alle priemgetallen heen en bepaal telkens hoe lang de reeks niet-priemgetallen is tussen het huidige en het vorige priemgetal. Houd bij wat de langste reeks is in een aparte variabele.

- Roep in je `main`-code de functie `zoek_langste_reeks()` aan met als argument `10000`. Daarna geef je de uitkomst door aan `print_boodschap()`. Zorg dat je output er netjes uitziet en dat we als gebruiker iets aan de informatie hebben.

## Testen

Loop nu de specificatie bovenaan de opdracht goed door en zorg dat je programma precies zo werkt als daar beschreven is. Test zelf met 100 en met 10,000.

Nu ben je klaar om te testen:

	checkpy reeks
