# Cijfers

Met 'command line arguments' kunnen we informatie aan een programma
geven zonder dat we de `input()` functie gebruiken. Programma
[command_line_arguments.py](command_line_arguments.py) laat zien hoe
dit werkt. Dit programma import eerst `sys` en print vervolgens de lijst
`sys.argv` welke alle 'command line arguments' bevat:

```python
import sys

print( sys.argv )
```

Als we dit programma nu (in de 'command line' of 'shell') starten en
daarachter bijvoorbeeld "aap noot mies" als argumenten meegeven:

```console
$ python command_line_arguments.py aap noot mies
['command_line_arguments.py', 'aap', 'noot', 'mies']
```

dan wordt in het programmma de lijst met strings
['command_line_arguments.py', 'aap', 'noot', 'mies'] geprint. Het
eerste element in de `sys.argv` lijst is de naam van het programma
gevolgd door wat we daar achter als argumenten meegeven. Op deze
manier kunnen we dus vooraf bij de start van het programma al
informatie meegeven zodat in veel gevallen in het programma geen
`input()` functie meer nodig om informatie aan de gebruiker te vragen.

## Gemiddelde Cijfers Berekenen

We gaan 'command line arugments' gebruiken om gemiddelde cijfers van
studenten te berekenen. Gegeven zijn onderstaande twee bestanden,
ieder met het cijfers van 10 studenten in vaste volgorde voor
respectievelijk deeltentamen1 en deeltentamen2. De cijfers van
deeltentamen1 hebben een wegingsfactor van 3 terwijl en cijfers van
deeltentamen2 een wegingsfactor van 1 hebben.

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

## Voorbeeldprogramma

Voor dit doel is programma [multiply_file.py](multiply_file.py) al
beschikbaar:

```python
import sys

def multiply_file(input_filename: str, multiplier: float, output_filename: str):
    with open(output_filename, "w") as output_file:
        with open(input_filename, "r") as input_file:
            for line in input_file:
                value = float(line) * multiplier
                value = round(value, 2)  # round to max 2 decimals
                output_file.write(str(value) + '\n')

if __name__ == '__main__':
    if len(sys.argv) <= 3: # not enough command line arguments given
        print("Too few command line arguments.")
        print("usage:", sys.argv[0], "<input_filename> <multiplier> <output_filename>")
        print("Multiplies all values in <input_filename> with <multiplier> and writes the result to <output_filename>.")
    else:
        input_filename = sys.argv[1]    # read 'input_filename' from the command line arguments
        multiplier = float(sys.argv[2]) # read 'multiplier' from the command line arguments
        output_filename = sys.argv[3]   # read 'output_filename' from the command line arguments
        multiply_file(input_filename, multiplier, output_filename)
```

Bij het uitvoeren van dit programma kunnen we met 'command line
arguments' de `input_filename`, `multiplier` en `output_filename`
meegeven als argumenten. Dit voorbeeld laat zien hoe we alle waarden
in `input_filename` 'deeltentamen1.txt' kunnen inlezen, vermenigvuldingen
met `multiplier` '100.0', en wegschrijven naar `output_filename` 'voorbeeld.txt':

```console
$ python multiply_file.py deeltentamen1.txt 100.0 voorbeeld.txt
```

Als we hierna de bestand 'voorbeeld.txt' openen zien we het resultaat:

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
eindoplossing komen. Bestanden kunnen daarbij gebruikt worden om
tussenresultaten op te slaan en 'command line arguments' om de namen
van deze bestanden door te geven aan volgende programma's. Deze
opdracht is daar een eenvoudig voorbeeld van.
