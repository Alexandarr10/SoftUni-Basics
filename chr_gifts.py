command = input()
age = 0
toyPrice = 5
sweaterPrice = 15
count16 = 0
countAbove = 0
toysMoney = 0
sweaterMoney = 0
while command != "Christmas":
    age = int(command)
    if age <= 16:
     count16 += 1
    toysMoney+= toyPrice
else:
    countAbove = countAbove + countAbove
    sweaterMoney+= sweaterPrice
command = input()
if command == "Christmas":
   pass
print(f"Number of adults: {countAbove}")
print(f"Number of kids: {count16}")
print(f"Money for toys: {toysMoney}")
print(f"Money for sweaters: {sweaterMoney}")
