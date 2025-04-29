number = int(input("Enter a number: "))

row = 1
while row <= n:
    column = 1
    while column <= n:
        print(row * column, end=' ')
        column += 1
    print()
    row += 1