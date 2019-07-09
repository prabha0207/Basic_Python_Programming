num,val=map(int,input().split())
number=list(map(int,input().split()))
countval=0
for i in number:
  ans=86400-i
  res=val-ans
  countval+=1
  if res<=0:
    break  
print(countval)
