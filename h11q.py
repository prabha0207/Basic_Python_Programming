number1=input().split()
number2=''
for i in number1:
    for y in range(-1,-len(i)-1,-1):
        number2+=i[y]
    if i!=number1[-1]:
        number2+=" "
print(number2)
