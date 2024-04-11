#1. Дължина в см – цяло число в интервала [10 … 500]
#Широчина в см – цяло число в интервала [10 … 300]
#Височина в см – цяло число в интервала [10… 200]
#Процент – реално число в интервала [0.000 … 100.000]

length = int(input())
width = int(input())
height = int(input())
perc = float(input()) / 100

volume = length * width * height / 1000
volume -= volume * perc

print(volume)

