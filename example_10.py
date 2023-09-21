# Tuples are like lists
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(y)
print(max(y))

for iterable in y:
    print(iterable)

# Tuples are "immutable"
x2 = [4, 5, 6]
x2[2] = 9
print(x2)

y2 = 'abc'
# y2[2] = 'd'
# print(y2)

z = (7, 8, 9)
# z[2] = 10
# print(z)

# Things not to do with tuples
z2 = (2, 3, 5)
# z2.sort()
# z2.append()
# z2.reverse()


l = list()
# print(dir(l))

i = tuple()
# print(dir(i))

# Tuples and assignment
(x, y) = (1, 'test')
print(y)

# Tuples and Dictionaries
d = dict()
d['test'] = 2
d['test2'] = 4
for k, v in d.items():
    print(k, v)

tups = d.items()
print(tups)

# Tuples are comparable
print((0,1,2) < (5, 1, 2))
print((0, 1, 2000000) < (0, 3, 4))
print(('Jones', 'Sally') < ('Jones', 'Sam'))
print(('Jones', 'Sally') > ('Adams', 'Sam'))