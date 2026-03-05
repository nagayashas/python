class Student:
#     #__init__(self) // it is an default constructor

#     # it is a parametraized constructor
#     # mandatorly there must be an argument its recommended to use self because of industry standards
#     # Self is an object reference 

    def __init__(self,fname):     
        print("object is created")
        self.name =fname
        print(self.name+ "yashas")

s1 = Student("naga") #object creation
print(s1.name)

# -------------------------------------------------------------------------
# when ever we create a function inside a class then mandatorly to have a self attribute in the function 
# self is used for objects 

class Student1:
    college = "BCET" 

    def __init__(self , name , marks):
        print("A new Student is created")
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcoming to " + self.college +","+self.name)
    
    def get_marks(self):
        return int(self.marks)

s1 = Student1("naga",100)
s1.welcome()
a= s1.get_marks()
print(a)

# -------------------------------------------------------------------------

class Students:

    def __init__(self,marks1,marks2,marks3):
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def average(self):
        print(round((self.marks1+self.marks2+self.marks3)/3 , 2))

stud1 = Students(100,200,200)
stud1.average()

stud2 = Students(10,20,30)
stud2.average()

# -------------------------------------------------------------------------

'''
if we wont wanna use the self paramether then we go for static methods

static method is associated with the class and to use the static method 
we write @staticmethod (which is a decorator)

'''
class greeting:
    @staticmethod #decorator
    def greet():
        print("thank god")
a1 = greeting()
a1.greet()

# -------------------------------------------------------------------------


