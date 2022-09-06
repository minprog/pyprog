# Orakel

"Het antwoord op alles."

> "All right," said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.  
> "You’re really not going to like it," observed Deep Thought.  
> "Tell us!"  
> "All right," said Deep Thought. "The Answer to the Great Question…"  
> "Yes...!"  
> "Of Life, the Universe and Everything…" said Deep Thought.  
> "Yes...!"  
> "Is.." said Deep Thought, and paused.  
> "Yes...!"  
> "Is.."  
> "Yes...!!!...?"  
> "Forty-two," said Deep Thought, with infinite majesty and calm.
>
> --- The Hitchhiker’s Guide to the Galaxy, Douglas Adams

## Opdracht

Schrijf, in een bestand genaamd `orakel.py`, een programma dat de gebruiker vraagt om antwoord te geven op de 'De grote vraag van het leven, het universum en alles daarbij'.
Als de gebruiker als antwoord `42`, `tweeenveertig`, of `tweeënveertig` geeft, moet het programma `Ja` printen, maar bij elk ander antwoord `Nee`.

## Code

Vanaf nu gaan we code aanroepen door middel van het gebruik van "if __name__ == '__main__':".
Hier kan je de code schrijven waarin je je verschillende functies aanroept, in plaats van dat je het los onder je zelfgeschreven functies zet.
Verder bestaat je code in deze opdracht uit een zelfgeschreven functie.

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def check_answer(answer: str) -> str:
        """
        Controleer of het antwoord op de vraag 42, tweeenveertig, of tweeen veertig is.
        """

    if __name__ == `__main__`:
        <Prompt hier de gebruiker om een antwoord, roep je functie aan, en print het oordeel>

## Tips

* Dit is de eerste keer dat je met `if`-`else`-statements gaat werken. Vergeet niet dat er ook booleaanse operaties zijn zoals `and` en `or`.

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
