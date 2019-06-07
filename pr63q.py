value=input()
list=[]
for i in value:
	if i not in list:
		list.append(i)
	else:
		break
print(len(list))
