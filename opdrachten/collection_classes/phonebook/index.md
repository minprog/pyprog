# Telefoonboek

Bouw een `Phonebook`-klasse die contacten (namen en telefoonnummers) opslaat in een interne dictionary. Deze dictionary mag niet rechtstreeks van buitenaf worden benaderd; alle interactie verloopt via methodes.

## Initializer

- Maak standaard een leeg telefoonboek als er een nieuwe instantie van de class wordt aangemaakt.
    - Gebruik hiervoor een attribuut `_contacts`.

- De class moet optioneel een initiële dictionary met contacten accepteren.
    - Gebruik een optionele parameter voor de initializer:

            def __init__(contact_list=None):
                ...
                if contact_list:
                    ...

    - De inhoud van deze dict moet *gekopieerd* worden naar het `_contacts`-attribuut dat je aanmaakt.

- Denk zelf na wat voor type naam en telefoonnummer moeten/kunnen zijn.

## Basisoperaties

- `add_contact(name, number)`: voegt een contact toe; als de naam al in de lijst staat geef je een foutmelding met `raise KeyError(f"duplicate key")`
- `get_number(name)`: geeft het nummer of `None` als het niet gevonden is
- `remove_contact(name)`: verwijdert een contact; doet niks als de naam er niet in zit
- `update_number(name, new_number)`: wijzigt het nummer van een bestaand contact

## Operaties

Implementeer deze operaties:

- `list_contacts()`: geeft een gesorteerde lijst van alle namen (zonder telefoonnummer)
- `search_by_prefix(prefix)`: geeft alle namen met deze prefix
- `reverse_lookup(number)`: geeft alle namen bij dit nummer
- `count_contacts()`: geeft het aantal contacten in de lijst
- `to_dict()`: geeft een volledige kopie van de interne dictionary (dus niet `return _contacts`)
- `merge(other_phonebook)`: voegt een ander `Phonebook`-object samen met deze, maar let op: je mag niet de `_contact` van het andere object gebruiken!
