'''
Exception handling is type of handling an error 
some of the errors are:-
    ZeroDivisionError
    ValueError
    TypeError
    IndexError
    KeyError
    FileNotFoundError

'''
# user defined error 
try:
    print(2/0)
except ZeroDivisionError:
    print("an invalid division")

# custom defined exception / error 

class CantVote(Exception):
    def __init__(self):
        print("exception")

class voters:
    age=19
    if age >=18:
        print("You can vote")
    else:
        raise CantVote 
    
# exception useing try catch


class Insufficient_Balance(Exception):
    def __init__(self):
        print("You dont have an proper balance")

class Withdraw:
    try:
        amount =3000
        if(amount>=3000):
            raise Insufficient_Balance()
        else:
            print("You can proceed")
    except Insufficient_Balance:
        pass

# =======================================================================================