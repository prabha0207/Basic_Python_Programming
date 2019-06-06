u=int(input())
v=input().split()
w=[]
x=''
for i in range(len(v)):
    if i==int(v[i]):
        w.append(i)
w.sort(key=int)
if len(w)>0:
    for i in range(len(w)-1):
        x+=str(w[i])+" "
    print(x+str(w[-1]))
else:
    print(-1)
