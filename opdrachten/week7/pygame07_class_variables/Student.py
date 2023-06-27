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

def main():
    print("passing_grade:", Student.passing_grade) # 'passing_grade' is available after the class definition
    
    s1 = Student()
    s1.add_grade(5)
    print(s1)                      # 's1.grades' is only available after an object is created 

    s2 = Student()
    s2.add_grade(4)
    s2.add_grade(8)
    print(s2)                      # 's2.grades' is only available after an object is created 

    Student.passing_grade = 5      # changing 'passing_grade'
    print("s1", s1)                # each Student object shares the 'passing_grade'
    print("s2", s2)                # each Student object shares the 'passing_grade'
    # as 's1' and 's2' go "out of scope", they together with their 'grades' get deleted

if __name__ == "__main__":
    main()
    print("passing_grade:", Student.passing_grade) # 'Student.passing_grade' remains available
