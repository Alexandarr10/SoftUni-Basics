years= int(input())
wash_price = float(input())
toy_price = int(input())
money_from_gifts= 0
money_given=10
toys_count = 0

for age in range(1,years+1):
    if age % 2== 0:
        money_from_gifts+= money_given - 1
        money_given+=10
    else:
        toys_count +=1
money_from_gifts+= toys_count*toy_price

if money_from_gifts >= wash_price:
    print(f"Yes! {money_from_gifts - wash_price:.2f}")
else:
    print(f"No! {wash_price - money_from_gifts:.2f}")
