# Compress

Teksten en lijsten met getallen kunnen vaak eenvoudig "gecomprimeerd" worden, dus kleiner gemaakt, maar zonder informatie te verliezen. De kunst is om een vaste manier te vinden om de originele data weer terug te krijgen.

Eén manier is "run-length encoding" waarbij je gebruik maakt van de mogelijkheid dat er vaak dezelfde elementen elkaar opvolgen (bijvoorbeeld in een lijst van metingen waarin een groot deel van de metingen 0 is).

Bij run-length encoding vervang je een reeks gelijke elementen door een *paar* `(element, aantal)`. Stel dat je 10 nullen achter elkaar hebt, dan kan het eruit zien als `(0, 10)`.

In deze module werken we met lijsten dus gaat de encryptie-functie een lijst opleveren met daarin ook weer lijsten. Elk van die interne lijsten is zo'n "paar", bijvoorbeeld `[0, 10]`.

## Opdracht

Schrijf een functie `compress` die een lijst met integers aanneemt en comprimeert naar een lijst met paren van integers.

Schrijf een functie `decompress` die een lijst van lijsten met twee integers aanneemt en decomprimeert naar een lijst met integers.

Maak hierbij uitgebreide doctests.

## Programma

Maak een hoofdprogramma dat 1000 keer een lijst van 1000 integers genereert. Elke lijst wordt door `compress` gehaald en het programma houdt bij wat de [compressie-ratio](https://en.wikipedia.org/wiki/Data_compression_ratio) van elk is. Uiteindelijk print het programma de gemiddelde compressie-ratio voor alle 1000 experimenten.
