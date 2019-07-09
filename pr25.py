val=int(input())
val2=list(map(int,input().split()))
list=[]
x=1
for i in range(0,val-1):
    if(val2[i+1]>val2[i]):
        x+=1
    else:
        list.append(x)
        x=1
list.append(x)
print(max(list))
