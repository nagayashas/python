class Student:
    #__init__(self) // it is an default constructor

    # it is a parametraized constructor
    # mandatorly there must be an argument its recommended to use self because of industry standards
    # Self is an object reference 

    def __init__(self,fname):     
        print("object is created")
        self.name =fname
        print(self.name+ "yashas")

s1 = Student("naga") #object creation
print(s1.name)
