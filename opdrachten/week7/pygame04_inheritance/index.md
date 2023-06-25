# Inheritance

De Player class en de Alien class hebben veel code gemeen, iets wat de
'code duplicatie' noemen. Code duplicatie willen we zo veel mogelijk
voorkomen omdat het de code onnodig langer maakt. Ook kunnen er
makkelijk inconsistencies ontstaan als we bij het veranderen van
duplicate code vergeten om de code op alle plekken aan te passen.

Een manier om code duplicatie te voorkomen is om gebruik te maken van
'inheritance'. Inhertiance kan worden gebruikt bij Object-Oriented
Programming en zorgt dat een class variabelen en methoden van een
andere class overerft.

## Inheritance Voorbeeld

In programma [Vehicles.py](Vehicles.py) berekenen we de reiskosten per
kilometer van verschillende vervoersmiddelen. Eerst wordt de algemene
class `Vehicle` gedefinieerd met 'instance variabelen' `cost` en
`total_kilometers` waar we van gaan overerven.

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

Daarna kunnen we met gebruik van inheritance een `Bicycle` class
definieeren zodat deze class alle variabelen en methoden van de
`Vehicle` class overerft. In de `__init__()` methode van `Bicycle`
roepen we met `super()` de `__init__()` methode van `Vehicle` aan
zodat daar de `cost` wordt opgeslagen.

    class Bicycle(Vehicle):

    def __init__(self, cost):
        super().__init__(cost)

Met deze class kunnen we nu een object (een instance) van `Bicycle`
aanmaken met een `cost` van 200€ en de kosten per kilometer berekenen
na 10000 kilometer fietsen.

    my_bicycle = Bicycle(200)
    my_bicycle.ride(10000)
    print("my_bicycle", my_bicycle) # my_bicycle price: 200 total_kilometers: 10000 cost_per_kilometer: 0.02

Op dezelfde manier kunnen we met inheritance een `Car` class laten
overerven van `Vehicle`, maar een `Car` krijgt ook nog een eigen
'instance variabele' `fuel_per_kilometer` die een effect heeft op het
berekenen van de reiskosten. Omdat deze bereking nu anders is krijgt
`Car` een eigen `cost_per_kilometer()` methode. In deze methode roepen
we wel met `super()` de `cost_per_kilometer()` methode van `Vehicle`
aan om code duplicatie te voorkomen en tellen daar vervolgens de
kosten voor de brandstof bij op.

    class Car(Vehicle):

    def __init__(self, cost, fuel_per_kilometer):
        super().__init__(cost)
        self.fuel_per_kilometer = fuel_per_kilometer
    
    def cost_per_kilometer(self):
        fuel_cost_per_kilometer = 2
        return super().cost_per_kilometer() + self.fuel_per_kilometer * fuel_cost_per_kilometer

Met deze class kunnen we nu de reiskosten vergelijken tussen twee
auto's met verschillende kosten en brandstofverbruik:

    my_car1 = Car(10000, 0.075)
    my_car2 = Car(15000, 0.05)

Als we even ver als de fiets rijden is de goedkopere auto met hoger
brandstofverbruik nog goedkoper per kilometer:
    
    my_car1.ride(10000)
    my_car2.ride(10000)
    print("my_car1", my_car1) # my_car1 price: 10000 total_kilometers: 10000 cost_per_kilometer: 1.15
    print("my_car2", my_car2) # my_car2 price: 15000 total_kilometers: 10000 cost_per_kilometer: 1.6

Als we 90000 kilometer verder rijden zijn de kosten per kilometer gelijk: 

    my_car1.ride(90000)
    my_car2.ride(90000)
    print("my_car1", my_car1) # my_car1 price: 10000 total_kilometers: 100000 cost_per_kilometer: 0.25
    print("my_car2", my_car2) # my_car2 price: 15000 total_kilometers: 100000 cost_per_kilometer: 0.25

Na nog eens 100000 kilometer is de duurdere auto met lager brandstofverbruik goedkoper.

    my_car1.ride(100000)
    my_car2.ride(100000)
    print("my_car1", my_car1) # my_car1 price: 10000 total_kilometers: 200000 cost_per_kilometer: 0.2
    print("my_car2", my_car2) # my_car2 price: 15000 total_kilometers: 200000 cost_per_kilometer: 0.175


![aliens.gif](aliens.gif)
