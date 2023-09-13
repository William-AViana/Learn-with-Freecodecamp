string_hours = input('Enter Hours: ')
string_rate = input('Enter Rate: ')

while string_hours == '' or string_rate == '':
    string_hours = input('Please enter hours in numbers example (5.35min): ')
    string_rate = input('Please enter the rate in numbers example (5.35): ')

float_hours = float(string_hours)
float_rate = float(string_rate)

def paymentComputer(float_hours, float_rate):
    if float_hours > 40.0:
        regular_hours = float_rate * float_hours
        overtime_payment = (float_hours - 40.0) * (float_rate * 0.5)
        payment = regular_hours + overtime_payment
    else:
        payment = float_hours * float_rate

    return payment

pay = paymentComputer(float_hours, float_rate)
print('Pay: $%.2f' % pay)
