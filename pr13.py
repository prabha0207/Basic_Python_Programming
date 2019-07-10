num1,num2=input().split()
val1=int(num1)
val2=int(num2)
list=[]
l=input().split()
l=[int(i) for i in l]
for i in range(val2):
  m=[]
  u,v=input().split()
  u=int(u)
  v=int(v)
  for i in range(u-1,v):
    m.append(l[i])
  list.append(min(m))
for i in list:
  print(i)

