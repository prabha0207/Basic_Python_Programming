val=input()
string=""
f=0
g=[]
if val==val[::-1]:
  g.append(0)
for x in range(len(val)-1):
  for y in range(x+1,len(val)):
    string=inp[x:y+1]
    if string==string[::-1]:
      g.append(len(val)-len(string))
print(min(g))
