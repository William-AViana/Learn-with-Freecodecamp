# Dictionaries: Common aplications
d = dict()
d['csev'] = 1
d['cwen'] = 1
# print(d)

d['csev'] = d['csev'] + 1
# print(d)

# Tracebacks
d2 = dict()
# print(d2['csev'])
# print('csev' in d2)

#When we see a new name
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
# print(counts)

# The get method for dictionaries
if name in counts:
    x = counts[name]
else:
    x = 0
# print(x)

x2 = counts.get(name)
# print(x2)

# Simplified counting with get
for name in names:
    counts[name] = counts.get(name, 0) + 1
# print(counts)

counts_2 = {'quincy': 1, 'mrugesh': 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))

# Dictionaries and loops
counts = dict()
print('Entenr a line of text: ')
line = input()

words = line.split()
# print('Words: ', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
# print('Counts', counts)

# Define loops and dictionaries

counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

# Retrieving lists of keys and calues
a = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(a))
print(a.keys())
print(a.values())
print(a.items()) # return a tuple

# Two Iteration Variables!
for b, c in a.items():
    print(b, c)

file = 'test.txt'
handle = open(file)
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or bigcount > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])