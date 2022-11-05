num_list = input("Enter your number's: ")
print("-" * 95)

num_list = num_list.split()
counter = 0
not_digit = []
for i in num_list:
    if i.isdigit():
        counter += 1
    else:
        not_digit.append(i)
if counter == len(num_list):
    print(
        f"Befor runing my codes:\nyour input: {num_list}  ,  Type list: {type(num_list)}  ,  Type item: {type(num_list[0])}\n")
    for index, item in enumerate(num_list):
        num_list[index] = int(item)
    print(
        f"After runing my codes:\nmy output: {num_list}  ,  Type list: {type(num_list)}  ,  Type item: {type(num_list[0])}")
else:
    print(f"Your input is not \"digit\"! {not_digit}")
print("-" * 95)
