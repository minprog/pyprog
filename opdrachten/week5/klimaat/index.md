# Klimaatanalyse

![](../eca2csv/temperature.png)

Tijd voor analyse. Schrijf een programma genaamd `klimaat.py` dat een bestand `climate.csv` kan inlezen en de volgende analyse uitprinten:

    KLIMAATANALYSE

    Databestand
    -----------
    Bestandsnaam: climate.csv
    Eerste datum: 01-01-1901
    Laatste datum: 31-12-2019

    Basisinformatie
    ---------------
    Laagste temperatuur: -11.4° op 26-01-1942
    Hoogste temperatuur: 37.5° op 25-07-2019
    Gemiddelde temperatuur: 13.6°

    Extremen 2010-2019
    ------------------
    In 2010 varieerde de temperatuur tussen -6.1° op 02-12 en 34.4° op 09-07
    In 2011 varieerde de temperatuur tussen -0.1° op 31-01 en 32.2° op 28-06
    In 2012 varieerde de temperatuur tussen -5.1° op 03-02 en 33.0° op 19-08
    In 2013 varieerde de temperatuur tussen -2.8° op 17-01 en 34.0° op 02-08
    In 2014 varieerde de temperatuur tussen 1.0° op 03-12 en 32.9° op 19-07
    In 2015 varieerde de temperatuur tussen -1.3° op 23-01 en 33.1° op 01-07
    In 2016 varieerde de temperatuur tussen -0.8° op 29-12 en 32.9° op 20-07
    In 2017 varieerde de temperatuur tussen -1.9° op 18-01 en 31.9° op 27-05
    In 2018 varieerde de temperatuur tussen -4.6° op 28-02 en 35.7° op 26-07
    In 2019 varieerde de temperatuur tussen -1.1° op 24-01 en 37.5° op 25-07

## Aanwijzingen

- Gebruik als input de file `climate.csv` die je hebt gegenereerd in de vorige opdracht.

- Je moet alle data in een variabele inlezen voor verdere verwerking.

- Het is niet toegestaan alle informatie in één lange functie te berekenen. Dit kan enigszins efficiënt zijn maar is funest voor de leesbaarheid van de code. Zorg dat je elke analyse in een aparte functie uitvoert.

- Bedenk welke delen je nog meer in aparte functies kunt zetten.

- Schrijf doctests en zorg dat alle types op orde zijn.

## Algorithmische tips

- Veel van deze opdracht gaat over het zoeken naar kleinste en grootste waarden in alle data of een deel daarvan. Het boek behandelt dit idee in de sectie "Processing Whitespace-Delimited Data" (p. 192).

- Het is helemaal prima om lelijke trucjes te gebruiken voor het doorspitten van de data. Zorg eerst dat je het werkend krijgt en daarna kun je alles altijd nog netter maken.
