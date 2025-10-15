# Functies: Schrikkel

In deze opdracht schrijf je een Python-module met daarin drie functies. Een `main` wordt hier niet gevraagd.

## Schrikkeljaren

Eerder heb je al een functie `is_schrikkel` geschreven die bepaalt of een enkel jaartal een schrikkeljaar is. Kopieer deze functie in een nieuwe module genaamd `schrikkel_functies.py`.

## Tellen

Schrijf een functie `tel_schrikkeljaren` die gegeven twee parameters `begin` en `eind` telt hoeveel schrikkeljaren zich tussen deze twee jaartallen bevinden. Tel de jaren `begin` en `eind` ook mee indien van toepassing.

    def tel_schrikkeljaren(begin: int, eind: int) -> int:

Gebruik in de functie een `for`-loop die precies van `begin` tot en met `eind` loopt (inclusief).

## n-de Schrikkeljaar

Schrijf een functie `nde_schrikkeljaar_vanaf` die gegeven twee parameters `begin` en `n`  het n-de schrikkeljaar geeft, geteld vanaf het jaar `begin`. Als `begin` een schrikkeljaar is tel je die ook mee.

Dit is een beetje een puzzeltje. Werk het eerst uit op papier in pseudocode; met name de variabelen en loops die je nodig hebt.
