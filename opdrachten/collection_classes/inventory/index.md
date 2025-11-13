# Opdracht: Bouw een `Inventory`-class

## 1. Doel van de opdracht
- Werken met Python-collections om gegevens te beheren.
- Toepassen van objectgeoriënteerd programmeren.
- Een kleine inventaris bouwen en manipuleren met eigen methodes.

## 2. Beschrijving
Ontwerp een class `Inventory` die een verzameling items bijhoudt, inclusief aantallen. Het domein mag je zelf kiezen (bijvoorbeeld game-inventaris, magazijnvoorraad of winkelvoorraad).

## 3. Minimale vereisten

### 3.1 Interne opslag
- Gebruik **minstens één** Python-collection om de inventaris op te slaan.
- Je mag zelf een datastructuur kiezen, maar licht in een korte comment toe waarom.

### 3.2 Vereiste methodes
- `add_item(name, amount=1)`: voegt items toe of verhoogt de hoeveelheid.
- `remove_item(name, amount=1)`: verwijdert een hoeveelheid; kies zelf hoe je negatieve hoeveelheden voorkomt.
- `get_quantity(name)`: geeft de huidige hoeveelheid terug.
- `__contains__(self, name)`: maakt gebruik van `in` mogelijk.
- `__len__(self)`: aantal verschillende items.
- `list_items(sorted=False)`: geeft overzicht van alle items (optioneel alfabetisch gesorteerd).

## 4. Uitbreidingsopties (kies er minstens één)
- Inventories samenvoegen (`__add__` of `merge`).
- Maximale capaciteit instellen.
- Werken met categorieën voor items.
- Zoekfuncties (substring, categorie, hoeveelheid > X).
- Exporteren/importeren via JSON.

## 5. Voorbeeldgebruik
```python
inv = Inventory()
inv.add_item("apple", 5)
inv.add_item("sword")
inv.remove_item("apple", 2)

print(inv.get_quantity("apple"))   # 3
print(inv.list_items(sorted=True))
print("sword" in inv)              # True
```

## 6. Wat lever je in?
1. Een Python-bestand `inventory.py` met de implementatie.
2. Een testbestand of notebook met minstens vijf demonstraties.
3. Een korte reflectie (max 200 woorden) over je ontwerpkeuzes en datastructuren.
