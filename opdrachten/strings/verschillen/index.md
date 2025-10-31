# String-verschillen

Maak een Python-module genaamd `verschillen.py`. Schrijf de volgende functies met doctests. Je maakt voor deze opgave geen `main`, maar wel doctests!

## Verschillend?

Schrijf een functie `is_different` die twee strings `s1` en `s2` aanneemt en bepaalt of deze strings verschillen.

Hiervoor ga je loopen met indexes, van 0 tot het einde van de strings. Je bekijkt steeds *hetzelfde* teken van beide strings (bijv. op index 1). Als de strings op één plek verschillen, dan weet je dat de strings verschillen, en kan de functie direct `return True` doen. Als ze niet verschillen op die plek, dan weet je nog niks. Je gaat dan door naar de volgende.

Hints:

- Schrijf het eerst zodat het werkt als je strings van gelijke lengte ("abc" en "def") geeft.
- Denk daarna hoe je het gaat afhandelen als de strings van verschillende lengte zijn en verwerk dit in de code.

## Hoe verschillend?

Schrijf een functie `count_difference` die twee strings `s1` en `s2` aanneemt en bepaalt hoeveel verschillen de strings hebben.

We gebruiken een vereenvoudigd algoritme. Als de strings verschillen van lengte dan berekenen we dat verschil en dat is de basis. Dan vergelijken we zoveel mogelijk de tekens per positie, zoals bij de vorige functie. Voor elke positie waar de tekens verschillen tel je één op bij de basis.
