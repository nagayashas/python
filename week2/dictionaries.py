dict1 = {
    "age":"22",
    "name" : "naga"
}

print(dict1)
dict1["goal"] = "success"
dict1["age"] = 23
val = dict1.pop("age")
print(val)
val1 = dict1.popitem()
print(val1)
print(dict1)