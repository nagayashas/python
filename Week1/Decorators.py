'''
Decorators are used in thr scenario where we dont want to the real part of the code but i need to make some
changes in the code then we can use the concept of decorators
'''
def div(a,b):
    print (a/b)

def function(func):

    def inner(a,b):
        if(a<b):
            a,b = b,a
        return func(a,b)
    
    return inner

div = function(div)

div(10,20)