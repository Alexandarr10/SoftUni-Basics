import sys
n= int(input())
max_size = -sys.maxsize
sum_numbers = 0

for _ in range(n):
    number = int(input())
    if number > max_size:
        max_size = number

    sum_numbers += number


if max_size == sum_numbers - max_size:
    print(f"Yes\nSum = {max_size}")
else:
    print(f"No\nDiff={abs(max_size-(max_size-sum_numbers))}")