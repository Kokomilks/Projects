size = int(input("Enter size of a square's width and length: "))

row = 1
while row <= size:
    column = 1
    while column <= size:
        print("*", end='')
        column = 1
    print()
    row += 1

size = int(input("Enter size of a square's width and length: "))

row = 1
while row <= size:
    print('*' * size)
    row += 1
