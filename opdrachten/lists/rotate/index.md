# Rotate

Schrijf een functie `rotate` met uitgebreide doctests die een lijst aanneemt en de inhoud met één stap draait. Dat wil zeggen dat alle elementen naar links verschuiven. Het eerste element van de lijst komt achteraan. De lijst moet aangepast worden en er is dus geen `return`.

## Code

Twee opmerkingen over de code:

- Gebruik nooit `list` als variabelenaam, want dit is al de naam van een **type**.

- Voor een functie als `rotate` is het niet van belang wat het type is van de elementen van de lijst zelf. Je moet echter wel een type opgeven. Gebruik `object` als het alles mag zijn:

        def rotate(lst: list[object]) -> None:

## Doctests

Hoe test je een functie die geen `return` doet en ook niet `print`? Dat ziet er zo uit:

    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]

De eerste twee regels zijn de setup: een lijst aanmaken en de functie aanroepen. De regel daarna is de echte test: je geeft alleen de variabelenaam, en je zegt gewoon wat het moet zijn. Begrijp je het niet? Check met je docent!

## Algoritme

Formuleer een compact algoritme waarin je gebruik maakt van de basisoperaties van Python.

In dit geval mag je alleen elementen kopiëren van de ene naar de andere plek! Dus je moet echt elk element "verschuiven" naar de plek ernaast. Voorbeeld van een element verplaatsen: `lst[2] = lst[3]`.

Bedenk vooraf:

- wat de input is
- hoe het algoritme er globaal uit moet zien (loops, variabelen)
- wat er teruggegeven wordt en hoe je dat opbouwt (variabele)
- of er nog bijzondere gevallen zijn om rekening mee te houden

<details markdown="1"><summary markdown="span">Weet je niet waar te beginnen?</summary>
Dit zijn enkele elementen die je bij deze opdracht kunt gebruiken:

- een `for`-loop met index
</details>

## Main?

Je schrijft geen `main` voor deze opdracht. Als je nog extra testcode wil hebben dan moet deze wel in een if-name-is-main staan.
