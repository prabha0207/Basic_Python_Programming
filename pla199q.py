number=str(input())
num=len(number)
r1=0
for i in range(0,num//2):
    if number[i]!=number[num-i-1]:
        r1=r1+1
if r1<=1:
    print("yes")
else:
    print("no")
