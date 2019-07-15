lengthL,widthB,heightH=list(map(int,input().split()))
ans=2*(lengthL*widthB + widthB*heightH + heightH*lengthL)
result=lengthL*widthB*heightH
print(ans,result)
