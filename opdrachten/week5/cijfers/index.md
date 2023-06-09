# Cijfers

Gegeven zijn onderstaande twee bestanden (files), ieder met het
cijfers van 10 studenten in vaste volgorde voor deeltentamen1 en
deeltentamen2. We gaan de eindcijfers voor het vak berekenen waarbij
deeltentamen1 een wegingsfactor van 3 heeft en deeltentamen2 een
wegingsfactor van 1 heeft.

bestand [deeltentamen1.txt](deeltentamen1.txt):

    5.8
    7.3
    6.5
    4.1
    8.5
    6.7
    5.2
    7.0
    8.9
    6.2
    
bestand [deeltentamen2.txt](deeltentamen2.txt):
    
    7.8
    8.3
    4.1
    6.3
    4.7
    3.6
    7.0
    7.3
    8.6
    5.1

## Code

Voor dit doel is programma [multiply_file.py](multiply_file.py) al beschikbaar:

    import sys

    def multiply_file(input_filename: str, multiplier: float, output_filename: str):
        with open(output_filename, "w") as output_file:
            with open(input_filename, "r") as input_file:
                for line in input_file:
                    value = float(line) * multiplier
                    value = round(value, 2) # round to 2 decimals
                    output_file.write(str(value) + '\n')
            
    if __name__ == '__main__':
        # print( sys.argv ) # uncomment to print all command line arguments
        if len(sys.argv) <= 3:
            print("Too few arguments.")
            print("usage:", sys.argv[0], "<input_filename> <multiplier> <output_filename>")
            print("Multiplies all values in <input_filename> with <multiplier> and writes the result to <output_filename>.")
        else:
            input_filename=sys.argv[1]
            multiplier=float(sys.argv[2])
            output_filename=sys.argv[3]
            multiply_file(input_filename,multiplier,output_filename)

Bij het uitvoeren van dit programma kunnen [command line
arguments](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
worden meegegeven waarmee je informatie aan een programma kan geven,
anders dan met de `input()` functie. Dit voorbeeld laat zien hoe we
alle waarden in invoerbestand 'deeltentamen1.txt' kunnen inlezen,
vermenigvuldingen met '100.0', en wegschrijven naar uitvoerbestand
'voorbeeld.txt':

    python multiply_file.py deeltentamen1.txt 100.0 voorbeeld.txt
    
Als we hierna uitvoerbestand 'voorbeeld.txt' openen zien we het resultaat:

    580.0
    730.0
    650.0
    410.0
    850.0
    670.0
    520.0
    700.0
    890.0
    620.0

## Opdracht

Gebruik het voorbeeldprogramma 'multiply_file.py' om zelf programma
'add_files.py' te schrijven waarmee we cijfers in twee verschillende
invoerbestanden bij elkaar op kunnen tellen en naar een uitvoerbestand
kunnen schrijven.

Gebruik vervolgens 'multiply_file.py' en 'add_files.py' om de
eindcijfers van het vak te berekenen. Houd daarbij rekening met de
wegingsfactoren. Zorg dat de 10 eindcijfers op volgorde onder elkaar
in bestand 'eindcijfers.txt' komen te staan.

## Programma Opdeling

Soms is het handig om niet 1 programma te schrijven om een probleem op
te lossen, maar om verschillende programma's te schrijven die ieder
een apart deelprobleem oplossen en zo in samenwerking tot de
eindoplossing komen. Bestanden kunnen daarbij goed gebruikt worden om
tussenresultaten in op te slaan en 'command line argument' om
tussenresultaten door te geven aan het volgende programma. Deze
opdracht is daar een eenvoudig voorbeeld van.
