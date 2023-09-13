string_hours = input('Enter Hours: ')
string_rate = input('Enter Rate: ')
payment = float(string_hours) * float(string_rate)
print('Payment: $%.2f' % payment)