string = input()
str_length = len(string)

result = 0
for i in range (0,str_length):
    current_char =string[i]

    if current_char == "a":
        result += 1
    elif current_char == "e":
        result += 2
    elif current_char == "i":
        result +=3
    elif current_char == "o":
        result +=4
    elif current_char == "u":
        result += 5
print(result)