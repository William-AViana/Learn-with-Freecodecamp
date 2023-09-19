# Working with lists
num_list = list()
while True:
    number = input('Enter a number: ')
    if number == 'done': break
    value = float(number)
    num_list.append(value)

average = sum(num_list) / len(num_list)
print('Avarege: %f' % average)