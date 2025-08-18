# Yell

1. Schrijf een functie die een string aanneemt en een versie teruggeeft waarin alle uitroeptekens verdubbeld zijn. Oh, en ook alle vraagtekens.

2. Als deze gevalideerd is met doctests, voeg dan een `main` toe zodat je het programma kunt runnen, en een woord opgeven dat dan met verdubbelde uitroeptekens wordt uitgeprint (met hulp van de functie).

## Algoritme

Tekens in een string toevoegen kan niet, zelfs niet als je precies weet waar, dus het is nodig om een nieuwe string aan te maken en stap-voor-stap te vullen met tekens, waarbij je de `?` en `!` verdubbelt.

Bedenk vooraf:

- wat de input is
- hoe het algoritme er globaal uit moet zien (loops, variabelen)
- wat er teruggegeven wordt en hoe je dat opbouwt (variabele)
- of er nog bijzondere gevallen zijn om rekening mee te houden

## Voorbeeld

Drie voorbeelden van het runnen van het programma. Er wordt steeds een tekst ingetikt en dan verschijnt op de volgende regel de output.

    $ python yell.py
    Can't shake it off of me!
    Can't shake it off of me!!

    $ python yell.py
    Who the hell put the muffins the freezer?
    Who the hell put the muffins the freezer??

    $ python yell.py
    Cringe? CRINGE!
    Cringe?? CRINGE!!
