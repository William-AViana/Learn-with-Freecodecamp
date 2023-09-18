# Strings and List

string = 'With three words'
stuff = string.split()
# print(stuff)
# print(stuff[1])
for word in stuff:
    print(word)

line = 'A lot                       of spaces'
list_of_the_string = line.split()
# print(list_of_the_string)

line2 = 'first;second;third'
list_line2 = line2.split()
# print(list_line2)
# print(len(list_line2))

list_line2 = line2.split(';')
# print(list_line2)
# print(len(list_line2))

