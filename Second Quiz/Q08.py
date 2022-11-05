# numbers = input("Enter numbers: ")
numbers = "12 14 15 15"
numbers = numbers.split()
total1 = 0
for index, item in enumerate(numbers):
    numbers[index] = int(item)
    total1 += numbers[index]
total2 = sum(numbers)
print("_"*50, "\n")
print(f"First way \'sum\': {total1}\nSecond way \'sum\': {total2}")
print("_"*50)
