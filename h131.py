num1=int(input())
num2=list(map(int,input().split()))
temp=[]
while(len(num2)!=0):
  if len(num2)>1:
    temp.append(max(num2))
    temp.append(min(num2))
    num2.remove(max(num2))
    num2.remove(min(num2))
  else:
    temp.append(max(num2))
    num2.remove(max(num2))
print(*temp,end="")  


