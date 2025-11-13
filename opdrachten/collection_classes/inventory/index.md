# Inventaris

Ontwerp een class `Inventory` die een verzameling items bijhoudt, inclusief aantallen. Het domein mag je zelf kiezen (bijvoorbeeld game-inventaris, magazijnvoorraad of winkelvoorraad).

Voorbeeld van het gebruik van de class:

    inv = Inventory()
    inv.add_item("apple", 5)
    inv.add_item("sword")
    inv.remove_item("apple", 2)
    
    print(inv.get_quantity("apple"))   # -> 3
    print(inv.list_items(sorted=True))
    print("sword" in inv)              # -> True

## Interne opslag

- Gebruik **minstens één** Python-collection om de inventaris op te slaan.
- Je mag zelf een datastructuur kiezen, maar licht in een korte comment toe waarom.

## Basisoperaties

- `add_item(name, amount=1)`: voegt items toe of verhoogt de hoeveelheid (standaard-amount is 1, zoals je ziet)
- `remove_item(name, amount=1)`: verwijdert een hoeveelheid; bedenk hoe je negatieve hoeveelheden voorkomt
- `get_quantity(name)`: geeft de huidige hoeveelheid terug
- `__contains__(self, name)`: deze speciale methode maakt gebruik van `in` mogelijk (dus `x in my_inventory`)
- `__len__(self)`: geeft het aantal verschillende items (zodat je `len(my_inventory)` kunt doen)
- `list_items(sorted=False)`: geeft een overzicht van alle items (optioneel alfabetisch gesorteerd)

## Operaties

- Een methode `set_limit()` om de maximale capaciteit in te stellen, zodat de inventory geen items meer toestaat zodra de limiet bereikt is.
- Een methode `find_by_min_quantity()` die de namen van alle items geeft waarvan er een minimum-aantal aanwezig is.
