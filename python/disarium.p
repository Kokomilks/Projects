number = input("Enter a number: ")

digits = []
for digit in number:
    digits.append(int(digit))

disarium = 0
power = 0
while power < len(digits):
    disarium += digits[power] ** (power + 1)
    power += 1

if disarium == int(number):
    print(f"\n")
