multiplicand = 12
multiplier = 4
final_multiplier = 0
while(multiplicand > 0):
    if(multiplicand % 2 != 0):
        final_multiplier += multiplier
    multiplicand /= 2
    multiplier *= 2
print(final_multiplier)