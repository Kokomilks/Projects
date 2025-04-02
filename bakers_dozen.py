quantity_trays = int(input("Enter number of trays: "))

if quantity_trays < 0:
    print("Invalid input!")
elif quantity_trays == 0:
    print("No bread")
else:
    total_bread = quantity_trays * 3
    
    dozens = total_bread // 13  
    remaining_bread = total_bread % 13

    if dozens > 0 and remaining_bread > 0:
        print(f"{dozens} baker's dozen{'s' if dozens > 1 else ''} and {remaining_bread} {'loaves' if remaining_bread > 1 else 'loaf'} of bread")
    elif dozens > 0:
        print(f"{dozens} baker's dozen{'s' if dozens > 1 else ''}")
    else:
        print(f"{remaining_bread} {'loaves' if remaining_bread > 1 else 'loaf'} of bread")