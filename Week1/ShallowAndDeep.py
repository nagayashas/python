import copy
list1 = [[1,2,3],[4,5,6]]

# in case of shallow copy an outer new object will be created and the values will be changed in the new 
# and there will be a referencing between them if there are any changes both will be changed
shallow = copy.copy(list1)

deep = copy.deepcopy(list1)
list1[0][0]=100
print("shallow ->" + str(shallow))
print("deep ->"+str(deep))


