import sys, os

if os.name == 'nt':
    _ = os.system('cls')
else:
    _ = os.system('clear')

prices = {
    "1": 150000.0,
    "2": 170000.0,
    "3": 210000.0
}

print('''Types of Condominium Units
1: Park view: $150,000.00
2: Golf course view: $170,000.00
3: Lake view: $210,000.00
''')

type_of_condominium = input("Enter type of condominium unit [1, 2, or 3]: ")

if type_of_condominium not in prices:
    sys.exit("\nInvalid type of condominium. Please enter a valid option: 1, 2, or 3.")

quantity = input("Number of units to be bought: ")

if not quantity.isdigit() or int(quantity) <= 0:
    sys.exit("\nInvalid quantity. Please enter a positive number.")

price = prices[type_of_condominium]
quantity = int(quantity)
amount_due = price * quantity

view = {"1": "Park", "2": "Golf course", "3": "Lake"}[type_of_condominium]

print(f"\n{quantity} {view} view condominium unit{' is' if quantity == 1 else 's are'} priced at ${amount_due:,.2f}.")
