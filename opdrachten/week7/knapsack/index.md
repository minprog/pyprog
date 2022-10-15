# Knapsack
Bij een knapsack-probleem krijgen we punten voor elk item dat we
inpakken in de knapsack. De knapsack heeft beperkte resources waardoor
niet alle items kunnen worden ingepakt. Resources bestaan uit een
weight en een volume. Het totaal aan resources van de ingepakte items
mag de resources van de knapsack niet overschrijden.

![](knapsack.png){: style="width:40rem;"}

De data in dit figuur is beschikbaar in file
[knapsack_small.csv](knapsack_small.csv). De data van grotere
knapsack-problemen is beschikbaar in files
[knapsack_medium.csv](knapsack_medium.csv) en
[knapsack_large.csv](knapsack_large.csv).

# Object-Oriented Programming
We gaan met Object-Oriented Programming een knapsack inpakking
proberen te vinden met zo hoog mogelijk aantal punten. Bij
Object-Oriented Programming definieren we verschillemde nieuwe types
uit het probleem-domein en geven die nuttige *instance variables* en
*methods*. Nuttige types voor het knapsack-probleem zijn `Resources`,
`Item` en `Knapsack`.

# Resources type
We definieren eerst het nieuwe type `Resources` als:

    class Resources:
        """ Holds the recources for a Knapsack problem. """
    
        def __init__(self, weight, volume):
            """ Creates a resources object with weight and volume. """
            self.weight=weight
            self.volume=volume

        def __repr__(self):
            """ Enables printing """
            return f"weight:{self.weight} volume:{self.volume}"

        def __iadd__(self, other):
            """ Implements '+=' operator. """
            self.weight += other.weight
            self.volume += other.volume
            return self
    
        def __isub__(self, other):
            """ Implements '-=' operator. """
            self.weight -= other.weight
            self.volume -= other.volume
            return self

        def __lt__(self, other):
            """ Implements '<' operator. """
            return self.weight < other.weight and self.volume < other.volume

Met dit type kunnen we nu resources optellen en vergelijken:

    r1 = Resources(100, 200)
    r2 = Resources(25, 50)
    r1 += r2
    print(r1)
    print(r2 < r1)

# Item type
Met type `Resources` maken we type `Item`. Dit type is alleen maar een
container voor points en resources.

    class Item:
        """ A Knapsack Item with points and resources. """
    
        def __init__(self, points, resources):
            """ Creates an item object with points and resources. """
            pass
        
        def __repr__(self):
            """ Enables printing. """
            return None

        def get_points(self):
            """ Returns the points. """
            return None

        def get_resources(self):
            """ Returns the resources. """
            return None

Deze class werkt nog niet. Implementeer deze class zodat we een Item
kunnen aanmaken, printen, en punten en resources kunnen opvragen:

    item = Item(20, Resources(100,200))
    print(item)
    print(item.get_points())
    print(item.get_resources())

# Knapsack type
Implemeteer ook type `Knapsack` op basis van de docstrings.

    class Knapsack:
        """ Knapsack to which Items can be added. Keeps track of points and available resources."""

        def __init__(self,resources):
            """ Creates an empty knapsack with resources. """
            pass
        
        def __repr__(self):
            """ Enables printing. """
            return None

        def item_fits(self,item):
            """ Returns True if item can still be add to the knapsack given 
            the remaing resources, False otherwise. """
            return None
    
        def add_item(self,item):
            """ Adds item to the knapsack and updates resources. """
            pass
        
        def remove_random_item(self):
            """ Removes and returns a random item from the knapsack. 
            Returns None if the knapsack has no items. """
            return None

        def __len__(self):
            """ Implements 'len(knapsack)' function where knapsack is of type Knapsack 
            to return the number of items in knapsack. """
            return None

        def get_points(self):
            """ Returns the points of all items in the knapsack. """
            return None

Hiermee zouden we items moeten kunnen inpakken in een knapsack:

    knapsack = Knapsack(Resources(100, 200))
    print( knapsack )
    item1 = Item(10, Resources(40, 70))
    knapsack.add_item( item1 )
    item2 = Item(20, Resources(45, 90))
    knapsack.add_item( item2 )
    print( knapsack )
    print( len(knapsack) ) 
    print( knapsack.get_points() )
    print( knapsack.item_fits(item2) )
    item = knapsack.remove_random_item()
    print( knapsack.item_fits(item2) )

# Load a Knapsack problem
Lees de data in de knapsack_small.csv file in. Hiervoor kan deze code
als startpunt gebruikt worden:

    def load_knapsack(filename):
        with open(filename, 'r') as file:
            for line in file:
                splits = line.split(',')
                if len(splits) > 6:
                    element = splits[0].strip()
                    points = int(splits[2])
                    weight = int(splits[4])
                    volume = int(splits[6])
                    print(f"element:{element} points:{points} weight:{weight} volume:{volume}")

# Inpakken
Schrijf functie:

    def solve_knapsack(filename):
        """ Return the highest number of points found when packing the knapsack in file 'filename' """
        return None

en mogelijke helper-functies om het hoogst mogelijke aantal punten te
vinden voor het inpakken van de *knapsack*. Een eenvoudig algoritme om
dit te doen is om:

*   alle items in een *all_items* knapsack te stoppen

*   in random volgorder elk item in *all_items* naar *knapsack* te verplaatsen zolang het item nog past

*   dit heel vaak te doen en het hoogst gevonden aantal punten te onthouden

Test dit eerst met het knapsack_small.csv probleem en pas het daarna
toe op het grotere knapsack_medium.csv probleem.

# Optioneel: Beter inpakken
Bedenk zelf een beter algoritme om het aantal punten van een knapsack
te maximaliseren. Zo kun je misschien het aantal punten van een
ingepakte *knapsack* verder verhogen door er eerst weer items uit te
halen.

Wat is het hoogst aantal punten wat je kunt vinden voor het
knapsack_large.csv probleem? Vergelijk je resultaat met andere.

# Voordelen van Object-Oriented Programming 
We hadden het Knapsack-probleem ook kunnen oplossen zonder gebruik van
Object-Oriented Programming (dus zonder gebruik van classes). Dan
waren er mogelijk minder regels code nodig geweest. Welke voordelen
kunnen we bedenken voor het gebruik van Object-Oriented
Programming voor het Knapsack-probleem?

## Types uit probleem-domein
De types komen overeen met concepten uit het probleem-domein waardoor
het makkelijker is om over de code na te denken.

## Encapsulation
Met *encapsulation* wordt bedoelt dat een class implementatie-details
verborgen houdt voor de gebruiker van een class. Eerder zagen we dit
bij functies, we kunnen een functie gebruiken zonder dat we hoeven te
weten hoe deze functie is geimplementeerd. Maar anders dan functies
kan een class ook *instance variables* verbergen zodat we nu dus ook
waarden (ook wel *state* genoemd) kunnen verbergen.

Een gebruiker van een class hoeft dus bij het aanroepen van *methods*
niks te weten over hoe waarden in een class zijn geimplementeerd. De
implementatie kan daardoor makkelijker veranderen zonder dat dat
effect heeft op andere delen van de code. Bij Object-Oriented
Programming is code daardoor vaak beter in compartimenten
opgedeeld. Enkele voorbeelden daarvan:

*   class Resouces heeft nu alleen *instance variables* weight en
    volume, als daar nog meer variabelen bij zouden komen zouden deze
    relatief gemakkelijk in de Resouces class kunnen worden toegevoegd
    zonder dat veel code buiten de Resouces class aangepast hoeft te
    worden.
    
*   In de Knapsack class heb je waarschijnlijk een *list* gebruikt om
    alle items op te slaan, maar een random element uit een *list*
    verwijderen kan langzaam zijn als de *list* erg lang is. Bij hele
    grote knapsack-problemen zou een *set* of een andere implementatie
    waarschijnlijk sneller zijn. Omdat deze *list* is verborgen in de
    Knapsack class, en dus niet gebruikt wordt in code buiten deze
    class, zou deze vervanging alleen effect hebben op code in de
    Knapsack class.
