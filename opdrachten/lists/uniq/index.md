# Uniq

Schrijf een functie `uniq` met uitgebreide doctests die een lijst aanneemt en een nieuwe lijst teruggeeft waarin dubbele elementen zijn verwijderd. De originele lijst mag **niet** veranderd worden.

## Algoritme

Een globaal opzetje:

0. Maak een nieuwe (lege) lijst aan om het resultaat in op te slaan.
1. Loop door alle posities van de lijst (dus met een positie-teller).
2. Als je bij een element aankomt, check of het als voorkomt in de nieuwe lijst.
    - Zo ja, sla over.
    - Zo niet, voeg het element toe aan de nieuwe lijst.
3. Zodra je alle elementen langs bent heb je alle unieke elementen gekopieerd.

Bedenk zelf vooraf:

- wat de input is
- hoe het algoritme er globaal uit moet zien (wat voor loops, welke variabelen)
- wat er teruggegeven wordt (voorbeelden!)
- of er nog bijzondere gevallen zijn om rekening mee te houden

## Main?

Je schrijft geen `main` voor deze opdracht. Als je nog extra testcode wil hebben dan moet deze wel in een if-name-is-main staan.
