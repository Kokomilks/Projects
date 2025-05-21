# use of for loop
count = int(input("Enter number of inputs: "))

print("Enter values")
numbers = []
counter = 1
for counter in range(1, count + 1):
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

# use of while loop
count = int(input("Enter number of inputs: "))

print("Enter values")
numbers = []
counter = 1
for counter in range(count):
    print(f"{counter + 1}. ", end='')
    number = int(input())
    numbers.append(number)
    counter += 1

print("\nEven numbers: ", end='')
index = 0
while index < count:
    if numbers[index] % 2 == 0:
        print(numbers[index], end=' ')
    index += 1

print("\nOdd numbers: ", end='')
index = 0
while index < count:
    if numbers[index] % 2 != 0:
        print(numbers[index], end=' ')
    index += 1
