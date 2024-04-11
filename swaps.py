first_number = int(input())
second_number = int(input())
third_number = int(input())
four_number = int(input())

current_combination = 0

for k in range(first_number, 9):
    for l in range(9, second_number - 1, -1):
        for m in range(third_number, 9):
            for n in range(9, four_number - 1, -1):
                if k == m and l == n and k % 2 == 0 and l % 2 != 0:
                    print("Cannot change the same player.")
                elif k % 2 == 0 and l % 2 != 0 and m % 2 == 0 and n % 2 != 0:
                    print(f"{k}{l} - {m}{n}")
                    current_combination += 1
                if current_combination == 6:
                    break
    if current_combination == 6:
        break
