
class Vehicle:

    def __init__(self, cost):
        self.cost = cost
        self.total_kilometers = 0

    def __repr__(self):
        return f"cost: {self.cost} total_kilometers: {self.total_kilometers} cost_per_kilometer: {self.cost_per_kilometer()}"
        
    def ride(self, kilometers):
        self.total_kilometers += kilometers
        
    def cost_per_kilometer(self):
        return self.cost / self.total_kilometers

class Bicycle(Vehicle):

    def __init__(self, cost):
        super().__init__(cost)

class Car(Vehicle):

    def __init__(self, cost, fuel_per_kilometer):
        super().__init__(cost)
        self.fuel_per_kilometer = fuel_per_kilometer
    
    def cost_per_kilometer(self):
        fuel_cost_per_kilometer = 2
        return super().cost_per_kilometer() + self.fuel_per_kilometer * fuel_cost_per_kilometer

my_bicycle = Bicycle(200)
my_car1 = Car(10000, 0.075)
my_car2 = Car(15000, 0.05)

my_bicycle.ride(10000)
my_car1.ride(10000)
my_car2.ride(10000)

print("my_bicycle", my_bicycle)
print("my_car1", my_car1)
print("my_car2", my_car2)

my_car1.ride(90000)
my_car2.ride(90000)
print("my_car1", my_car1)
print("my_car2", my_car2)
my_car1.ride(100000)
my_car2.ride(100000)
print("my_car1", my_car1)
print("my_car2", my_car2)
