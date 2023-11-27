# Collection Functions 2

Maak een Python-bestand aan genaamd `collection_functions2.py`. Maak de volgende opgaven.

De bedoeling van deze opgaven is om te leren hoe je moet loopen met for-loops en dictionaries en zo alle elementen bekijken (zie ook de uitleg op de dicts-pagina). Deze techniek kun je blijven oefenen en hiermee kun je elke opdracht met dictionaries of lists, sets of tuples leren oplossen. Het is af te raden om te zoeken naar "slimme" manieren om de opgaven op te lossen, want die manieren kun je vaak niet op nieuwe opgaven toepassen en zijn ook lastiger te onthouden.

1.  Nadat je een reeks experimenten hebt gedaan heb je een dictionary met daarin de "waarschijnlijkheid van detectie" van verschillende soorten subatomaire deeltjes.

    In de dictionary zijn de keys de namen van de deeltjes, en de waarden zijn de waarschijnlijkheden. Bijvoorbeeld `{'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}`.

    Schrijf een functie die zo'n dictionary aanneemt (vermeld het juiste type) en dan de naam van het deeltje teruggeeft dat het minst waarschijnlijk geobserveerd wordt. In bovenstaand geval zou het 'meson' zijn.

2.  Schrijf een functie genaamd `count_duplicates` die een dictionary aanneemt en dan teruggeeft het aantal waarden dat twee of meer keer voorkomt.

3.  Een "balanskleur" is een kleur waarvan de waarden voor rood, groen en blauw samen 1.0 zijn. Schrijf een functie genaamd `is_balanced` die een dictionary met de keys 'R', 'G' en 'B' neemt met waarden tussen 0 en 1. De functie geeft `True` als de dictionary een balanskleur beschrijft, anders `False`.

4.  Schrijf een functie `dict_intersect` die twee dictionaries als argumenten krijgt, en een enkele dictionary teruggeeft waarin alléén de key-value pairs staan die in beide dictionaries aanwezig zijn (zowel key als value moeten gelijk zijn!).

## Hint

Gebruik alleen wat je uit het boek of van deze site geleerd hebt! Bedenk hoe je methods van de verschillende soorten collection types kunt toepassen en combineren om op je antwoord te komen.
