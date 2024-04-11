fat_percent = int(input())
protein_percents = int(input())
carps_percents = int(input())
total_calories = int(input())
water_percents = int(input())
percent = 100
gram_fat = ((fat_percent / 100) * total_calories) / 9
gram_carps = ((carps_percents / 100) * total_calories) / 4
protein_gram = ((protein_percents / 100) * total_calories) / 4

total_food_kilos = (gram_fat + gram_carps + protein_gram)
calories_per_kilo = total_calories / total_food_kilos
water = percent - water_percents
gram_food = (water * calories_per_kilo) / 100


print(f"{gram_food:.4f}")



