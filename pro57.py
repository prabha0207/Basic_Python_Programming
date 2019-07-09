number1,number2=map(str,input().split())
countvalue=0
for i in range(0,len(number1)):
    for j in range(0,len(number2)):
        if number1[i]==number2[j]:
            countvalue+=1
if countvalue>=2:
    print("yes")
else:
    print("no")
