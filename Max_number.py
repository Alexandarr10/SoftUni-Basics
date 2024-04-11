bigger_num = int(input())

while True :
    user_input = input()
    if user_input == 'Stop':
        break
    num = int(user_input)
    if num > bigger_num:
        bigger_num = num

print(bigger_num)
