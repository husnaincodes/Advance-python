class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        avg = sum(self.marks)
        print(f"HI {self.name} your avg score is: {avg/3}")
s1 = Student("Hunain",[98,88,85])
s1.average()
