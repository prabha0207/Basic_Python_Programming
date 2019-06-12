number1,number2 = map(int,input().split())
number3 = list(map(int,input().split()))
amount = int(input())
total = (sum(number3)-number3[number2])//2
if amount == total:
  print("Bon Appetit")
else:
  print(amount-total)
