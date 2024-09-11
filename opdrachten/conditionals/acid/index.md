# Acid test

Gegeven is het volgende Python-programma:

    ph = float(input("Enter the ph level: "))
    if ph < 7.0:
        print("It's acidic!")
    else:
        print("It's alkaline!")

Maak een Python-bestand aan genaamd `acid.py`. Splits bovenstaande programma op zodat het voldoet aan onze standaard-manier van programma's schrijven. Hierin is er een **functie die een berekening doet** en een **hoofdprogramma dat de input en output afhandelt**. Het moet er ongeveer zo uitzien:

    def is_acidic(...) -> bool:
        <functie met docstring, voorbeelden en implementatie>
    
    if __name__ == '__main__':
        <hoofdprogramma doet alleen input en print, en roept is_acidic aan>

## Hint

- De logica is al gegeven. Het enige dat je moet doen is het in de template passen.

- Het is noodzakelijk om zowel in `is_acidic` als in de `__main__` een if-else toe te voegen.

## Testen

Je kunt testen of je functie correct is door je bestand in te leveren op deze pagina. Omdat je een compleet programma hebt geschreven kun je het ook direct testen:

    python acid.py
