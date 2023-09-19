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
print(x)

x2 = counts.get(name)
# print(x2)

# Simplified counting with get
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

counts_2 = {'quincy': 1, 'mrugesh': 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))