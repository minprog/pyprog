# Weken

Schrijf, in een bestand genaamd `weken.py`, een functie genaamd `weeks_elapsed`. Je moet hierbij onderstaande code als basis gebruiken.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de doctests aan en voeg dan de implementatie toe. Welke Python-onderdelen uit de eerste hoofdstukken van het boek kun je hiervoor gebruiken?

    def weeks_elapsed(day1: int, day2: int) -> int:
        """
        day1 and day2 are days in the same year. Return the number of full weeks
        that have elapsed between the two days.

        >>> weeks_elapsed(3, 20)
        2
        >>> weeks_elapsed(20, 3)
        2
        >>> weeks_elapsed(8, 5)

        >>> weeks_elapsed(40, 61)

        """

## Testen

Je kunt testen of je functie correct is door je bestand in te leveren op deze pagina. Maar je kunt ook je functie handmatig testen:

- Start `python -i weken.py`. Jouw programma wordt dan ingeladen en je krijgt een prompt `>>>` om commando's in te voeren.

- Tik bijvoorbeeld in `weeks_elapsed(3, 20)` om te kijken of je functie het juiste antwoord geeft.

## Omvormen naar een programma

Tot nu toe heb je functies gemaakt en ook hierboven heb je een Python-bestand geschreven waarin een functie staat. Dat is geen compleet Python-programma.

In de komende weken ga je meestal interactieve Python-programma's maken. Die bestaan uit één of meer functies en daarbij een **hoofdprogramma**. Het hoofdprogramma heeft als taak om invoer en uitvoer te regelen, en één of meer van de functies aan te roepen voor het doen van een berekening, beslissing of transformatie.

Een hoofdprogramma begint altijd met een "if-name-is-main":

    if __name__ == '__main__':

## Opdracht

Hier vind je een groot deel van het hoofdprogramma voor `weken.py`:

    if __name__ == '__main__':
        day1 = int(input("Dagnummer 1: "))
        day2 = int(input("Dagnummer 2: "))
        result = ...
        print(f"Er zijn {result} volle weken verstreken.")

Op de eerste twee regels vragen we de gebruiker van ons programma om twee dagnummers in te tikken. Op de derde regel moet de functie `weeks_elapsed` aangeroepen worden. En op de vierde regel wordt het resultaat geprint dat was opgeslagen in de variabele `result`.

Vul de code aan op de plek van de `...` om de functie aan te roepen.

Als je nu het programma **opstart** kun je het uittesten. Ga naar de Terminal of Command Prompt en start Python met jouw programma:

    % python weken.py
    Dagnummer: 3
    Dagnummer: 20
    Er zijn 2 volle weken verstreken.

We hebben hier zelf op het toetsenbord de getallen `3` en `20` ingevoerd en daarna is het resultaat geprint. Ziet het er bij jou exact zo uit? Dan is je programma klaar om in te sturen en gecontroleerd te worden.
