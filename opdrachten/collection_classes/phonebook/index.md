# Telefoonboek

Bouw een `Phonebook`-klasse die contacten (namen en telefoonnummers) opslaat in een interne dictionary. Deze dictionary mag niet rechtstreeks van buitenaf worden benaderd; alle interactie verloopt via methodes.

## Constructor

- Maak standaard een leeg telefoonboek.
    - Gebruik een attribuut zoals `_contacts`.
    - Externe code (buiten de class) mag dit niet direct wijzigen.
- Moet optioneel een initiële dictionary met contacten accepteren.
    - De inhoud van deze dict moet *gekopieerd* worden naar het dict-attribuut.

## Basisoperaties

- `add_contact(name, number)`: voegt een contact toe; overschrijft of geeft een fout bij dubbele naam (documenteer keuze).
- `get_number(name)`: geeft het nummer terug of behandelt "niet gevonden" op een nette manier.
- `remove_contact(name)`: verwijdert een contact; netjes omgaan met onbekende naam.
- `update_number(name, new_number)`: wijzigt het nummer van een bestaand contact.

## Operaties

Implementeer deze operaties:

- `list_contacts()`: gesorteerde lijst van alle namen (zonder telefoonnummer).
- `search_by_prefix(prefix)`: alle namen met deze prefix.
- `reverse_lookup(number)`: alle namen bij dit nummer.
- `count_contacts()`: aantal contacten in de lijst.
- `to_dict()`: geeft een volledige kopie van de interne dictionary (dus niet `return _contacts`).
- `merge(other_phonebook)`: voegt een ander Phonebook samen met deze.
