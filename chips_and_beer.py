import math

fan_name = input()
budget = float(input())
bottles_beer = int(input())
pacages_chips = int(input())

beer_price = 1.20 * bottles_beer
chips_price = math.ceil((beer_price * 0.45) * pacages_chips)
total_price = beer_price + chips_price

if total_price <= budget :
    print(f"{fan_name} bought a snack and has {budget - total_price:.2f} leva left.")
else:
    print(f"{fan_name} needs {total_price - budget:.2f} more leva!")

