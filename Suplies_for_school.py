packets_of_pens = int(input())
packets_of_markers = int(input())
litres_of_board_preparation = int(input())
percent_discount = int(input()) /100

packet_pens = 5.80
packet_markers = 7.20
litre_preparation = 1.20

price_before_discount = packets_of_pens * packet_pens + packets_of_markers * packet_markers + litres_of_board_preparation * litre_preparation
price_with_discount = price_before_discount - price_before_discount * percent_discount

print(price_with_discount)




