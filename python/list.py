<<<<<<< HEAD

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


string = input("Enter a word: ") [::-1]
print(string)


a = 10
b = 20
c = 15

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c
print(largest)


number = int(input("Enter a number: "))

if number <= 1:
    print("Not prime")
else:
    for i in range(2, int(number ** 0.5) + 1):  # Loop from 2 to the square root of n
        if number % i == 0:  # If number is divisible by i
            print("Not Prime")
            break
    else:
        print("Prime")


for i in range(1, 11):
    print(i)


total = 0

for i in range(1, 101):
    total += i
print(total)

input_string = "hello"

count = 0

for i in input_string:
    if i in "aeiou": 
        count += 1
print(count)

n = 5

for i in range(1, 11):
    product = n * i
    print(f"{n} x {i} = {product}")

=======

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


string = input("Enter a word: ") [::-1]
print(string)


a = 10
b = 20
c = 15

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c
print(largest)


number = int(input("Enter a number: "))

if number <= 1:
    print("Not prime")
else:
    for i in range(2, int(number ** 0.5) + 1):  # Loop from 2 to the square root of n
        if number % i == 0:  # If number is divisible by i
            print("Not Prime")
            break
    else:
        print("Prime")


for i in range(1, 11):
    print(i)


total = 0

for i in range(1, 101):
    total += i
print(total)

input_string = "hello"

count = 0

for i in input_string:
    if i in "aeiou": 
        count += 1
print(count)

n = 5

for i in range(1, 11):
    product = n * i
    print(f"{n} x {i} = {product}")

>>>>>>> eb5526b (none)
