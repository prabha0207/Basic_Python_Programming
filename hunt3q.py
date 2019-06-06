nu1=int(input())
nu2=input().split()
l=[]
for i in range(0,nu1):
  if(int(nu2[i])==i):
    l.append(nu2[i])
if(l==[]):
  print("-1")
else:
  l.sort()
  for j in range(0,len(l)):
    print(l[j],end=" ")
