# Orakel

> **Studeertip.** Heb je nu al ChatGPT gebruikt voor een opdracht? Dat is niet zo gek als je niet weet waar je moet beginnen. Maar: deze cursus moet echt zonder ChatGPT! Anders ga je het tentamen waarschijnlijk <u>niet</u> halen. Zorg dus dat je vandaag of morgen nog in gesprek komt met je groepsdocent als je merkt dat je ChatGPT hebt moeten gebruiken.

"All right," said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
"You’re really not going to like it," observed Deep Thought.
"Tell us!"
"All right," said Deep Thought. "The Answer to the Great Question…"
"Yes...!"
"Of Life, the Universe and Everything…" said Deep Thought.
"Yes...!"
"Is.." said Deep Thought, and paused.
"Yes...!"
"Is.."
"Yes...!!!...?"
"Forty-two," said Deep Thought, with infinite majesty and calm.

--- The Hitchhiker’s Guide to the Galaxy, Douglas Adams

## Opdracht

Schrijf, in een bestand genaamd `orakel.py`, een programma dat de gebruiker vraagt om antwoord te geven op de 'De grote vraag van het leven, het universum en alles daarbij'.
Als de gebruiker als antwoord `42`, `tweeenveertig`, of `tweeënveertig` geeft, moet het programma `Ja` printen, maar bij elk ander antwoord `Nee`.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python orakel.py
    Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij? 42
    Ja

    $ python orakel.py
    Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij? tweeenveertig
    Ja

    $ python orakel.py
    Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij? drieëntachtig
    Nee

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def check_answer(answer: str) -> bool:
        """
        Controleer of het antwoord op de vraag één van de opties
        42, tweeenveertig, of tweeënveertig is.
        """

    if __name__ == '__main__':
        <Vraag hier de gebruiker om een antwoord, roep je functie aan, en print het oordeel>

## Tips

* Vergeet niet dat er ook booleaanse operaties zijn zoals `and` en `or`.

## Zelf testen

Werkt je programma goed? Je kunt het insturen om te controleren. Maar je kunt een deel van de tests ook zelf runnen. Dat maakt het verbeteren van fouten misschien iets sneller.

-   Gebruik dit commando om de doctests te controleren die je zelf geschreven hebt:

        python3 -m doctest -v programma.py

    Gebruik hierin het `python` of `python3`-commando afhankelijk van wat op jouw computer de juiste versie is.

-   Je kunt ook de type hints checken. Installeer dan `mypy` via het commando `pip3 install mypy` en controleer zo je programma:

        mypy --strict --ignore-missing-imports programma.py

Mocht het installeren niet lukken, dan kun je altijd hulp vragen. Maar hoe dan ook kun je insturen op deze website, en dan gebeurt het controleren automatisch.
