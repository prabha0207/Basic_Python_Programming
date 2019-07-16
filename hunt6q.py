u=int(input())
li=list(map(int,input().split()[:u]))
v=False
for i in li:
    if(li.count(i)>1):
        v=True
        break
if v:
    print(i)
else:
    print("unique")
