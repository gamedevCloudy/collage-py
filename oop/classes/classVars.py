class Student:
    sub = "math" #class variable

    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
    def display(self):
        print("Roll= %d, Name: %s, Sub: %s" %(self.roll,self.name, self.sub))

s1 = Student(101,"Ram")

s1.display()
s2 = Student(203, "Mili")
s2.sub = "PPS"
s2.display()
