# RNA

## Eiwitsynthese

Eiwitsynthese is het proces waarbij eiwitten worden gemaakt op basis van de informatie in het DNA. Simpel gezegd is eiwitsynthese het maken van een eiwit in een menselijke cel. De eerste stap van eiwitsynthese is de transcriptie van DNA naar RNA. (Je hoeft voorgaande niet te begrijpen.)

DNA bestaat uit verschillende moleculen, waaronder 4 nucleotiden die de DNA-code vormen: Adenine (A), Guanine (G), Cytosine (C) en Thymine (T). RNA is een zogenaamde complementaire transcriptie van DNA. De complementaire nucleotide van Adenine is Uracil (U), van Guanine is Cytosine, van Cysotine is Guanine en van Thymine is Adenine.

Een complementaire RNA-keten kan dus volgens een vast patroon beredeneerd worden uit de DNA-keten. Zo geeft een DNA-keten `ATGC` altijd de RNA-keten `UACG` als je bovenstaande regels toepast.

## Opdracht

Schrijf, in een bestand genaamd `rna.py`, een programma dat een dna keten van willekeurige lengte omschrijft naar een rna keten.
We willen in deze opdracht dat je oefent met het gebruik van lijsten, dus ook als je zelf bedenkt dat het op een andere manier kan, vragen we je om het op de voorgeshreven manier te implementeren.

* Zowel de input als de output van het programma zijn strings.
* Wanneer de ingevoerde DNA string niet valide is, print dan dat het DNA niet valide is.
* Je programma moet zowel kleine als hoofdletters accepteren.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.


    def check_input(dna: str) -> bool:
        """
        Controleer of de input een correcte DNA string is.    
        """

    def convert_dna(dna_list: list) -> list:
        """
        Converteer een lijst met DNA elementen naar een lijst met RNA elementen.
        """

    def convert_to_list(dna: str) -> list:
        """
        Converteer de DNA string naar een lijst met nucleotiden.
        """

    def convert_to_string(rna: list) -> str:
        """
        Converteer de RNA lijst naar string van nucleotiden.
        """

    if __name__ == '__main__':
        Prompt de gebruiker voor dna, roep je functies aan, en print de gevonden rna string.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python rna.py
    DNA: ATGC
    RNA: UACG

    $ python rna.py
    DNA: atGcAgtAttGCA
    RNA: UACGUCAUAACGU
