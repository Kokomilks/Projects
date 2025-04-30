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
    print((' ' * (size - count)) + ("* " * count))
    count += 1

size = int(input("Enter size of base: "))

print()
row = 1
while row <= size:
    column = 1
    while column <= size - row:
        print("* ", end='')
        column += 1
    print()
    row += 1
size = int(input("Enter size of base: "))

print()
row = 1
while row <= size:
    column = 1
    while column <= row:
        print(column, end=' ')
        column += 1
    print()
    row += 1

size = int(input("Enter size of base: "))

print()
row = 1
while row <= size:
    print(" " * (size - row), end='')
    column = row
    while column > 1:
        print(column, end='')
        column -= 1
    column = 1
    while column <= row:
        print(column, end='')
        column += 1
    print()
    row += 1
