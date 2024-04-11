min_num = int(input())

while True:
    user_input = input()
    if user_input == "Stop":
     break
    current_input = int(user_input)
    if current_input < min_num:
        min_num = current_input

print(min_num)