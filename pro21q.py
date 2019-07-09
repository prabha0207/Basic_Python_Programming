value1=int(input())
value2=list(map(int,input().split()))
ans=int(value1/2)
result1=value2[:ans]
result2=value2[ans::]
if ((sum(result1)//len(result1))==(sum(result2)//len(result2))):
    print("yes")
else:
    print("no")
