number1,number2=input().split()
value1=input().split()
for i in range(int(number2)):
    value2=max(value1,key=int)
    value1.pop(value1.index(max(value1,key=int)))
print(value2)
