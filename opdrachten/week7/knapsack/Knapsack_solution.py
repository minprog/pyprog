import random

class Resources:
    """ Holds the recources for a Knapsack problem. """
    
    def __init__(self, weight: int, volume: int):
        """ Creates a resources object with weight and volume. """
        self.weight=weight
        self.volume=volume
        
    def __repr__(self) -> str:
        """ Prints the instance variables of this class. """
        return f"Resources(weight:{self.weight} volume:{self.volume})"

    def __iadd__(self, other: 'Resources') -> 'Resources':
        """ Implements '+=' operator. """
        self.weight += other.weight
        self.volume += other.volume
        return self
    
    def __isub__(self, other: 'Resources') -> 'Resources':
        """ Implements '-=' operator. """
        self.weight -= other.weight
        self.volume -= other.volume
        return self

    def can_fit(self, other: 'Resources') -> bool:
        """ Tests if the volume and weight of 'other' are both smaller or equal to that of 'self'.
            Useful to test if an item can still fit in the knapsack.
        """
        return other.weight <= self.weight and other.volume <= self.volume

def resources_example() -> None:
    r1 = Resources(100, 200)
    print(r1)                # Resources(weight:100 volume:200)
    r2 = Resources(25, 50)
    r1 += r2
    print(r1)                # Resources(weight:125 volume:250)
    print(r2.can_fit(r1))    # True   (item with resources r1 would     fit in a knapsack with resources r2)
    print(r1.can_fit(r2))    # False  (item with resources r2 would not fit in a knapsack with resources r1)
    r1 -= r2
    print(r1)                # Resources(weight:100 volume:200)
    
class Item:
    """ A Knapsack Item with points and resources. """
    
    def __init__(self, points: int, resources: Resources):
        """ Creates an item object with points and resources. """
        self.points = points
        self.resources = resources
        
    def __repr__(self) -> str:
        """ Prints the instance variables of this class. """
        return f"Item(weight:{self.points} volume:{self.resources})"

    def get_points(self) -> int:
        """ Returns the points. """
        return self.points
    
    def get_resources(self) -> Resources:
        """ Returns the resources. """
        return self.resources

def item_example() -> None:
    item = Item(20, Resources(100, 200))
    print(item)                   # Item(points:20 resources:Resources(weight:100 volume:200))
    print(item.get_points())      # 20
    print(item.get_resources())   # Resources(weight:100 volume:200)

class Knapsack:
    """ Knapsack to which Items can be added. Keeps track of points and available resources."""

    def __init__(self, resources: Resources):
        """ Creates an empty knapsack with resources. """
        self.points = 0
        self.resources = resources
        self.items: list[Item] = []
        
    def __repr__(self) -> str:
        """ Prints the instance variables of this class. """
        return f"Knapsack(points: {self.points}, resources: {self.resources}, items: {self.items})"
    
    def item_fits(self, item: Item) -> bool:
        """ Returns True if item can still be add to the knapsack given 
            the remaining resources, False otherwise. """
        return self.resources.can_fit(item.resources)

    def add_item(self, item: Item) -> None:
        """ Adds item to the knapsack and updates resources (and maybe points). """
        self.points += item.get_points()
        self.resources -= item.get_resources()
        self.items.append(item)
        
    def remove_last_item(self) -> object:
        """ Removes and returns the last item from the knapsack and updates 
            resources (and maybe points). Returns None if the knapsack has no items. """
        if len(self) == 0:
            return None
        item = self.items[-1]
        self.items.pop()
        self.points -= item.get_points()
        self.resources += item.get_resources()
        return item

    def __len__(self) -> int:
        """ Implements 'len(knapsack)' function, where knapsack is of type Knapsack,
            to return the number of items in the knapsack. """
        return len(self.items)

    def get_points(self) -> int:
        """ Returns the total number of points of all items in the knapsack. """
        return self.points

def knapsack_example() -> None:
    knapsack = Knapsack(Resources(100, 200))
    print( knapsack )                          # (afhankelijk van jouw implementatie)
    print( len(knapsack) )                     # 0
    print( knapsack.get_points() )             # 0
    item1 = Item(10, Resources(40, 70))
    knapsack.add_item( item1 )
    print( knapsack )                          # (afhankelijk van jouw implementatie)
    print( len(knapsack) )                     # 1
    print( knapsack.get_points() )             # 10
    item2 = Item(20, Resources(45, 90))
    knapsack.add_item( item2 )
    print( knapsack )                          # (afhankelijk van jouw implementatie)
    print( len(knapsack) )                     # 2
    print( knapsack.get_points() )             # 30
    print( knapsack.item_fits(item2) )         # False
    item = knapsack.remove_last_item()
    print( knapsack.item_fits(item2) )         # True
    print( knapsack )                          # (afhankelijk van jouw implementatie)
    print( len(knapsack) )                     # 1
    print( knapsack.get_points() )             # 10
    item = knapsack.remove_last_item()
    print( knapsack )                          # (afhankelijk van jouw implementatie)
    print( len(knapsack) )                     # 0
    print( knapsack.get_points() )             # 0


def load_knapsack(filename) -> tuple[Knapsack, list[Item]]:
    items=[]
    with open(filename,'r') as file:
        header = file.readline()
        for line in file:
            splits = line.split(',')
            if len(splits)>3:
                element = splits[0].strip()
                points = int(splits[1])
                weight = int(splits[2])
                volume = int(splits[3])
                #print(f"element:{element} points:{points} weight:{weight} volume:{volume}")
                resources = Resources(weight,volume)
                if element=="knapsack":
                    knapsack=Knapsack(resources)
                else:
                    items.append(Item(points,resources))
    return knapsack, items

def solve_knapsack(filename):
    """ Returns the highest number of points found while trying different ways of
        packing the knapsack in file 'filename' """
    knapsack, items = load_knapsack(filename)
    runs = 1000
    best_points = -1
    indices = [index for index in range(len(items))]
    for run in range(runs):
        random.shuffle(indices)
        for index in indices:
            item=items[index]
            if knapsack.item_fits(item):
                knapsack.add_item(item)
        # knapsack is full, test the score
        if knapsack.get_points()>best_points:
            best_points=knapsack.get_points()
            print("best_points:", best_points)
        # empty the knapsack
        while len(knapsack)>0:
            knapsack.remove_last_item()
    return best_points

if __name__ == "__main__":
    resources_example()
    item_example()
    knapsack_example()
    best_points = solve_knapsack("knapsack_large.csv")
    
