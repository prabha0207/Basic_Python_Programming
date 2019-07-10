#num
num1,num2=list(map(int,input().split()))
l=list(map(int,input().split()))
queries=[]
while(num2):
	queries.append(list(map(int,input().split())))
	num2-=1
for i in queries:
	x=0
	for k in range(i[0]-1,i[1]):
		x=x^l[k]
	print(x)

