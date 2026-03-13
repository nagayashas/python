def sum( n):
    count =0
    for i in range(1,n+1):
        count+=i
        print(str(i)+"    ->" , end="")
        yield count

value =sum(10)
for i in value:
    print(i)