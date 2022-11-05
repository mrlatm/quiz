my_list = input("Enter your numbers:").split()
for index, item in enumerate(my_list):
    my_list[index] = int(item)
my_list.sort()
a = my_list[0]
total = 0
while a < my_list[-1]+1:
    total += a
    a += 1
print("_"*35,"\n")
print(
    f"Firs number: {my_list[0]}\nSecond number: {my_list[1]}\nResult: {total}")
print("_"*35)
