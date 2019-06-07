val1=int(input())
val2=str(val1)
val3=0
for i in range(0,len(val2)):
    if int(val2[i:i+2])<26 and len(str(int(val2[i:i+2])))==2:
        val3=val3+1
if val3==2:
    print(val3+val3//2)
else:
    print(val3+val3//2+1)
