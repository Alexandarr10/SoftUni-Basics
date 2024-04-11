people = int(input())
season = input()
price = 0
if season == "spring" and people <= 5:
    price = 50
elif season == 'spring' and people > 5:
    price = 48

if season == 'summer' and people <= 5:
    price = 48.50 * 0.85
elif season == 'summer' and people >5 :
    price = 45 * 0.85

if season == 'autumn' and people <= 5:
    price = 60
elif season == 'autumn' and people >5 :
    price = 49.50

if season == 'winter' and people <= 5:
    price = 86 * 1.08

elif season == 'winter' and people >5 :
    price = 85 * 1.08

total_price = people * price
print(f"{total_price:.2f} leva.")



