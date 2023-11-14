# Comprehensions

In Python bestaan "comprehensions" waarmee je met een korte expressie een nieuwe collectie aan kunt maken. Bij deze cursus houden we het bij `list`-comprehensions, maar houd wel in je achterhoofd dat er meer bestaan!

Hieronder ga je vijf keer een functie maken met bijbehorende doctests. Via de doctests controleer je of elke functie goed werkt.

## Lijsten maken

Een list comprehension is eigenlijk niet meer dan een `for`-loop op één regel, gecombineerd met een speciale syntax om een lijst te maken. Dit ziet er als volgt uit:

    >>> some_list = [i * 2 for i in range(10)]
    >>> print(some_list)
    [0,2,4,6,8,10,12,14,16,18]

Bovenstaande maakt een gloednieuwe lijst. Je leest de list-comprehension als volgt: zet voor elke `i` in `range(10)` de uitkomst van de expressie `i*2` neer in de lijst. Het is dus een hele compacte syntax om het volgende voor elkaar te krijgen:

    some_list = []
    for i in range(10):
        some_list.append(i * 2)

Je hoeft overigens niet per se de waarde `i` te gebruiken bij het genereren van de uitkomst. In de volgende comprehension gebruiken we `i` puur als teller, zodat we 100 keer een random getal kunnen genereren:

    >>> import random
    >>> random_numbers = [random.random() for i in range(100)]
    >>> print(random_numbers)
    [0.298720086438369, 0.7619029711407771, 0.6239567171981671, ...]

#### Oefening

Schrijf een functie `four_random_letters()` die met hulp van een list-comprehension een lijst met vier random letters genereert.

De random letters moeten gekozen worden uit een opgegeven parameter genaamd `base`, een string met letters zoals `"ABCD"`. Gebruik voor het random kiezen de Python-functie `random.choice()`.

Een voorbeeld van een volledig random uitkomst zou zijn `['A', 'C', 'A', 'A']`.

Voor de doctests zijn er drie mogelijkeheden. De eerste is om één enkele letter op te geven, zodat altijd dezelfde letter wordt gekozen. Dan weet je zeker wat de uitkomst is, ook al is het "random". De tweede optie is om meerdere letters op te geven maar wel dezelfde (bijvoorbeeld `"AAA"`). Zo weet je wederom de uitkomst. De laatste optie is om wel verschillende letters op te geven, maar niet de uitkomst te testen. In plaats daarvan test je de *lengte* van de uitkomst. Ondanks dat je functie random is kun je deze toch testen.

## Condities

Je kunt een conditie verwerken in een list-comprehension. De volgende comprehension baseert zich specifiek op de getallen die deelbaar zijn door 2, en vermenigvuldigt elk van die getallen met 3 om de nieuwe lijst te genereren.

    >>> some_list = [i * 3 for i in range(10) if i % 2 == 0]
    >>> print(some_list)
    >>> [0, 6, 12, 18, 24]

Volledig equivalent is de uitgeschreven `for`-loop:

    some_list = []
    for i in range(10):
        if i % 2 == 0
            some_list.append(i * 3)

#### Oefening

Schrijf een functie `ten_odd_plus_five()` die met hulp van een list-comprehension een lijst getallen genereert.

De getallen moeten de eerste `n` oneven getallen zijn, afkomstig van een parameter `n`. Bij elk getal boven bovendien 5 zijn opgeteld.

Als de parameter `n` is 3, dan zou de uitkomst zijn `[6, 8, 10]`.

## Van lijst naar lijst

Je kunt list-comprehensions ook baseren op bestaande lijsten. Dan gebruien we niet `range(10)` om de loop aan te sturen, maar een lijst. Bijvoorbeeld:

    >>> vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    >>> uppercase_vowels = [vowel.upper() for vowel in vowels]
    >>> print(uppercase_vowels)
    ['A', 'E', 'I', 'O', 'U', 'Y']

Let op dat het hier gebruikelijk is om voor de variabelen zo'n combinatie van enkelvoud (vowel) en meervoud (vowels) te maken. Het enkelvoud wijst dan naar het losse element dat wordt verwerkt.

#### Oefening

Schrijf een functie `password_numeric_analysis()` die met hulp van een list-comprehension van een opgegeven *string* bepaalt of elk teken een cijfer is. De naam van de parameter is `password`. Het resultaat is een `list`.

Als we de functie testen met de string `'mo4br99!'`. Zou het resultaat beginnen met `[False, False, True, ...]`.

## Filteren

Als je een comprehension baseert op een lijst, gecombineerd met een `if`-statement, dan noemen we dat een filter. Bijvoorbeeld:

    >>> numbers = [1,4,9,3,2,5,10,6]
    >>> even_numbers = [number for number in numbers if number % 2 == 0]
    >>> print(even_numbers)
    [4, 2, 10, 6]

List-comprehensions kunnen dus heel handig zijn om met heel weinig code, veel voor elkaar te krijgen. Vaak zijn ze ook nog leesbaarder dan een grote `for`-loop! Als je dus zo'n `for`-loop schrijft, denk dan eens of je dit simpeler kan maken met een list-comprehension.

Let wel, je kan heel ver gaan. Zo kun je multidimensionele list comprehensions schrijven met allerlei condities erin. Op een gegeven moment moet je jezelf dan toch afvragen of het nog wel overzichtelijker is dan een gewone `for`-loop!

    >>> dont_do_this_at_home = [[a * b for a in range(10) for b in range(5) if a > b] for i in range(3)]

#### Oefening

Schrijf een functie `numbers_list_from_password()` die met hulp van een list-comprehension en de methode `isnumeric()` uit een opgegeven *string* de cijfers geeft. De naam van de parameter is `password`. Het resultaat moet een list zijn.

## Strings genereren

Let op dat de basis van de comprehensions soms een string is, maar een comprehension zal altijd een *lijst* geven. Het genereren van strings met een comprehension is niet mogelijk in Python. Toch kun je met een kleine extra stap wel een string maken:

    >>> ['a' for i in range(4)]
    ['a', 'a', 'a', 'a']
    >>> ''.join(['a' for i in range(4)])
    'aaaa'

Dit kan soms van pas komen!

#### Oefening

Schrijf een functie `numbers_from_password()` die met hulp van een list-comprehension en de methode `isnumeric()` uit een opgegeven string de cijfers geeft. De naam van de parameter is `password`. Het resultaat moet een string zijn, geen list!
