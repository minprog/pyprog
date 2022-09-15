# RNA-transcriptie

Eiwitsynthese is het proces waarbij eiwitten worden gemaakt op basis van informatie in het DNA, wat onder andere gebeurt in menselijke cellen. Omdat de nieuwe eiwitten niet worden gemaakt op de plek waar het DNA is opgeslagen wordt er een kopie van het relevante stuk DNA gemaakt, en vervoerd naar de locatie waar de eiwitten geproduceerd worden. Dit stukje gekopieerde DNA heet RNA.

DNA bestaat uit 2 lange ketens nucleotiden, die met elkaar verbonden zijn door middel van nucleotiden-paren, die samen de bekende dubbele helix vormen. Deze nucleotiden heten Adenine (A), Guanine (G), Cytosine (C) en Thymine (T). Deze nucleotiden kunnen in slechts 2 paren voorkomen: G-C en A-T. Dit betekent dat als de ene keten uit CTGAC bestaat, de andere keten GACTG moet zijn. De ketens zijn als het ware ‘gespiegeld’.

Alle informatie staat dus in 1 van de ketens, en om deze informatie te kopiëren is maar 1 van de ketens nodig. RNA bestaat dan ook uit een enkele keten nucleotiden, en wordt gevormd door passende nucleotiden tegen een van de ketens van DNA aan te leggen, om zo een gespiegelde kopie te maken. Het enige verschil is dat in RNA geen Thymine (T) maar Uracil (U) heeft. Een gekopieerde A wordt dus een U, en een RNA-keten gebaseerd op CTGAC wordt GACUG. Via dit patroon kan iedere DNA-keten worden omgeschreven naar RNA.

Bovenstaande hoef je niet te begrijpen om de opdracht te maken!

## Opdracht

Schrijf, in een bestand genaamd `rna.py`, een programma dat een DNA-keten van willekeurige lengte omschrijft naar een RNA-keten.

* Zowel de input als de output van het programma zijn strings.
* Wanneer de ingevoerde DNA-keten niet valide is dan print je een foutmelding zoals hieronder.
* Je programma moet zowel kleine als hoofdletters accepteren.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

We willen in deze opdracht dat je oefent met het gebruik van lijsten, dus ook als je zelf bedenkt dat het op een andere manier kan, vragen we je om het op de voorgeshreven manier te implementeren.

    def check_input(dna: str) -> bool:
        """
        Controleer of de input een correcte DNA string is.    
        """

    def convert_dna(dna_list: list) -> list:
        """
        Converteer een lijst met DNA-elementen naar een lijst met RNA-elementen.
        """

    def convert_to_list(dna: str) -> list:
        """
        Converteer de DNA-string naar een lijst met nucleotiden.
        """

    def convert_to_string(rna: list) -> str:
        """
        Converteer de RNA-lijst naar string van nucleotiden.
        """

    if __name__ == '__main__':
        <Vraag om DNA, roep je functies aan, en print RNA>

## Tips

* Gebruik ''.join(lijst) om een lijst met letters tot een enkele string te combineren.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python rna.py
    DNA: ATGC
    RNA: UACG

    $ python rna.py
    DNA: atGcAgtAttGCA
    RNA: UACGUCAUAACGU
