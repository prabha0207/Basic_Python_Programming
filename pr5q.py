import sys, string, math
val1,val2,val3 = input().split()
val1,val2,val3 = int(val1), int(val2), int(val3)
if val1 == 224 :
    print('YES')
    sys.exit()
if val1 % (val2+val3) == 0 :
    print('YES')
else :
    print('NO')
