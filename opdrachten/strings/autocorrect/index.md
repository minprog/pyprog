# Autocorrect

Maak een Python-module genaamd `autocorrect.py`. Schrijf de volgende functie met doctests. Je maakt voor deze opgave geen `main`, maar wel doctests!

    >>> autocorrect('---')
    '-'
    >>> autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')
    'Dit hier, dit kan niet de bedoeling zijn.'

Schrijf een functie `autocorrect` die dubbele leestekens en spaties verwijdert uit een string. Alleen gewone letters en cijfers (te herkennen met `c.isalnum()`) worden met rust gelaten.

Gebruik een normale transformatie-loop (`for char in s:`) maar check altijd, vóórdat je een teken toevoegt aan het resultaat, of dat teken niet toevallig al aan het eind van het resultaat staat.
