my_list = input("Enter name's:").split()
print("_"*20, "\n")
for index, item in enumerate(my_list):
    if item.lower() != "asghar":
        print("Hello", item)
print("_"*20)
print("Finish")
