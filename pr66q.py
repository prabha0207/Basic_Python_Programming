num1,num2,num3,num4 = map(int, input().split())
counter = 0
ans= num2-num3
if (ans >= 0):
    di = (num1-num3)*2
    for i in range (num4):
        if (i == num4-1):
             di =di/ 2
        if (ans < di):
            ans = num2
            counter += 1
        ans = ans - di
        if (ans < 0):
            counter = -1
            break
        di = 2*num1 - di

    print (counter)
else:
    print (-1)
