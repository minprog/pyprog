# Merge lists

Schrijf een functie `merge_lists` die twee gesorteerde lijsten van integers samenvoegt in een nieuwe lijst, die eveneens gesorteerd is.

Het gaat altijd om lijsten die zelf al gesorteerd zijn, zoals bijvoorbeeld `[1, 2, 5]` en `[4, 5, 6]`. Als je die twee opgeeft bij deze functie wordt het resultaat daarom `[1, 2, 4, 5, 5, 6]`.

De procedure:

- Stel: de *gezamenlijke* lengte van de lijsten is X. Gebruik een loop die stopt als je X elementen hebt toegevoegd aan de nieuwe lijst. Je loop mag dus maximaal X stappen nemen!

- Stel: de lijsten heten A en B. Je moet bij elke stap beslissen of je een element van A of van B toevoegt aan de nieuw te maken lijst.

- Je moet tellers maken die bijhouden hoeveel tekens je al uit A hebt gepakt en hoeveel tekens uit B. Die tellers geven dus aan *waar je bent*.

Vergeet de doctests niet.
