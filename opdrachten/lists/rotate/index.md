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

<details markdown="1"><summary markdown="span">Weet je niet waar te beginnen?</summary>
Dit zijn enkele elementen die je bij deze opdracht kunt gebruiken:

- een `for`-loop met index
- voorbeeld van een element verplaatsen: `lst[2] = lst[3]`
- "alle elementen naar links verschuiven" moet je echt zo doen
</details>

## Main?

Je schrijft geen `main` voor deze opdracht. Als je nog extra testcode wil hebben dan moet deze wel in een if-name-is-main staan.
