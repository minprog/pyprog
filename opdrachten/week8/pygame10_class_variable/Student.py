class Student:
    identifier = 1000 # class variable: shared by all objects of class Student

    def __init__(self):
        Student.identifier += 1 # instance variable: each object gets its own variable
        self.student_nr = Student.identifier # assign unique student_nr

    def __repr__(self):
        return f"student_nr:{self.student_nr} identifier:{Student.identifier}"

students = [Student(), Student(), Student()]
print("students:",students)
