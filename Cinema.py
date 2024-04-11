movie = input()
rolls = int(input())
cols = int(input())

total_capacity = rolls * cols

if movie == "Premiere":
    win = total_capacity * 12
elif movie == "Normal":
    win = total_capacity * 7.50
else:
    win = total_capacity * 5

print (f"{win:.2f} leva.")