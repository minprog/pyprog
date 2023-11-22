# Collection Functions

Maak een Python-bestand aan genaamd `collection_functions.py`.

1.  Schrijf een functie genaamd `find_dups` die een lijst integers aanneemt en een set teruggeeft met daarin alleen de integers die twee of meer keer voorkomen in de lijst (verzin eerst een paar voorbeelden!).

2.  Gegeven zijn twee sets met daarin de gegevens van woestijnratten. Dat kunnen zijn de namen of anders ID-nummers. De ene set bevat gegevens van vrouwtjes, de andere van mannetjes (het gaat hier om een wetenschappelijk experiment over voortplanting).

    Schrijf een functie genaamd `mating_pairs` die de twee sets aanneemt en dan een *set van pairs* teruggeeft, waarin matchende paren woestijnratten staan. Om de paren samen te stellen neem je met hulp van de methode `pop()` één mannetje en één vrouwtje en die combineer je in een *tuple*.

    Het return type van de functie is `set[tuple[object, object]]`. We gebruiken hier `object` om aan te geven dat er diverse mogelijkheden zijn voor het soort gegevens dat in de tuple staat (zoals dus een integer of een string).

3.  In een dictionary zijn de keys per definitie uniek, maar de values (waarden) niet. Schrijf een functie genaamd `count_values` die een dictionary aanneemt en het aantal unieke waarden in de dictionary uitrekent. Stel dat de input `{'red': 1, 'green': 1, 'blue': 2}` is, dan moet de output `2` zijn.

## Hint

Gebruik alleen wat je uit het boek geleerd hebt! Bedenk hoe je methods van de verschillende soorten collection types kunt toepassen en combineren om op je antwoord te komen.
