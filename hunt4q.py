u=int(input())
v=list(map(int,input().split()))
for i in v:
  if(v.count(i)==1):
    print(i)
    break
