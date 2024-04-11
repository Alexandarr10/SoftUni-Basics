#Брой танцьори – цяло число в интервала [1 … 10]
#2. Брой точки – реално число в интервала [1.00 … 10000.00]
#3. Сезон – текст със следните възможности - "summer" или "winter"
#4. Място – текст със следните възможности - "Bulgaria" или "Abroad"

dancers = int(input())
points = float(input())
season = input()
place = input()
bills = 0

win_price = dancers * points

if place == 'Bulgaria' :
    win_price = dancers * points
else: win_price = win_price * 0.50

if season == 'summer' and place == 'Abroad' :
    bills = win_price + win_price * 1.10
elif season == 'winter' and place == 'Abroad' :
    bills = win_price + win_price * 1.15

if season == 'summer' and place == 'Bulgaria' :
    bills = win_price + win_price * 1.05
if season == 'winter' and place == 'Bulgaria' :
    bills = win_price + win_price * 1.08

total_sum = win_price - bills

charity = total_sum * 0.75

total = total_sum - charity

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {total_sum / dancers}")








