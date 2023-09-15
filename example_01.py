smallest = None
print('Before: ', smallest)
for intervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or intervar < smallest:
        smallest = intervar
        break
    print('Loop: ', intervar, smallest)
print('Smallest: ', smallest)

large_so_far = -1
print('Before', large_so_far)
for the_num in [9, 12, 5, 7, 68, 9]:
    if the_num > large_so_far:
        large_so_far = the_num
print('After', large_so_far)