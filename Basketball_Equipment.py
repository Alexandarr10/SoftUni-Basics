year_price= int(input())
shoes = year_price * 0.60
jersey = shoes * 0.80
ball = jersey / 4
others = ball / 5

price = (year_price + shoes + jersey + ball + others)

print(price)