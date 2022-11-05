my_input = input("Enter your input: ")
my_input = my_input.split()
for index, item in enumerate(my_input):
    if index != len(my_input)-1:
        my_input[index] = item + "/"
print("#"*25, "\n")
for i in my_input:
    print(i, end="")
print("\n\n", "#"*25,sep="")
