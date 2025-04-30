size = int(input("Enter size of base: "))

print()
row = 1
while row <= size:
    column = 1
    while column <= row:
        print("* ", end='')
        column += 1
    print()
    row += 1

size = int(input("Enter size of base: "))

count = 1
while count <= size:
    print((' ' * (size - count)) + ("*" * count))
    count += 1
