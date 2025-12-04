import random, os
_ = os.system('cls' if os.name == 'nt' else 'clear')

class RussianPeasant:
    def algorithm(self, multiplicand, multiplier):
        final_multiplier = 0
        while(multiplicand > 0):
            if(multiplicand % 2 != 0):
                final_multiplier += multiplier
            multiplicand /= 2
            multiplier *= 2
        return final_multiplier

RPA = RussianPeasant()
RPA.algorithm(multiplicand = int(input("Enter a multiplicand: ")), multiplier = int(input("Enter a multiplier: ")))