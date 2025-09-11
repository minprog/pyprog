# Functies: Collatz

In deze opdracht schrijf je een Python-module met daarin twee functies. Een `main` wordt hier niet gevraagd.

## De Collatz-reeks

Een Collatz-reeks begint bij een getal $n$ en eindigt altijd bij $1$. De progressie vormt zich als volgt:

- Als getal $n$ even is (dus deelbaar door 2) dan wordt het door twee gedeeld en dat is het volgende getal.
- Als het getal oneven is dan vermenigvuldig je het met 3 en telt er 1 bij op.

Een voorbeeld: 3 wordt 10 wordt 5 wordt 16 wordt 8 wordt 4 wordt 2 wordt 1.

## Printen

Schrijf een functie `print_collatz` die gegeven een parameter `n` de bijbehorende Collatz-reeks print. Op elke regel komt één getal en de eerste `n` wordt ook geprint. Na het getal 1 eindigt het programma.

Werk het eerst uit op papier in pseudocode; met name de variabelen en loops die je nodig hebt.

## Tellen

Schrijf een functie `collatz_length` die gegeven een parameter `n` de lengte van de bijbehorende Collatz-reeks print. Hier worden de Collatz-getallen dus *niet* geprint, maar alleen de totale lengte.

Werk het eerst uit op papier in pseudocode; met name de variabelen en loops die je nodig hebt.

Hints:

- Je kunt niet vooraf berekenen hoe lang de reeks gaat zijn, dus je moet de reeks berekenen en in de tussentijd een teller bijhouden.

- Omdat je de reeks wel moet doorlopen kun je de functie baseren op de code van `print_collatz`.
