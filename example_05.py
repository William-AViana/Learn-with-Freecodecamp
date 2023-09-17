# Concatenating lists using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# print(c)
# print(a)
# print(b)

# List can be sliced using:
list = [1, 2, 3, 4, 5, 6]
# print(list[1:3])
# print(list[3:])
# print(list[:])

# List methods
x = [1, 2, 3, 4, 5]
# print(type(x))
# print(dir(x))
# print(x.__add__([6, 7,8, 9,10])) # add elements is not modify
# print(x)

# Biulding a List from Scratch
y = []
y.append('book')
y.append('88')
# print(y)

# Is something in a List?
some = [11,22,33,44,55]
# print(11 in some)
# print(15 in some)
# print(100 not in some)

# List are in Order
friends = ['Graziela', 'Samuel', 'Keia']
friends.sort()
# print(friends)
# print(friends[0])

# Biult-in Function and Lists
nums = [2, 42, 54, 65, 8, 34]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
# avg
print(sum(nums) / len(nums))