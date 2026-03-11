intern = {"name": "naga" , "age" :"22" , "company": "ITT"}
print(intern["name"]) # Gives an error in the abscence of key
print(intern.get("name")) # Gives an output as none in the abscence of key
print(intern.get("experience"),"NOT AVAILABLE")


"""
TO ADD A NEW ELEMENT OR UPDATE AN ELEMENT WE USE update()
"""

intern.update({"name":"nagayashas","phno" : "1234567890"})
del intern["age"]


popped = intern.pop("age")
print(popped)

print("length :" + str(len(intern)))

print(intern.keys())
print(intern.values())
print(intern.items()) # Prints the data in key and value format

# to loop on dictionarties we should use items()
print("===LOOPING ON KEY AND VALUE===")
for key,values in intern.items():
    print(values)
print(intern)