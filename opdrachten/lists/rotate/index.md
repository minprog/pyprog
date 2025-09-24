# Rotate

Schrijf een functie `rotate` met uitgebreide doctests die een lijst aanneemt en de inhoud met één stap draait. Dat wil zeggen dat alle elementen naar links verschuiven. Het eerste element van de lijst komt achteraan. De lijst moet aangepast worden en er is dus geen `return`.

## Code

Twee opmerkingen over de code:

- Gebruik nooit `list` als variabelenaam, want dit is al de naam van een **type**.

- Voor een functie als `rotate` is het niet van belang wat het type is van de elementen van de lijst zelf. Je moet echter wel een type opgeven. Gebruik `object` als het alles mag zijn:

        def rotate(lst: list[object]) -> None:

## Algoritme

Formuleer een compact algoritme waarin je gebruik maakt van de basisoperaties van Python.

Bedenk vooraf:

- wat de input is
- hoe het algoritme er globaal uit moet zien (loops, variabelen)
- wat er teruggegeven wordt en hoe je dat opbouwt (variabele)
- of er nog bijzondere gevallen zijn om rekening mee te houden
