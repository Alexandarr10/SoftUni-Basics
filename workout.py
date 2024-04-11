import math  # Import the math module

total_days = int(input())
initial_distance = float(input())
percent_increase = [int(input()) for _ in range(total_days)]

total_distance = initial_distance

for percentage in percent_increase:
    initial_distance += initial_distance * percentage / 100
    total_distance += initial_distance

if total_distance >= 1000:
    print(f"You've done a great job running {math.ceil(total_distance - 1000)} more kilometers!")
else:
    needed_distance = 1000 - total_distance
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(needed_distance)} more kilometers")
