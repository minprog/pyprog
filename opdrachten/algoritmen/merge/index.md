# Merge lists

Schrijf een functie `merge_lists` die op de volgende manier twee lijsten van integers samenvoegt in een nieuwe lijst. Bijvoorbeeld `[1, 2, 5]` en `[4, 5, 6]` wordt samen `[1, 2, 4, 5, 5, 6]`.

- De originele lijsten moeten reeds *gesorteerd zijn*. Dat is een aanname die je mag doen voor je functie, die de functie simpeler maakt. Voor de doctests moet je dus ook gesorteerde lijsten aanleveren.

- Stel: de gezamenlijke lengte van de lijsten is X. Gebruik een loop die stopt als je X elementen hebt toegevoegd aan de nieuwe lijst.

- De uiteindelijke lijst moet ook gesorteerd zijn. Stel: de lijsten heten A en B. Je moet elke stap zorgvuldig kiezen of je een element van A of van B toevoegt aan de lijst, zodat de nieuwe lijst ook gesorteerd blijft.

- Je loop mag maximaal X stappen nemen!
