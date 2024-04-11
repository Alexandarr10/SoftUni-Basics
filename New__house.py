flower = input()
total_flower = int(input())
budget = int(input())

roses = total_flower * 5
dahlias = total_flower * 3.80
tulips = total_flower * 2.80
narcissus = total_flower * 3
gladiolus = total_flower * 2.50
total_price = 0


if flower == "Roses":
    total_price = total_flower * roses
    if total_flower > 80:
        total_price *= 0.90
elif flower == "Dahlias":
    total_price = total_flower * dahlias
    if total_flower > 90:
        total_price *= 0.85
elif flower == "Tulips":
    total_price = total_flower * tulips
    if total_flower > 80:
        total_price *= 0.85
elif flower == "Narcissus":
    total_price = total_flower * narcissus
    if total_flower < 120:
        total_price *= 1.15
elif flower == "Gladiolus":
    total_price = total_flower * gladiolus
    if total_flower < 80:
        total_price *= 1.20

if total_price >= budget:
    print(f"Not enough money, you need {total_price - budget} leva more.")
else:
    print(f"Hey, you have a great garden with {total_flower} {flower} and {budget - total_price} leva left.")
