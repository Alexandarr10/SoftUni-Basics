nylon_price = 1.50
paint = 14.50
thinner_for_paint = 5.00
bags_price = 0.40
nylon_price+= nylon_price + 2
paint+= paint * 0.10


needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
needed_hours = int(input())

total_price = nylon_price * needed_nylon + paint * needed_paint + thinner_for_paint * needed_thinner + bags_price

price_per_hour = total_price * 0.30

total = total_price + price_per_hour * needed_hours

print(total)

