class Circle:
    def __init__(self, radius):
        self.r = radius
    def Area(self):
        print("Area = ", (3.14)*(self.r)**2)
    def Circumference(self):
        print("Circumference = ", 2*(3.14)*(self.r))


n = int(input("Enter radius: "))
c = Circle(n)
c.Area()
c.Circumference()


class Temperature:
    def ConverttoF(self, Ctemp):
        print("Temp in Fahrenheit - ",Ctemp*9/5+32)
        def ConverttoC(self, Ftemp):
            print("Temp in Celsius - ",(Ftemp-32)*5/9)

T = Temperature()
n1 = float(input("Enter Temp in Celsius: "))
T.ConverttoF(n1)
n2 = float(input("Enter Temp in Fahrenheit: "))
T.ConverttoC(n2)


class Student:
    def __init__(self, Name, Rollno):
        self.Name = Name
        self.Rollno = Rollno
    def setAge(self, age):
        self.age = age
    def setmarks(self, marks):
        self.marks = marks
    def display(self):
        print("Student Details")
        print("---------------")
        print("Name = ", self.Name)
        print("Roll Number", self.Rollno)
        print("Age = ", self.age)
        print("Marks = ", self.marks)

s = Student("ML Lab", 1007)
s.setAge(20)
s.setmarks(99)
s.display()


class Time:
    def __init__(self, hour, min):
        self.hour = hour
        self.min = min
    def addTime(t1, t2):
        t3 = Time(0, 0)
        t3.hour = t1.hour + t2.hour
        t3.min = t1.min + t2.min
        while t3.min >= 60:
            t3.hour += 1
            t3.min -= 60
            return t3
    def displayTime(self):
        print("Time is %d hours and %d minutes" %(self.hour, self.min))
    def displayMin(self):
        print((self.hour * 60) + self.min, "minutes")
        
a = Time(1, 23)
b = Time(1, 52)
c = Time.addTime(a,b)
c.displayTime()
c.displayMin