''' 
read()-> reads all the lines
readlines() -> reads all the lines but between lines there will be \n 
readline()-> reads only one line
tell() -> points the current position in the text file
seek() -> repositions the current position to the first 
'''

# with open('text.txt' ,'r') as f:
#     for contents in f:
#         print(contents,end="") 

#     contents = f.read(100)
#     print(contents)

# with open("text2.txt" , 'w') as towrite:
#     towrite.write("byeeeeeeeee")


# Copied the one file ocontents to another file
# with open("text.txt",'r') as rf:
#     with open("copy.txt",'w') as wf:
#         for lines in rf:
#             wf.write(lines)

"""======================================================================="""

# JSON Handling 

import json
data = [
    {"name" :"Nagayashas","age" :"22"},
    {"name":"shetty","age":"100"}
]
with open("JsonFile.json","w") as write:
    json.dump(data ,write)

