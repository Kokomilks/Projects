<<<<<<< HEAD


# Input the wood type, table size, and quantity
wood_type = str(input("Enter type of wood [P, O, M]: "))
table_size = str(input("Enter size of table [S, M, L]: "))
table_quantity = int(input("Enter number of tables: "))

cost = None
wood = ""

# To determine if the input met the following
# conditions then initialize the corresponding values
if wood_type.lower() == "p":
    cost = 100
    wood = "pine"
elif wood_type.lower() == "o":
    cost = 225
    wood = "oak"
elif wood_type.lower() == "m":
    cost = 310
    wood = "mahogany"
else:
    print("Invalid type of wood")

size = None

if table_size.lower() == "s":
    cost += 0
    size = "small"
elif table_size.lower() == "m":
    cost += 15
    size = "medium"
elif table_size.lower() == "l":
    cost += 25
    size = "large"
else:
    print("Invalid size of table")

# Calculate the total cost
total = cost * table_quantity

# Display the output
print(f"{table_quantity} {size} {wood} tables cost ${total:,.2f}")


# Shortened code using dictionaries

import sys, re, os

os.system("cls")

# Mappings for wood types and table sizes
wood_prices = {'p': 100, 'o': 225, 'm': 310}
wood_names = {'p': 'pine', 'o': 'oak', 'm': 'mahogany'}
size_prices = {'s': 0, 'm': 15, 'l': 25}
size_names = {'s': 'small', 'm': 'medium', 'l': 'large'}

# Input the wood type, table size, and quantity
wood_type = input("Enter type of wood [P, O, M]: ").lower()
if wood_type not in ['p', 'o', 'm']:
    print("\nInvalid wood type")
    sys.exit(0)

table_size = input("Enter size of table [S, M, L]: ").lower()
if wood_type not in ['s', 'm', 'l']:
    print("\nInvalid table size")
    sys.exit(0)

table_quantity = int(input("Enter number of tables: "))
if re.match("^[+]?([1-9]/d*|0)$", table_quantity) is None:
    sys.exit("\nInvalid quantity")

# Check for valid wood type and size
if wood_type not in wood_prices or table_size not in size_prices:
    print("Invalid input")
else:
    cost = wood_prices[wood_type] + size_prices[table_size]
    wood = wood_names[wood_type]
    size = size_names[table_size]

    # Calculate the total cost
    total = cost * int(table_quantity)

    # Display the output
    print(f"{table_quantity} {size} {wood} tables cost ${total:,.2f}")
=======


# Input the wood type, table size, and quantity
wood_type = str(input("Enter type of wood [P, O, M]: "))
table_size = str(input("Enter size of table [S, M, L]: "))
table_quantity = int(input("Enter number of tables: "))

cost = None
wood = ""

# To determine if the input met the following
# conditions then initialize the corresponding values
if wood_type.lower() == "p":
    cost = 100
    wood = "pine"
elif wood_type.lower() == "o":
    cost = 225
    wood = "oak"
elif wood_type.lower() == "m":
    cost = 310
    wood = "mahogany"
else:
    print("Invalid type of wood")

size = None

if table_size.lower() == "s":
    cost += 0
    size = "small"
elif table_size.lower() == "m":
    cost += 15
    size = "medium"
elif table_size.lower() == "l":
    cost += 25
    size = "large"
else:
    print("Invalid size of table")

# Calculate the total cost
total = cost * table_quantity

# Display the output
print(f"{table_quantity} {size} {wood} tables cost ${total:,.2f}")


# Shortened code using dictionaries

import sys, re, os

os.system("cls")

# Mappings for wood types and table sizes
wood_prices = {'p': 100, 'o': 225, 'm': 310}
wood_names = {'p': 'pine', 'o': 'oak', 'm': 'mahogany'}
size_prices = {'s': 0, 'm': 15, 'l': 25}
size_names = {'s': 'small', 'm': 'medium', 'l': 'large'}

# Input the wood type, table size, and quantity
wood_type = input("Enter type of wood [P, O, M]: ").lower()
if wood_type not in ['p', 'o', 'm']:
    print("\nInvalid wood type")
    sys.exit(0)

table_size = input("Enter size of table [S, M, L]: ").lower()
if wood_type not in ['s', 'm', 'l']:
    print("\nInvalid table size")
    sys.exit(0)

table_quantity = int(input("Enter number of tables: "))
if re.match("^[+]?([1-9]/d*|0)$", table_quantity) is None:
    sys.exit("\nInvalid quantity")

# Check for valid wood type and size
if wood_type not in wood_prices or table_size not in size_prices:
    print("Invalid input")
else:
    cost = wood_prices[wood_type] + size_prices[table_size]
    wood = wood_names[wood_type]
    size = size_names[table_size]

    # Calculate the total cost
    total = cost * int(table_quantity)

    # Display the output
    print(f"{table_quantity} {size} {wood} tables cost ${total:,.2f}")
>>>>>>> eb5526b (none)
