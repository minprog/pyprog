# RNA-transcriptie

Eiwitsynthese is het proces waarbij eiwitten worden gemaakt op basis van informatie in het DNA, wat onder andere gebeurt in menselijke cellen. Omdat de nieuwe eiwitten niet worden gemaakt op de plek waar het DNA is opgeslagen wordt er een kopie van het relevante stuk DNA gemaakt, en vervoerd naar de locatie waar de eiwitten geproduceerd worden. Dit stukje gekopieerde DNA heet RNA.

DNA bestaat uit 2 lange ketens nucleotiden, die met elkaar verbonden zijn door middel van nucleotiden-paren, die samen de bekende dubbele helix vormen. Deze nucleotiden heten Adenine (A), Guanine (G), Cytosine (C) en Thymine (T). Deze nucleotiden kunnen in slechts 2 paren voorkomen: G-C en A-T. Dit betekent dat als de ene keten uit CTGAC bestaat, de andere keten GACTG moet zijn. De ketens zijn als het ware ‘gespiegeld’.

Alle informatie staat dus in 1 van de ketens, en om deze informatie te kopiëren is maar 1 van de ketens nodig. RNA bestaat dan ook uit een enkele keten nucleotiden, en wordt gevormd door passende nucleotiden tegen een van de ketens van DNA aan te leggen, om zo een gespiegelde kopie te maken. Het enige verschil is dat in RNA geen Thymine (T) maar Uracil (U) heeft. Een gekopieerde A wordt dus een U, en een RNA-keten gebaseerd op CTGAC wordt GACUG. Via dit patroon kan iedere DNA-keten worden omgeschreven naar RNA.

Bovenstaande hoef je niet te begrijpen om de opdracht te maken!

## Opdracht

Schrijf, in een bestand genaamd `rna.py`, een programma dat een DNA-keten van willekeurige lengte omschrijft naar een RNA-keten.

* Zowel de input als de output van het programma zijn strings.

* Je schrijft als volgt om:
    * A -> U
    * G -> C
    * C -> G
    * T -> A

* Wanneer de ingevoerde DNA-keten niet valide is dan print je een foutmelding zoals hieronder.

* Je programma moet zowel kleine als hoofdletters accepteren.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def check_input(dna: str) -> bool:
        """
        Controleert of de input een correcte DNA string is.
        Accepteert zowel hoofd- als kleine letters.
        """

    def transcribe_dna_to_rna(dna: str) -> str:
        """
        Schrijft een string met DNA-elementen om naar een string met
        RNA-elementen (als hoofdletters).
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder. DNA wordt ingetikt op het toetsenbord en de RNA (of foutmelding) wordt door het programma geprint.

    $ python rna.py
    DNA: ATGC
    RNA: UACG

    $ python rna.py
    DNA: atGcAgtAttGCA
    RNA: UACGUCAUAACGU
    
    $ python rna.py
    DNA: hello
    That is not a valid DNA string
