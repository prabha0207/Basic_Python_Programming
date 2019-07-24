number1,number2=input().split()
value1=input().split()
value2=input().split()
c=0
for i in value2:
    if i in value1:
        c+=1
if c==len(value2):
    print("YES")
else:
    print("NO")
