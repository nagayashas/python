def sum(*a):
    sum=0
    for i in a:
        sum=sum+i
    return sum

print(sum(2,3,10,20,10))


print([x*x for x in range(10)])



print([numbers for numbers in range(2,11)
         if all(numbers%i!=0 for i in range(2,numbers))])

print(
    [number if number%2 == 0 else "odd"  for number in range(11)    ]
)

print([x*x if x%2==0 else "NATA" for x in range(10)])

