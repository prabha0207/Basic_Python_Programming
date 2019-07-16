num=list(input())
arr=[]
for i in num:
    if i not in arr:
        arr.append(i)
print(*arr,sep='')
