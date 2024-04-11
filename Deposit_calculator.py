deposit = float(input())
deposit_deadline = int(input())
yearly_discount = float(input()) / 100

final_sum = deposit + deposit_deadline * ((deposit * yearly_discount) / 12 )

print(final_sum)