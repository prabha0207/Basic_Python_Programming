number=int(input())
list=[]
value=number//2+number
for x in range(1,number+1):
    if x%2==0:
        list.append(x)
for y in range(1,number+1):
    if y%2!=0:
        list.append(y)
for z in range(1,number+1):
    if z%2==0:
        list.append(z)
print(value)
print(*list)
