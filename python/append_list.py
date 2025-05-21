count = int(input("Enter number of inputs: "))

print("Enter values")
numbers = []
counter = 1
while counter <= count:
    print(f"{counter}. ", end='')
    number = int(input())
    numbers.append(number)
    counter += 1

print("\nEven numbers: ", end='')
for number in numbers:
    if number % 2 == 0:
        print(number, end=' ')


print("\nOdd numbers: ", end='')
for number in numbers:
    if number % 2 != 0:
        print(number, end=' ')
