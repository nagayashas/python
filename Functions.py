# ananymous function
# variable = lambda parameters : logical operation
add = lambda x , y : print(x+y)
add(2,3)


'''
RECURSIVE FUNCTION 
    A Function calling itself again and again is called as recursive function 
    base condition is mandatory
'''

def add(n):
    if n==1:
        return 1
    else:
       return n+add(n-1)

print(add(5))


def fact(n):
    if n==1 or n==0 :
        return 1
    else :
        return n*fact(n-1)

print(fact(5))