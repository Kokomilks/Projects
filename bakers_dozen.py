trays = int(input("Enter number of trays: "))

if trays < 0:
    print("Invalid input!")
elif trays == 0:
    print("No bread")
else:
    total_loaves = trays * 3
    
    dozens = total_loaves // 13  
    remaining_loaves = total_loaves % 13

    if dozens > 0 and remaining_loaves > 0:
        print(f"{dozens} baker's dozen{'s' if dozens > 1 else ''} and {remaining_loaves} {'loaves' if remaining_loaves > 1 else 'loaf'} of bread")
    elif dozens > 0:
        print(f"{dozens} baker's dozen{'s' if dozens > 1 else ''}")
    else:
        print(f"{remaining_loaves} {'loaves' if remaining_loaves > 1 else 'loaf'} of bread")