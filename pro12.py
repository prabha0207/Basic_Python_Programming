num1,num2=map(int,input().split())
lis=list(map(int,input().split()))
l1=[]
for i in range(0,num2):
     a,b=map(int,input().split())
     l1.append([a,b])
for i in range(num2):
     lower=l1[i][0]
     upper=l1[i][1]
     x=sum(lis[lower-1:upper])
     print(x)
