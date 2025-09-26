# List basics

In deze opgave schrijf je één Python-module `list_basics.py` met daarin een aantal functies. Er moeten steeds diverse doctests bij staan.

## Zoek een element

Een functie die checkt of het element `elt` ergens in de lijst `lst` staat.

    def list_contains_element(lst: list[object], elt: object) -> bool:
        ...

Beperkingen: je moet de functie met een loop schrijven, dus bestaande onderdelen van Python zoals `in` en `find` zijn niet toegestaan.

Tip: we gebruiken hier `list[object]` om aan te geven dat de lijst elke soort element kan bevatten. In Python is alle data niet alleen een `int`, `float`, of `str` maar sowieso ook een `object`.

## Tel elementen

Een functie die telt hoe vaak een bepaald element te vinden is in een lijst (bijvoorbeeld een getal).

    def list_count_element(lst: list[object], elt: object) -> bool:
        ...

Beperkingen: je moet de functie met een loop schrijven om langs alle elementen te gaan.

## Tel meerdere elementen

Een functie die telt hoe vaak bepaalde elementen te vinden zijn in een lijst (bijvoorbeeld getallen). Als `lst_elt` bijvoorbeeld de getallen 4 en 29 bevat, telt de functie hoevaak deze getallen voorkomen in de lijst `lst`.

    def list_count_elements(lst: list[object], lst_elt: list[object]) -> bool:
        ...

Beperkingen: je moet de functie met een loop schrijven om langs alle elementen in `lst` te gaan. Als je een element uit `lst` hebt mag je met `lst in lst_elt` kijken of het één van de gezochte elementen is.

## Main?

Je schrijft geen `main` voor deze opdracht. Als je nog extra testcode wil hebben dan moet deze wel in een if-name-is-main staan.
