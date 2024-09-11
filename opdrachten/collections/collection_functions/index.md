# Collection Functions

Maak een Python-bestand aan genaamd `collection_functions.py`.

1.  Schrijf een functie genaamd `find_dups` die een lijst integers aanneemt en een set teruggeeft met daarin alleen de integers die twee of meer keer voorkomen in de lijst (verzin eerst een paar voorbeelden!).

2.  Gegeven zijn twee sets met daarin de gegevens van woestijnratten. Dat kunnen zijn de namen of anders ID-nummers. De ene set bevat gegevens van vrouwtjes, de andere van mannetjes (het gaat hier om een wetenschappelijk experiment over voortplanting).

    Schrijf een functie genaamd `mating_pairs` die de twee sets aanneemt en dan een *set van pairs* teruggeeft, waarin matchende paren woestijnratten staan. Om de paren samen te stellen neem je met hulp van de methode `pop()` één mannetje en één vrouwtje en die combineer je in een *tuple*.

    Het return type van de functie is `set[tuple[object, object]]`. We gebruiken hier `object` om aan te geven dat er diverse mogelijkheden zijn voor het soort gegevens dat in de tuple staat (zoals dus een integer of een string).

    Tip voor doctesten: de volgorde in een set blijft niet behouden. Maak dus een zo klein mogelijke test om toch de functionaliteit te controleren. Maak twee sets aan met twee elementen, geef die aan de functie. Er zijn dan 4 mogelijke uitkomsten qua volgorde: controleer of de uitkomst één van die 4 uitkomsten is.

3.  In een dictionary zijn de keys per definitie uniek, maar de values (waarden) niet. Schrijf een functie genaamd `count_values` die een dictionary aanneemt en het aantal unieke waarden in de dictionary uitrekent. Stel dat de input `{'red': 1, 'green': 1, 'blue': 2}` is, dan moet de output `2` zijn.

De bedoeling van de volgende opgaven is om te leren hoe je moet loopen met for-loops en dictionaries en zo alle elementen bekijken (zie ook de uitleg op de dicts-pagina). Deze techniek kun je blijven oefenen en hiermee kun je elke opdracht met dictionaries of lists, sets of tuples leren oplossen. Het is af te raden om te zoeken naar "slimme" manieren om de opgaven op te lossen, want die manieren kun je vaak niet op nieuwe opgaven toepassen en zijn ook lastiger te onthouden.

1.  Nadat je een reeks experimenten hebt gedaan heb je een dictionary met daarin de "waarschijnlijkheid van detectie" van verschillende soorten subatomaire deeltjes.

    In de dictionary zijn de keys de namen van de deeltjes, en de waarden zijn de waarschijnlijkheden. Bijvoorbeeld `{'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}`.

    Schrijf een functie `least_prob` die zo'n dictionary aanneemt (vermeld het juiste type) en dan de naam van het deeltje teruggeeft dat het minst waarschijnlijk geobserveerd wordt. In bovenstaand geval zou het 'meson' zijn.

2.  Schrijf een functie genaamd `count_duplicates` die een dictionary aanneemt en dan teruggeeft het aantal waarden dat twee of meer keer voorkomt.

3.  Een "balanskleur" is een kleur waarvan de waarden voor rood, groen en blauw samen 1.0 zijn. Schrijf een functie genaamd `is_balanced` die een dictionary met de keys 'R', 'G' en 'B' neemt met waarden tussen 0 en 1. De functie geeft `True` als de dictionary een balanskleur beschrijft, anders `False`.

4.  Schrijf een functie `dict_intersect` die twee dictionaries als argumenten krijgt, en een enkele dictionary teruggeeft waarin alléén de key-value pairs staan die in beide dictionaries aanwezig zijn (zowel key als value moeten gelijk zijn!).

## Hint

Gebruik wat je uit het boek of van deze site geleerd hebt! Bedenk hoe je methods van de verschillende soorten collection types kunt toepassen en combineren om op je antwoord te komen.
