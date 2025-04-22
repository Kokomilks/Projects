number = int(input("Enter a number: "))

divisor = 2
print(f"Factors of {number} are: 1", end=' ')

while divisor <= number // 2:
    if divisor % number == 0:
        print(divisor, end=' ')
    divisor += 1

print(number)