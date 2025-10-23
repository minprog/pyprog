# Complexiteitsvragen

Alle onderstaande codefragmenten gebruiken een datastructuur die gegevens bevat. Bepaal de big O-complexiteit in termen van `n` voor deze fragmenten, waarbij `n` het aantal elementen in de datastructuur vertegenwoordigt. Als de big O-complexiteit van een algoritme bijvoorbeeld kwadratisch is, moet je antwoord `O(n^2)` zijn.

## Complexiteit van ingebouwde operaties

De complexiteit van de pseudocode moet je kunnen beredeneren, maar je moet ook weten wat de inherente complexiteit is van de operaties die je in Python kunt uitvoeren, zoals het toevoegen van een element aan een lijst. Op <https://wiki.python.org/moin/TimeComplexity> vind je de tijdcomplexiteit van ingebouwde operaties op `list`, `set` en `dict`.

De tabellen op deze website geven zowel de gemiddelde als de worst-case complexiteit. Voor deze opdracht vragen we je **de gemiddelde complexiteit uit de tabel te gebruiken**. De reden hiervoor is dat `set` en `dict` gemiddeld uitzonderlijk goed presteren, en de worst-case zelden voorkomt. Voor het vergelijken van algoritmes is de worst-case daarom vaak niet relevant. Maar let op: in kritieke situaties waarin prestaties belangrijk zijn, kan het zijn dat "Individuele acties onverwacht lang duren".

Tip: `print` heeft complexiteit O(1).

## Template voor antwoorden

Vul steeds de Big-O in en geef op de regel(s) eronder een precieze afleiding van dit resultaat.

    Vraag 1: O(...)
    uitleg...

    Vraag 2: O(...)
    uitleg...

    Vraag 3: O(...)
    uitleg...

    Vraag 4: O(...)
    uitleg...

    Vraag 5: O(...)
    uitleg...

    Vraag 6: O(...)
    uitleg...

Als voorbeeld geven we de volgende pseudocode:

    for every element in the list L:
        if element not in set S:
            add to set S

Onze uitwerking:

    Voorbeeld: O(n)
    We lopen langs alle n elementen van L
    In de loop doen we soms een add, en die kost O(1) per keer
    Daarom is het geheel ook O(n)

### Vraag 1

Bepaal de complexiteit van de volgende regels pseudocode. Neem voor `n` de lengte van de lijst.

    while list is not sorted:
        for every element in the list:
            if this element > element to the right:
                swap element with element to the right

### Vraag 2

Gegeven is de volgende set:

    my_set = set([42, 21, 7, 3, 2])

Bepaal de complexiteit van de volgende regels pseudocode.

    if 14 in my_set:
        print("gevonden :)")
    else:
        print("niet gevonden :(")

### Vraag 3

Gegeven is de volgende set:

    my_set = set([42, 21, 7, 3, 2])

Bepaal de complexiteit van de volgende regels pseudocode.

    for i in range(len(my_set)):
        if i in my_set:
            print(f"{i}: gevonden :)")
        else:
            print(f"{i}: niet gevonden :(")

### Vraag 4

Gegeven is de volgende opzet:

    n = 10
    set1 = set(range(0, n))
    set2 = set(range(n//2, n + n//2))

Bepaal de complexiteit van de volgende regels pseudocode.

    intersection = set1 & set2
    print(intersection)

### Vraag 5

Gegeven is de volgende opzet:

    n = 10
    list1 = list(range(0, n))
    list2 = list(range(n//2, n + n//2))

Bepaal de complexiteit van de volgende regels pseudocode.

    intersection = []
    for element in list1:
        if element in list2:
            intersection.append(element)

    print(intersection)

### Vraag 6

Gegeven is de volgende opzet:

    n = 10
    my_dict = {}
    for key in range(n):
        my_dict[key] = list(range(2 * key, 2 * key + n))

Bepaal de complexiteit van de volgende regels pseudocode.

    for i in range(n):
        my_list = my_dict[i]
        if i * 5 in my_list:
            print(i * 5)
