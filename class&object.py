class Student:
    def __init__(self,name,marks):

        self.name  = name
        self.marks = marks
        print("Add new student in database...")
s1 = Student("Ali",97)

s2 = Student("Ahmad",88)

print(s2.name,s2.marks)
print(s1.name,s1.marks)