# Integer lists

In deze opgave schrijf je één Python-module `list_int_basics.py` met daarin een aantal functies. Er moeten steeds diverse doctests bij staan.

## Beslissing: alles even?

Een functie die controleert of alle integers uit de lijst `lst` even zijn.

    def list_check_all_even(lst: list[int]) -> bool:
        ...

Beperkingen: je moet de functie met een loop schrijven om langs alle elementen te gaan.

Tip: het is niet helemaal duidelijk wat het antwoord moet zijn als er helemaal geen getallen in de lijst staan. We kiezen hier voor `True` (dit betekent: triviaal waar).

## Tel even getallen

Een functie telt hoeveel integers uit de lijst `lst` even zijn.

    def list_count_even(lst: list[int]) -> int:
        ...

Beperkingen: je moet de functie met een loop schrijven om langs alle elementen te gaan.

## Pak de even getallen

Een functie die uit een lijst `lst` de even getallen haalt en in een nieuwe lijst zet.

    def list_get_even(lst: list[int]) -> list[int]:
        ...

Beperkingen: je moet de functie met een loop schrijven om langs alle elementen te gaan.

## Main?

Je schrijft geen `main` voor deze opdracht. Als je nog extra testcode wil hebben dan moet deze wel in een if-name-is-main staan.
