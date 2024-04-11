name = input()
current_class = 1
grade = 0
fails = 0
average= 0
while True:
    current_grade = float(input())
    if current_grade < 4:
        fails += 1
        continue
    if fails >= 2:
        break
    current_class += 1
    grade += current_grade
    if current_class > 12:
        break
if fails >= 2:
    print(f"{name}has been excluded at {current_class - 1} grade")
else:
  average = grade / 12
  print(f"{name} graduated. Average grade: {average:.2f} ")

