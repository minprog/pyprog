# Class Variables

In een class komen drie verschillende categorieen van variabelen voor:

- local variables
- class variables
- instance variables

Programma [Student.py](Student.py) geeft een voorbeeld van elke categorie:

    class Student:
        passing_grade = 5.5     # class variable

    def __init__(self):
        self.grades = []    # instance variable

    def __repr__(self):
        return f"grades: {self.grades} passing_grade: {Student.passing_grade} is_passing: {self.is_passing()}"
        
    def add_grade(self, grade):
        self.grades.append(grade)
        
    def is_passing(self):
        average = sum( self.grades ) / len(self.grades) # local variable
        return average >= type(self).passing_grade

## Local Variable

Een 'local variable' (average) wordt aangemaakt in een methode en wordt
ge-delete onmiddelijk na het uitvoeren van deze methode. Een 'local
variable' is dus alleen binnen één methode beschikbaar. Bij een
'local variable' schrijven we geen voorvoegsel:

    average

## Class Variable

Een 'class variable' (passing_grade) wordt aangemaakt bij het
definieeren van een class en wordt pas ge-delete als het hele
programma wordt afgesloten. Een 'class variable' is in alle methoden
van de class beschikbaar en wordt gedeeld door alle objecten van een
class. Bij een 'class variable' schrijven we in een methode de naam
van de class of `type(self)` of als voorvoegsel:

    Student.passing_grade
    type(self).passing_grade

## Instance Variable

Een 'instance variable' (c) wordt aangemaakt voor ieder object
('instance') van een class en wordt ge-delete als een object "out of
scope" gaat. Een 'instance variable' is in alle methoden van de class
beschikbaar en ieder object heeft haar eigen 'instance variables'. Bij
een 'instance variable' schrijven we in een methode 'self.' als
voorvoegsel:

    self.grades

## Gebruik van de Student class

Het verschil tussen deze catergorieen wordt duidelijker als
we de `Student` class gebruiken in deze voorbeeldcode:

    def main():
        print("Student.passing_grade:", Student.passing_grade) # 'passing_grade' is already available after the class definition
        
        s1 = Student()
        s1.add_grade(5)
        print(s1)                      # 's1.grades' is only available after an object is created 
    
        s2 = Student()
        s2.add_grade(4)
        s2.add_grade(8)
        print(s2)                      # 's2.grades' is only available after an object is created 
    
        Student.passing_grade = 5      # change 'passing_grade'
        print("s1", s1)                # each Student object shares the 'passing_grade'
        print("s2", s2)                # each Student object shares the 'passing_grade'
        # as 's1' and 's2' go "out of scope", they together with their 'grades' get deleted
    
    if __name__ == "__main__":
        main()
        print("Student.passing_grade:", Student.passing_grade) # 'passing_grade' remains available

wat tot deze uitvoer leidt:

    Student.passing_grade: 5.5
    grades: [5] passing_grade: 5.5 is_passing: False
    grades: [4, 8] passing_grade: 5.5 is_passing: True
    s1 grades: [5] passing_grade: 5 is_passing: True
    s2 grades: [4, 8] passing_grade: 5 is_passing: True
    Student.passing_grade: 5

## Kies de Juiste Categorie

Als we een variable aan een class willen toevoegen is het belangrijk
om de juiste categorie te kiezen:

- kies in eerste instantie voor 'local variable'
- behalve als dezelfde variable in meerdere methoden nodig is, kies dan voor 'class variable'
- behalve als ieder object haar eigen variabele nodig heeft, kies dan voor 'instance variable'

## Opdracht: Alien class

De `Alien` class van ons spel erft de `radius`, `line_width` en
`color` variabelen van de `Unit` class als 'instance variables', maar
omdat elk `Alien` object dezelfde waarden voor deze variabelen
gebruikt is het beter deze waarden te delen zodat er minder variabelen
(minder geheugen) nodig zijn. Vervang daarom deze 'instance variables'
in de `Unit` class door 'class variables' in de `Alien` class.

Doordat deze 'instance variables' verdwijnen uit de `Unit` class en
dus niet meer worden ge-erft door de `Player` class moet ook de
`Player` class dezelfde 'class variables' krijgen als de `Alien`
class.

Omdat iedere unit wel haar eigen waarden voor de `position` en
`speed` variabelen nodig heeft, blijven dat wel 'instance variables'
in de Unit class.

## UML Class Diagram

In een UML class diagram worden `class variables` onderstreept:

![class_variables.uxf](class_variables.png)

## Interactie

Zorg dat de interactie tussen units onverandert blijft.

![interaction.gif](../pygame06_interaction/interaction.gif)
