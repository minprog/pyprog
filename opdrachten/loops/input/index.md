# Functies: Input

In deze opdracht schrijf je een Python-module `int_input.py` met daarin vier functies.

Maak ook een `if-name-is-main` waarin je elk van de functies aanroept zodat je ze kunt uittesten:

    if __name__ == '__main__':
        get_positive_int()
        get_any_int_but_0()
        get_min_int(100)
        get_two_different_ints()

Zet deze onderaan je bestand.

## Input-functies

In Python hebben we de functie `input()` maar deze is vrij eenvoudig. Als de gebruiker van het programma iets verkeerd intikt wordt hier verder niks mee gedaan.

In deze opgaven ga je gespecialiseerde input-functies schrijven. Het doel is om te oefenen met het maken van input-loops. Die loops kun je kopiëren in andere programma's.

Controleren of een invoer een geheel getal is is te lastig voor deze opgaven. Dat doen we niet.

Een voorbeeld van gespecialiseerde input-functie:

    def get_odd_number() -> int:
        """
        Deze functie vereist een oneven integer.
        """
        result = int(input("Enter an odd int: "))
        while result % 2 == 0:
            result = int(input("Enter an odd int: "))
        return result

## Positief geheel getal

Schrijf een functie `get_positive_int` die om input vraagt. Je mag ervan uitgaan dat de gebruiker wel een integer intikt, dus geen tekst of kommagetallen. Maar je moet in de functie wél controleren of er sprake is van een positief getal (1 of hoger). Als dat niet zo is, wordt opnieuw om input gevraagd.

## Alles behalve 0

Schrijf een functie `get_any_int_but_0` die om input vraagt. Je mag ervan uitgaan dat de gebruiker wel een integer intikt, dus geen tekst of kommagetallen. Maar je moet in de functie wél controleren of er sprake is van een ander getal dan `0`. Als dat niet zo is, wordt opnieuw om input gevraagd.

## Minimaal

Schrijf een functie `get_min_int` die om input vraagt. Er is een parameter `minimum` die aangeeft wat het minimale getal is dat ingevoerd moet worden. Je mag ervan uitgaan dat de gebruiker wel een integer intikt, dus geen tekst of kommagetallen. Maar je moet in de functie wél controleren of het ingevoerde getal voldoet aan het minimum. Als dat niet zo is, wordt opnieuw om input gevraagd.

## Twee verschillende etallen

Schrijf een functie `get_two_different_ints` die *twee keer* om input vraagt. Je mag ervan uitgaan dat de gebruiker wel twee keer een integer intikt, dus geen tekst of kommagetallen. Maar je moet in de functie wél controleren of de getallen niet gelijk zijn. Als dat toch zo is, wordt opnieuw om input gevraagd (wederom twee getallen).
