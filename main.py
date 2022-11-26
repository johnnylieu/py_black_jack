import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealers_hand = []
players_hand = []

print(art.logo)

dealers_hand.append(random.choice(cards))
players_hand.append(random.choice(cards))

print(f'Your cards: {players_hand}, current score: {sum(players_hand)}')
print(f'Dealder\'s cards: {dealers_hand}, current score: {sum(dealers_hand)}')