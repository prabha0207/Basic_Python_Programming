n=int(input())
x=[int(x) for x in input().split()]
u=[]
for i in range(0,n-1):
    for j in range(i+1,n):
        if(x[i]==x[j]):
            u.append(x[i])
            
w=list(set(sorted(u)))
if len(w)==0:
    print("unique")
else:
    for i in range(0,len(w)):
        print(w[i],end=" ")
