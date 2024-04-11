import math

n_days = int(input())
daily_kilos = float(input())
i = 0
total_kilos = daily_kilos
while i < n_days:
    percent_per_day = int(input())
    daily_kilos = daily_kilos * (1 + percent_per_day / 100)
    total_kilos += daily_kilos
    i += 1

if total_kilos >= 1000:

    print(f"You've done a great job running {math.ceil(total_kilos - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(1000 - total_kilos)} more kilometers")