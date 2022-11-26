import random
import art

def start():
    end_game = False

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    dealers_hand = []
    players_hand = []

    print(art.logo)

    dealers_hand.append(random.choice(cards))
    dealers_hand.append(random.choice(cards))
    players_hand.append(random.choice(cards))
    players_hand.append(random.choice(cards))

    print(f'Your cards: {players_hand}, current score: {sum(players_hand)}')
    print(f'Dealder\'s first card: {dealers_hand[0]}\n')

    while end_game == False:
        if sum(dealers_hand) < 17:
            dealers_hand.append(random.choice(cards))
            if sum(dealers_hand) > 21 or sum(dealers_hand) == 21:
                end_game = True
        
        if sum(players_hand) > 21 or sum(players_hand) == 21:
            end_game = True
            
        if sum(players_hand) < 21:
            get_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if get_card.lower() == 'y':
                players_hand.append(random.choice(cards))
            else:
                while sum(dealers_hand) < 21:
                    dealers_hand.append(random.choice(cards))

                    print(f'\nYour cards: {players_hand}, current score: {sum(players_hand)}')
                    print(f'Dealder\'s cards: {dealers_hand}, current score: {sum(dealers_hand)}\n')

        print(f'\nYour cards: {players_hand}, current score: {sum(players_hand)}')
        print(f'Dealder\'s cards: {dealers_hand}, current score: {sum(dealers_hand)}\n')

    if sum(dealers_hand) == 21 or sum(players_hand) > 21:
        print("you lose")
    elif sum(dealers_hand) < 21 and sum(dealers_hand) > sum(players_hand):
        print("you lose")
    elif sum(players_hand) > 21:
        print("you lose")
    elif sum(players_hand) == 21:
        print("you win")
    elif sum(players_hand) < 21 and sum(players_hand) > sum(dealers_hand):
        print("you win")
    elif sum(dealers_hand) > 21:
        print("you win")
    else:
        print("it's a tie")

    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_again.lower() == 'y':
        start()

start()