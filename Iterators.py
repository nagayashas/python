# class OneToTen:

#     def __init__(self):
#         self.num=1
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if(self.num <= 10):
#             val = self.num
#             self.num +=1
#         else:
#             raise StopIteration
#         return val

# ans = OneToTen()

# for values in ans:
#     print(values)

class EvenOdd:

    def __init__(self):
        self.position=1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.position

        while self.position <= 20:
            value = self.position
            self.position += 1

            if value % 2 == 0:
                return value
        
        raise StopIteration

ans = EvenOdd()

for answer in ans:
    print(answer)