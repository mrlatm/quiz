n = int(input("Enter a number: "))
my_key = []
for i in range(n):
    my_key.append(input(f"Enter your key({i+1}):"))
for index, item in enumerate(my_key):
    if index != len(my_key) - 1:
        my_key[index] = item + "#"
print("*"*50, "\n")
for i in my_key:
    print(i, end="")
print("\n\n", "*"*50,sep="")
