u=int(input())
v=input().split()
v.sort(reverse=True,key=int)
w=''
for i in v:
    w+=i
print(w)
