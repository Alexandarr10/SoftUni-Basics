pocket_money = float(input())
day_winning = float(input())
expenses = float(input())
gift_price = float(input())

saved_money = pocket_money * 5
wined_money = day_winning * 5
total_saved_money = saved_money + wined_money
total_money = total_saved_money - expenses

if total_money >= gift_price:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {gift_price - total_money:.2f} BGN.")