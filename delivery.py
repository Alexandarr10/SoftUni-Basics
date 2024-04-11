weight_in_kg = float(input())
delivery_type = input()
distance_in_km = int(input())

base_price_per_km = 0.03

if 1 <= weight_in_kg <= 10:
    base_price_per_km = 0.05
elif 10 <= weight_in_kg <= 40:
    base_price_per_km = 0.10
elif 40 <= weight_in_kg <= 90:
    base_price_per_km = 0.15
elif 90 <= weight_in_kg <= 150:
    base_price_per_km = 0.20

express_delivery_price = 0.0

if delivery_type == 'express':
    if weight_in_kg < 1.0:
        express_delivery_price = 0.80
    elif 1 <= weight_in_kg <= 10:
        express_delivery_price = 0.40
    elif 10 <= weight_in_kg <= 40:
        express_delivery_price = 0.05
    elif 40 <= weight_in_kg <= 90:
        express_delivery_price = 0.02
    elif 90 <= weight_in_kg <= 150:
        express_delivery_price = 0.01
    express_delivery_price *= base_price_per_km

total_price = (base_price_per_km + weight_in_kg * express_delivery_price) * distance_in_km

print(f"The delivery of your shipment with weight of {weight_in_kg:.3f} kg. would cost {total_price:.2f} lv.")