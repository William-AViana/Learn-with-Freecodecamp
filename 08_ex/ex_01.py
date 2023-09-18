file_hand = open('test.txt')

for line in file_hand:
    line2 = line.rstrip()
    words = line2.split()
    # print(words[0])
    if len(words) < 3 or words[0] != 'From:':
        continue
    print(words[2])
        
