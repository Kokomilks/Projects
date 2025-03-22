import sys
import os

# Clear screen cross-platform
_ = os.system('cls' if os.name == 'nt' else 'clear')

# Shortened code using dictionaries

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
if table_size not in ['s', 'm', 'l']:
    print("\nInvalid table size")
    sys.exit(0)

table_quantity = input("Enter number of tables: ")
try:
    table_quantity = int(table_quantity)
    if table_quantity <= 0:
        print("\nQuantity must be a positive number")
        sys.exit(0)
except ValueError:
    print("\nPlease enter a valid number")
    sys.exit(0)

# Check for valid wood type and size
if wood_type not in wood_prices or table_size not in size_prices:
    print("Invalid input")
    sys.exit(0)

cost = wood_prices[wood_type] + size_prices[table_size]
wood = wood_names[wood_type]
size = size_names[table_size]

# Calculate the total cost
total = cost * table_quantity

# Display the output
print(f"{table_quantity} {size} {wood} tables cost ${total:,.2f}")
