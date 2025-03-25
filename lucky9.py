import random, os
_ = os.system('cls' if os.name == 'nt' else 'clear')

# deck of cards - 52 cards
# 4 suits - hearts diamonds cloves spades
# 13 faces - aces (1) 2 3 4 5 6 7 8 9 10 jack (11) queen (12) king (13)
# randrange (1, 14) = to randomize between 1 to 13
# randint (1, 13) = to randomize between 1 to 13

print("Lucky 9 Simulation")

card1 = random.randint(1, 13)
card2 = random.randint(1, 13)

print(f"Card 1 = {card1}\nCard 2 = {card2}")

card = (card1 + card2) % 10
card3 = -1

if card >= 0 and card <= 6: # not good, need to draw third card
    card3 = random.randint(1, 13)
    print(f"Card 3 = {card3}")
    card = (card + card3) % 10

print(f"Your card is {card}.")