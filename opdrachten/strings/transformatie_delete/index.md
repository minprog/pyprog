# Tekens verwijderen uit een string

Bij deze oefeningen ga je tekens verwijderen uit een string. Of beter gezegd: je gaat stap-voor-stap een string kopiëren en dan *sommige tekens weglaten*.

Maak een Python-module genaamd `string_transformatie_delete.py`. Schrijf de volgende functies met doctests. Je maakt voor deze opgave geen `main`, maar wel doctests!

## Verwijder letter 'n'

Schrijf een functie `verwijder_n` die alle letters `n` verwijdert uit een string en deze teruggeeft.

    def verwijder_n(s: str) -> str:
        ...

Bedenk zelf een paar voorbeelden.

Het is niet mogelijk om letterlijk delen van een string te _verwijderen_. Strings zijn niet mutable, ofwel "aanpasbaar". Je zult daarom een nieuwe string moeten opbouwen op basis van de gegeven string `s` en die nieuwe string returnen.

## Verwijder letter 'n' aan eind van elk woord

Schrijf een functie `verwijder_n_eind` die alle letters `n` verwijdert uit een string --- maar alleen die aan het eind van een woord staan --- en deze teruggeeft.

    def verwijder_n_eind(s: str) -> str:
        ...

Bedenk zelf een paar voorbeelden.

Hiervoor moet je _vooruit kijken_. Je moet een loop maken op basis van posities, zodat je het teken op elke positie kan bekijken (`pos`) maar ook de letter op de volgende positie (`pos + 1`). Let wel op, dat als je bij het einde van de string bent (`pos = len(s)-1`) je niet naar de volgende positie mag kijken.

    for pos in range(len(s)):
        ...

## Verwijder letter 'n' aan begin van elk woord

Schrijf een functie `verwijder_n_begin` die alle letters `n` verwijdert uit een string --- maar alleen die aan het begin van een woord staan --- en deze teruggeeft.

    def verwijder_n_begin(s: str) -> str:
        ...

Bedenk zelf een paar voorbeelden.

Hiervoor moet je _achteruit kijken_. Je moet een loop maken op basis van posities, zodat je het teken op elke positie kan bekijken (`pos`) maar ook de letter op de vorige positie (`pos - 1`). Let wel op dat je niet positie `-1` bekijkt als je op `pos = 0` bent.

    for pos in range(len(s)):
        ...
