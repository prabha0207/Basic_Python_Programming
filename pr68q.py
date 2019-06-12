number1,number2=input().split()
if(number1.isdigit() and number2.isdigit()):
              number1,number2=int(number1),int(number2)
              if(number2==1):
                  print("1 2")
              else:
                 print("1 "+str(number1-number2))
