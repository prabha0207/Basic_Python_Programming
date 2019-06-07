u,v=input().split()
w=0
if len(u)>len(v):
  u,v=v,u
i=0
while i<len(u):
  s+=(ord(v[i])-ord(u[i]))
  i+=1
for i in range(i,len(v)):
  w+=ord(v[i])-ord('u')+1
print(w)
