"""
tuples are same as list but cant change they are immutable

sets does not care about insertion and they dont follow order of insertion

"""

names ={"naga","bharath","rajesh"}
food = {"naan","masala","food","naga"}

print("Intersection :" + str(names.intersection(food)))
print("Difference :" + str(names.difference(food)))
print("Union :" + str(names.union(food)))


# to create an emty set 
empty_set = set()