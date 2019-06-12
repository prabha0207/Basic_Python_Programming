import math
value1=int(input())
string=math.log10(value1)/math.log10(2)
if math.ceil(string)==math.floor(string):
	print("0")
else:
    c=(value1-1)//2
    string=c*2
    print(value1-string)
