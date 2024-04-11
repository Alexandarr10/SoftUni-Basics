# Input
city = input()
sales = float(input())

commission = 0
is_invalid_input = False

# Logic
if city == 'Sofia':
    if sales >= 0 and sales <= 500:
        commission = sales * 0.05
    elif sales > 500 and sales <= 1000:
        commission = sales * 0.07
    elif sales > 1000 and sales < - 10000:
        commission = sales * 0.08
    elif commission > 10000:
        commission = sales * 0.12
    else:
        is_invalid_input = True


elif city == 'Varna':
    if sales >= 0 and sales <= 500:
        commission = sales * 0.045
    elif sales > 500 and sales <= 1000:
        commission = sales * 0.075
    elif sales > 1000 and sales < - 10000:
        commission = sales * 0.1
    elif commission > 10000:
        commission = sales * 0.13
    else:
        is_invalid_input = True



elif city == 'Plovdiv':
    if sales >= 0 and sales <= 500:
        commission = sales * 0.055
    elif sales > 500 and sales <= 1000:
        commission = sales * 0.08
    elif sales > 1000 and sales < - 10000:
        commission = sales * 0.12
    elif commission > 10000:
        commission = sales * 0.145
    else:
        is_invalid_input = True

else:
    is_invalid_input = True

# Output
if not is_invalid_input:
    print(f'{commission:.2f}')
else:
    print('error')