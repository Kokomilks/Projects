quantity_trays = int(input("Enter number of trays: "))

if quantity_trays < 0:
    print("Invalid input!")
elif quantity_trays == 0:
    print("No bread baked")
else:
    total_bread = quantity_trays * 3
    
    dozen_bread = total_bread // 13  
    remaining_bread = total_bread % 13

    if dozen_bread > 0 and remaining_bread > 0:
        print(f"{dozen_bread} baker's dozen{'s' if dozen_bread > 1 else ''} and {remaining_bread} {'loaves' if remaining_bread > 1 else 'loaf'} of bread")
    elif dozen_bread > 0:
        print(f"{dozen_bread} baker's dozen{'s' if dozen_bread > 1 else ''}")
    else:
        print(f"{remaining_bread} {'loaves' if remaining_bread > 1 else 'loaf'} of bread")