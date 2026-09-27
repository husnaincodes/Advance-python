class Student :
    def __init__(self, name= None, age= None, grade= None, students= None):
        self.name = name
        self.age = age
        self.grade = grade
        self.students =  []
        def add_student(self, student):
            """Add a student to the list."""
            self.students.append(student)
    def display_info(self):
        """Display and return the student's information."""
        info = f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
        print(info)
        # return info
s1 = Student("Alice", 20, "A")
s2 = Student("Bob", 22, "B")
s3 = Student("Charlie", 21, "C")

s1.add_student(s2)
s1.add_student(s3)
s1.add_student(s1)  # Adding s1 to its own list of students
s2.add_student(s1)  # Adding s1 to s2's list of students
s1.display_info()
s2.display_info()
s3.display_info()