import sys

num_count = int(input())
max_num = 0
min_num = 0
for i in range(0, num_count):
    num = int(input())
    if i == 0:
        max_num = num
        min_num = num
    else:
        if num> max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    print(f"Max number : {max_num}")
    print(f"Min number : {min_num}")


