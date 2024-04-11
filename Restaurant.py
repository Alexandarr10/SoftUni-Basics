#Пилешко меню – 10.35
#Меню с риба – 12.40
#Вегетарианско меню – 8.15

chicken = 10.35
fish = 12.40
vegetarian = 8.15

#Брой пилешки менюта – цяло число в интервала [0 … 99]
#Брой менюта с риба – цяло число в интервала [0 … 99]
#Брой вегетариански менюта – цяло число в интервала [0 … 99]

chicken_num = int(input())
fish_num = int(input())
vegetarian_num = int(input())

price= (chicken * chicken_num) + (fish * fish_num) + (vegetarian * vegetarian_num)

decert= price * 0.20
dellivery = 2.50

total_price = price + decert + dellivery

print(total_price)
