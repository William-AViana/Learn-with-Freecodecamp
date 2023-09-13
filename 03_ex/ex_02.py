string_hours = input('Enter Hours: ')
string_rate = input('Enter Rate: ')

try:
    float_hours = float(string_hours)
    float_rate = float(string_rate)
except:
    print('Error, please enter a numeric input')
    quit()

if float_hours > 40.0:
    regular_hours = float_rate * float_hours
    overtime_payment = (float_hours - 40.0) * (float_rate * 0.5)
    payment = regular_hours + overtime_payment
else:
    payment = float_hours * float_rate

print('Pay: $%.2f' % payment)