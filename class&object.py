class Student:
    def __init__(self,name,marks):

        self.name  = name
        self.marks = marks
        print("Add new student in database...")
s1 = Student("Ali",97)

print(s1.name,s1.marks)