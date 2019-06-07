u,v=input().split()
s=abs(len(u)-len(v))
for i in range(len(u)):
    if len(v)==1 and v[i] in u:
        break
    if u[i]!=v[i]:
        s=s+1
print(s)
