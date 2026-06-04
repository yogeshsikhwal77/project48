from functools import reduce
l = [1,2,3,4]

square = lambda x: x*x

#map
sqList=map(square,l)
print(list(sqList))

#filter
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyeven = filter(even,l)
print(list(onlyeven))     #[2, 4]

#reduce
def sum(a,b):
    return a+b


print(reduce(sum,l))  #10