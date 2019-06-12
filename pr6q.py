value1=int(input())
value2=list(map(int,input().split()))
res=0
for i in range(len(value2)-2):
    for j in range(i+1,len(value2)-1):
        for k in range(j+1,len(value2)):
            if value2[i]<value2[j]<value2[k] and i<j<k:
                res=res+1
print(res)
