number = int(input("Enter a number: "))

row = 1
while row <= number:
    column = 1
    while column <= number:
        print(row * column, end=' ')
        column += 1
    print()
    row += 1