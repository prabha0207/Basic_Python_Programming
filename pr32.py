num1,num2=map(int,input().split())
if num1<=num2:
  u=num1
else:
  u=num2
m=[]
for i in range(0,u):
  m.append(sorted(list(map(int,input().split()))))
m=sorted(m)
for i in range(0,len(m[0])):
  for j in range(0,len(m)-1):
    if m[j][i]>m[j+1][i]:
      m[j][i],m[j+1][i]=m[j+1][i],m[j][i]
for i in m:
  print(*i)
