value=int(input())
number=list(map(int,input().split()))
list=[]
s=1
for i in number:
  if i not in list:
    list.append(i)
for i in range(len(list)-1):
  if (list[i]<list[i+1]):
    s+=1
print(s)
