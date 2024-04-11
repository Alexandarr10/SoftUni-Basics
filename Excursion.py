budget = float(input())
season = input()

price = 0
destination = ""
place = ""

if budget <= 100:
    destination = "Bulgaria"

    if season == "Summer":
        place = "Camp"
        price = budget * 0.30
    else:
        place = "Hotel"
        price = budget * 0.70

elif budget <= 1000:

       destination = "Balkans"

       if season == "Summer":
        place = "Camp"
        price = budget * 0.40
       else:
           place = "Hotel"
           price = budget * 0.80

else:
    destination = "Europe"
    place = "Hotel"
    price = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")