# Input
fruit = input()
week_day = input()
qty = float(input())

# Logic
if week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'banana':
        total = qty * 2.70
    elif fruit == 'apple':
        total = qty * 1.25
    elif fruit == 'orange':
        total = qty * 0.9
    elif fruit == 'grapefruit':
        total = qty * 1.6
    elif fruit == 'kiwi':
        total = qty * 3
    elif fruit == 'pineapple':
        total = qty * 5.6
    elif fruit == 'grapes':
        total = qty * 4.2
elif week_day == 'Monday' \
        or week_day == 'Tursday' \
        or week_day == 'Wednesday' \
        or week_day == 'Thursday' \
        or week_day == 'Friday':
    if fruit == 'banana':
        total = qty * 2.50
    elif fruit == 'apple':
        total = qty * 1.20
    elif fruit == 'orange':
        total = qty * 0.85
    elif fruit == 'grapefruit':
        total = qty * 1.45
    elif fruit == 'kiwi':
        total = qty * 2.7
    elif fruit == 'pineapple':
        total = qty * 5.5
    elif fruit == 'grapes':
        total = qty * 3.85

# Output
if total == 0:
    print('error')
else:
    print(f'{total:.2f}')