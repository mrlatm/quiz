import math
my_list = [49, 0, 1, -1, -49, -2]


def fifty_sort(item):
    return abs(50 - item)


print("-"*50)
print(f"\nmy list befor sort: {my_list}\n")
my_list.sort(key=fifty_sort)
print(f"\nmy list after sort: {my_list}\n")
print("-"*50)
