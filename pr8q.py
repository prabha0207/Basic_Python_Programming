import math,functools
value1,value2=map(int,input().split())
value3=[int(i) for i in input().split()]
for i in range(value2):
    value4,value5=map(int,input().split())
    result=functools.reduce(math.gcd,value3[value4-1:value5])
    print(result)
