# List --> list is used to store the elements in one line and they are seperated by ,


fruits = ["apple","banana" , "mango"]
print(fruits)
for each in fruits:
    print(each)
# list slicing 
print("List of " +str(fruits[0:2])) # here the 2nd index will be not considered 
print("List of " +str(fruits[:2])) # if we dont specify starting it will be default 0 
print("List of " +str(fruits[1:])) # if we dont specify ending it will be default length of string -1

"""
==============================================================================================================================================
List methods

"""
names =["naga","bharath","rajesh"]
food = ["naan","masala","food"]

names.append("shet") # it will insert at last 
names.insert(1,"yashwant") # it will insert based on the index

names.extend(food) # it is used to concatenate 2 lists
print(names+food)

names.remove("rajesh")
pop = names.pop()  #pop method will remove the last element and return the popped value
print(pop)
names.reverse() # to reverse the array elements 
names.sort() # to sort the elements in ascending order
names.sort(reverse=True) # to sort the elelments in reverse order 
temp = sorted(names, reverse=True)
print(names.index('bharath'))# return the index of the element
print("naga" in names) # to check whether the elements is present or not 
numbers =[1,6,7,4,3,9,2,19,0]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

for values,index in enumerate(names):
    print(index , values)