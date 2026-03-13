def decorator(func):
    def wrapper(*args):
        print("i am a decorator function ")
        return  func(*args)
    return wrapper

@decorator
def add(*args):
    print(args)
    sum = 0
    for i in args:
        sum +=i
    return sum


print(add(2,3))