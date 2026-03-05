# del keyword is used to delete the object proporties and delete object
class Student:
    def __init__(self,name):
        self.name=name

s1 = Student("ITT")
# del s1
print(s1)

# ----------------------------------------------------------------------------------------------

# To declare any methods and variables as private then we add a prefix of __(double underscore) 
# in front of methods and variables

# ----------------------------------------------------------------------------------------------
'''
Inheritance
    1. Single Level         2.Multiple          3.Multilevel

    Python supports multiple inheritance because it uses a well-defined Method Resolution Order (MRO) algorithm to remove ambiguity.
        Python uses the C3 Linearization (MRO) algorithm to decide the order in which parent classes are searched.
        This prevents the Diamond Problem by defining a clear method lookup order.

'''
class A:
    cust1 = "class A"
class B(A): # braket represents that you are inheriting the class 
    cust2 = "class B"
class C(B):
    cust3 = "class C"

c=C()
print(c.cust3)
print(c.cust2)
print(c.cust1)

# ----------------------------------------------------------------------------------------------

'''
    super()
'''

class Cammera:
   def __init__(self,name):
       print(f"clicked by {name}")
class Mobile(Cammera):
    
    def __init__(self, brand,name):
        super().__init__(name)
        print(f"the Mobile name is {brand}")

oppo = Mobile("oppo","itt")


#  ----------------------------------------------------------------------------------------------

