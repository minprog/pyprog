# RNA-transcription

> Please note: the checks for this assignment will be available on Wednesday at the latest. Do not submit your solution before that time.

Protein synthesis is the process of creating proteins based on information from the DNA, which is a process that, for example, happens in human cells. Because new proteins are not created in the same place that the DNA is stored, a copy of the relevant piece of DNA is made, and transported to where it is needed to synthesize the proteins. This copied piece of DNA is called RNA.

DNA consists of 2 large chains of necleotides, that are connected to each other through nucleotide-pairs, that together form the well known helix shape. These nucleotides are called Adenine (A), Guanine (G), Cystosine (C) and Thymine (T). These nucleotides can only exist in 2 pairs: G-C and A-T. This means that when one chain consists of CTGAC, the other chain has to be GACTG. The chains are in a sense 'mirrored'.

That way, all information is contained in either of the cains, and to copy this information only one of those chains is required. RNA is therefore only made out of one chain of nucleotides. It is made by sequencing the correct nucleotides along one of the DNA chains, to make a mirrored copy of it. The only difference is that RNA does not contain Thymine (T), but Uracil (U). A copied Adenine (A) becomes a Uracil (U), which means a CTGAC on the DNA turns into GACUG on the RNA. Through this pattern, every DNA-chain can be written into an RNA chain.

Don't worry if you don't fully understand the text above. We will only be applying the concepts!

## Assignment

Implement, in a file called `rna.py`, a program that transcribes a DNA-chain of random length into an RNA-chain of equal length.

* Both input and output of the program consists of strings.
* When the input DNA-chain is not valid, print an error message as can be seen below.
* Your program should be able to handle both upper case and lower case chains.

## Code

Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

For this assignment we want you to practice the use of lists, that means that even if you know of another way to implement the functions, we ask you to follow the prescribed strategy of implementation.

    def check_input(dna: str) -> bool:
        """
        Checks whether the input is a correct DNA string.
        """

    def transcribe_dna_to_rna(dna_list: list[str]) -> list[str]:
        """
        Writes a list of DNA-elements into a list of RNA-elements.
        """

    def convert_to_list(dna: str) -> list[str]:
        """
        Converts the DNA-string into a list of nucleotides.
        """

    def convert_to_string(rna: list[str]) -> str:
        """
        Converts an RNA-list to a string of nucleotides.
        """

    if __name__ == '__main__':
        <Main program>

## Tips

* Use `''.join(list)` to turn a list of letters to a single string.

## Examples

Your program should work like the examples below.

    $ python rna.py
    DNA: ATGC
    RNA: UACG

    $ python rna.py
    DNA: atGcAgtAttGCA
    RNA: UACGUCAUAACGU
