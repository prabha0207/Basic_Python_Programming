number=int(input())
t1=3
s1=3
list=[]
list.append(3)
for i in range(1,number+1):
    if t1==1:
        t1=2*s1
        s1=t1
        list.append(t1)
    else:
        t1=t1-1
        list.append(t1)
print(list[number-1])
