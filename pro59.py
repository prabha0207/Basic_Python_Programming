num,value=map(str,input().split("|"))
tat=input()
if  len(num)>len(value):
    if len(num)==len(value)+len(tat):
        print(num+"|"+value+tat)
elif len(num)<len(value):
     if len(value)==len(num)+len(tat):
        print(num+tat+"|"+value)
elif len(num)==len(value) and len(tat)>1 or (len(value) or len(num)):
    print("impossible")
