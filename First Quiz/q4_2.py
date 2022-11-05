num = 0
while num != "exit":
    num = input("Enter a number or \"exit\": ")
    if num == "exit":
        break
    if int(num) % 2 == 0:
        print("-" * 40, "\nYour number is Even!\n", "-" * 40, sep="")
    elif int(num) % 2 != 0:
        print("-" * 40, "\nYour number is Odd!\n", "-" * 40, sep="")
