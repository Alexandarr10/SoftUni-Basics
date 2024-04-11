user_name = input()
user_psw = input()

input_psw = input()

while input_psw != user_psw:
    input_psw = input()

print (f"Welcome {user_name}!")