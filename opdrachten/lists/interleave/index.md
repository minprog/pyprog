# Interleave

Schrijf een functie `interleave` met uitgebreide doctests die twee lijsten aanneemt en een nieuwe lijst maakt waarin de elementen uit de twee originele lijsten afwisselend zijn opgenomen. De functie moet óók een parameter `keep` aannemen (bool). Deze parameter bepaalt of eventuele overtollige elementen uit een van de lijsten worden weggegooid of behouden: het kan namelijk zijn dat de lijsten niet even lang zijn en dat je elementen uit de langste lijst niet meer kwijt kunt. Als `keep == True` dan moeten deze elementen gewoon aan het eind van de resultaatlijst worden toegevoegd.

## Tip

Schrijf de functie eerst zonder de parameter en alleen voor lijsten die even lang zijn. Bouw de complexiteit op zodra je weet dat dat eerste stuk perfect werkt.

## Algoritme

Formuleer een compact algoritme waarin je gebruik maakt van de basisoperaties van Python.

Bedenk vooraf:

- wat de input is
- hoe het algoritme er globaal uit moet zien (loops, variabelen)
- wat er teruggegeven wordt en hoe je dat opbouwt (variabele)
- of er nog bijzondere gevallen zijn om rekening mee te houden

<details markdown="1"><summary markdown="span">Weet je niet waar te beginnen?</summary>
Dit zijn enkele elementen die je bij deze opdracht kunt gebruiken:

- eigenlijk gewoon een simpele `for`-loop met een index om te tellen
- loop zo lang als de *kortste* lijst lang is
- daarna kun je nog een `for`-loop gebruiken om het restje van de langste lijst te kopiëren
</details>
