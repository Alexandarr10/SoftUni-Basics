price_tshirt = float(input())
target_amount = float(input())


price_shorts = 0.75 * price_tshirt
price_socks = 0.2 * price_shorts
price_sneakers = 2 * (price_tshirt + price_shorts)


total_cost = price_tshirt + price_shorts + price_socks + price_sneakers

discount = 0.15 * total_cost
if total_cost - discount >= target_amount:
    print(f"Yes, he will earn the world-cup replica ball!\nHis sum is {total_cost - discount:.2f} lv.")
else:
    needed_money = target_amount - (total_cost - discount)
    print(f"No, he will not earn the world-cup replica ball.\nHe needs {needed_money:.2f} lv. more.")