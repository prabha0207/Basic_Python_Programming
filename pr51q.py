number1=int(input())
l=list(map(int,input().split()))
number2=[]
number3=1
for i in range(number1):
	val=l[i:]
	ans=len(val)
	for j in range(ans-1):
		if val[j]>0 and val[j+1]<0:
			number3=number3+1
		elif val[j]<0 and val[j+1]>0:
			number3=number3+1
		else:
			break
	number2.append(str(number3))
	number3=1
print(" ".join(number2))
