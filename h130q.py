number=int(input())
list=[]
cou=0
for i in range(3,number):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if i%10==3:
            cou=cou+i
print(cou)
