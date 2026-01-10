import sys

number = int(input("Enter a number: "))
if number < 0:
    sys.exit("\nInvalid Input")

sum = 0
counter = 1
while counter <= number:
    sum += counter
    counter += 1
print(f"\nSum is {sum}.")

print()