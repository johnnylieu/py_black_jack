import random
import art
from os import system, name

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

def show_partial_hand(players_hand, dealers_hand):
    return f'\nš Your cards: {players_hand}, current score: {sum(players_hand)}\nš“ Dealer\'s first card: {dealers_hand[0]}\n'

def show_hands(players_hand, dealers_hand):
    return f'\nš Your cards: {players_hand}, current score: {sum(players_hand)}\nš“ Dealer\'s cards: {dealers_hand}, current score: {sum(dealers_hand)}\n'

def initial_comparison(players_hand, dealers_hand):
    # can't have a return in here because it will end game
    if (sum(dealers_hand) == 21) and (sum(players_hand) != 21):
        print(show_hands(dealers_hand, players_hand))
        print("Dealer wins šø")
    elif (sum(players_hand) == 21) and (sum(dealers_hand) != 21):
        print(show_hands(dealers_hand, players_hand))
        print("šµ YOU WIN!")
    elif (sum(players_hand) == 21) and (sum(dealers_hand) == 21):
        show_hands(players_hand, dealers_hand)
        print("š¤š½ IT'S A TIE")

def compare_score(players_hand, dealers_hand):
    if (sum(dealers_hand) == 21) or (sum(players_hand) > 21):
        return "YOU LOSE šø"
    elif (sum(dealers_hand) < 21) and (sum(dealers_hand) > sum(players_hand)):
        return "YOU LOSE šø"
    elif sum(players_hand) > 21:
        return "YOU LOSE šø" 
    elif sum(players_hand) == 21:
        return "šµ YOU WIN"
    elif (sum(players_hand) < 21) and (sum(players_hand) > sum(dealers_hand)):
        return "šµ YOU WIN"
    elif sum(dealers_hand) > 21:
        return "šµ YOU WIN"
    elif sum(dealers_hand) == sum(players_hand):
        return "š¤š½ IT'S A TIE"

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def start():
    clear()
    end_game = False

    dealers_hand = []
    players_hand = []

    print(art.logo)

    for i in range(2):
        players_hand.append(deal_cards())
        dealers_hand.append(deal_cards())

    print(show_partial_hand(players_hand, dealers_hand))
    initial_comparison(players_hand, dealers_hand)

    while end_game == False:
        hit = input("Type 'y' to get another card, type 'n' to pass: ")

        if hit.lower() == 'y':
            players_hand.append(deal_cards())

            if sum(players_hand) >= 21:
                end_game = True
            print(show_partial_hand(players_hand, dealers_hand))

        elif hit.lower != 'y':
            while (sum(dealers_hand) < 21) and (sum(dealers_hand) <= sum(players_hand)) and (sum(players_hand) < 21) and (sum(dealers_hand) < 17):
                dealers_hand.append(deal_cards())
            end_game = True
    
    print(show_hands(players_hand, dealers_hand))
    print(compare_score(players_hand, dealers_hand))

    play_again = input(f"\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_again.lower() == 'y':
        start()

start()