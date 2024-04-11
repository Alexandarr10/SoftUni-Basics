hour = int(input())
day = input()

if hour >= 10 and hour <= 18 and day != "Sunday":
    print("open")
else:
    print("closed")