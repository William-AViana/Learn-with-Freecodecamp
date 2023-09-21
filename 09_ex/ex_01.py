file_name = input('Enter a file name: ')

if len(file_name) < 1: file_name = 'test.txt'

hand = open(file_name)

di = dict()
for line in hand:
    line = line.rstrip()
    # print(line)
    words = line.split()
    for word in words:
        oldcount = di.get(word, 0)
        # print('Old', oldcount)
        newcount = oldcount + 1
        # di[word] = newcount
        di[word] = di.get(word, 0) + 1

largest = 1
for key, value in di.items():
    print(key, value)
    if value > largest:
        largest = value
        theword = key
print('Done', theword, largest)