paper = int(input())
plat = int(input())
glue = float(input())
diss = int(input())

paper_price = 5.80
plat_price = 7.20
glue_price = 1.20

paper_total_price = paper * paper_price
plat_total_price = plat * plat_price
glue_total_price = glue * glue_price
total_price = paper_total_price + plat_total_price + glue_total_price
total_price *= (1 - diss / 100)

print(f"{total_price:.3f}")

