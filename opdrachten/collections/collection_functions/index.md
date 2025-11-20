# Collection Functions

Maak een Python-bestand aan genaamd `collection_functions.py`.

1.  Schrijf een functie genaamd `list_duplicates` die een lijst integers aanneemt en een set teruggeeft met daarin alleen de integers die twee of meer keer voorkomen in de lijst (verzin eerst een paar voorbeelden!).

2.  Gegeven zijn twee sets met daarin de gegevens van woestijnratten. Dat kunnen zijn de namen of anders ID-nummers. De ene set bevat gegevens van vrouwtjes, de andere van mannetjes (het gaat hier om een wetenschappelijk experiment over voortplanting).

    Schrijf een functie genaamd `mating_pairs` die de twee sets aanneemt en dan een *set van pairs* teruggeeft, waarin matchende paren woestijnratten staan. Om de paren samen te stellen neem je met hulp van de methode `pop()` één mannetje en één vrouwtje en die combineer je in een *tuple*.

    Het return type van de functie is `set[tuple[object, object]]`. We gebruiken hier `object` om aan te geven dat er diverse mogelijkheden zijn voor het soort gegevens dat in de tuple staat (zoals dus een integer of een string).

    Tip voor doctesten: de volgorde in een set blijft niet behouden. Maak dus een zo klein mogelijke test om toch de functionaliteit te controleren. Maak twee sets aan met twee elementen, geef die aan de functie. Er zijn dan 4 mogelijke uitkomsten qua volgorde: controleer of de uitkomst één van die 4 uitkomsten is.

3.  In een dictionary zijn de keys per definitie uniek, maar de values (waarden) niet. Schrijf een functie genaamd `count_values` die een dictionary aanneemt en het aantal unieke waarden in de dictionary uitrekent. Stel dat de input `{'red': 1, 'green': 1, 'blue': 2}` is, dan moet de output `2` zijn.

De bedoeling van de volgende opgaven is om te leren hoe je moet loopen met for-loops en dictionaries en zo alle elementen bekijken (zie ook de uitleg op de dicts-pagina). Deze techniek kun je blijven oefenen en hiermee kun je elke opdracht met dictionaries of lists, sets of tuples leren oplossen.

1.  Nadat je een reeks experimenten hebt gedaan heb je een dictionary met daarin hoe vaak je een groeiplek van paddestoelen bent tegengekomen tijdens een inventarisatie. De dictionary is georganiseerd op naam van de soort (ofwel: dat is de key). Voorbeeld:

         {'biefstukzwam': 5, 'gewone oesterzwam': 12, 'gewoon eekhoorntjesbrood': 2, 'porseleinzwam': 22, 'judasoor': 4}

    Schrijf een functie `minst_voorkomende` die zo'n dictionary aanneemt (vermeld het juiste type) en dan de naam van het deeltje teruggeeft dat het minst waarschijnlijk geobserveerd wordt. In bovenstaand geval zou het `'gewoon eekhoorntjesbrood'` zijn.

2.  Schrijf een functie genaamd `tel_dubbele` die een dictionary aanneemt en dan teruggeeft het aantal waarden dat twee of meer keer voorkomt.

3.  Een "genormaliseerde vector" is een vector (lijst waarden) waarvan de waarden samen 1.0 zijn. Schrijf een functie genaamd `is_normal` die een dictionary met willekeurige keys neemt, met waarden tussen 0 en 1. De functie geeft `True` als de waarden dictionary samen 1.0 zijn, anders `False`.

4.  Schrijf een functie `dict_intersect` die twee dictionaries als argumenten krijgt, en een enkele dictionary teruggeeft waarin alléén de key-value pairs staan die in beide dictionaries aanwezig zijn (zowel key als value moeten gelijk zijn!).

5.  Schrijf een functie `get_valuable_letters` die het *aantal* letters uit het Scrabble-alfabet geeft, op basis van een opgegeven bepaalde minimum-waarde (parameter). Als dat minimum 10 is, dan is er maar één letter die voldoet. Het Scrabble-alfabet is een dictionary die je in de functie moet zetten:

        scrabble_points = {
        'a': 1, 'b': 3, 'c': 5, 'd': 2, 'e': 1, 'f': 4, 'g': 3, 'h': 4, 'i': 2, 'j': 4,
        'k': 3, 'l': 3, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 2, 's': 2, 't': 2,
        'u': 4, 'v': 4, 'w': 5, 'x': 8, 'y': 8, 'z': 4}

6.  Schrijf een functie `emmeren` die een lijst van lijsten van integers aanneemt, zoals `[[1,2,3], [3,4], [4,5]]` en een dictionary geeft met als key de lengte van een lijst, en als value een lijst van alle lijsten van die lengte. Het antwoord voor voorgaande zou zijn `{3: [[1, 2, 3]], 2: [[3, 4], [4, 5]]}`.

## Hint

Gebruik wat je uit het boek of van deze site geleerd hebt! Bedenk hoe je methods van de verschillende soorten collection types kunt toepassen en combineren om op je antwoord te komen.
