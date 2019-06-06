n=int(input())
f=list(map(int,input().split()))
f.sort(reverse=True)
for i in range(0,n):
  print(f[i],end="")
