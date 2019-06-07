value1,value2=map(int,input().split())
value3,value4=map(int,input().split())
value5,value6=map(int,input().split())
value7,value8=map(int,input().split())
temp1=value4-value2
temp2=value6-value8
temp3=value5-value3
temp4=value7-value1
if temp1==temp2== temp3==temp4:
	print("yes")
else:
	print("no")
