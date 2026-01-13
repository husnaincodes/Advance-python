class Student:
    def __init__(self,fullname):

        self.name  = fullname
        print("Add new student in database...")
s1 = Student("Ali")

print(s1.name)