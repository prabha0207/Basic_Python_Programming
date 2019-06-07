from itertools import combinations
u,v=map(int,input().split())
w=len(str(u))
x=list(combinations(str(u),w-v))
x=(sorted(x))
y="".join(x[0])
print(y)


