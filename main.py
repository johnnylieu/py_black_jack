import random
import art

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
    return f'\nYour cards: {players_hand}, current score: {sum(players_hand)}\nDealer\'s first card: {dealers_hand[0]}\n'

def show_hands(players_hand, dealers_hand):
    return f'\nYour cards: {players_hand}, current score: {sum(players_hand)}\nDealer\'s cards: {dealers_hand}, current score: {sum(dealers_hand)}\n'

def compare_score(dealers_hand, players_hand):
    print(show_hands(players_hand, dealers_hand))
    if (sum(dealers_hand) == 21) or (sum(players_hand) > 21):
        return "YOU LOSE 💸"
    elif (sum(dealers_hand) < 21) and (sum(dealers_hand) > sum(players_hand)):
        return "YOU LOSE 💸"
    elif sum(players_hand) > 21:
        return "YOU LOSE 💸" 
    elif sum(players_hand) == 21:
        return "💵 YOU WIN"
    elif (sum(players_hand) < 21) and (sum(players_hand) > sum(dealers_hand)):
        return "💵 YOU WIN"
    elif sum(dealers_hand) > 21:
        return "💵 YOU WIN"
    elif sum(dealers_hand) == sum(players_hand):
        return "🤝🏽 IT'S A TIE"

def start():
    end_game = False

    dealers_hand = []
    players_hand = []

    print(art.logo)

    players_hand.append(deal_cards())
    dealers_hand.append(deal_cards())
    players_hand.append(deal_cards())
    dealers_hand.append(deal_cards())

    print(show_partial_hand(players_hand, dealers_hand))

    if (sum(dealers_hand) == 21) and (sum(players_hand) != 21):
        print(show_hands(dealers_hand, players_hand))
        print("Dealer wins 💸")
    elif (sum(players_hand) == 21) and (sum(dealers_hand) != 21):
        print(show_hands(dealers_hand, players_hand))
        print("💵 YOU WIN!")
    elif (sum(players_hand) == 21) and (sum(dealers_hand) == 21):
        print("🤝🏽 IT'S A TIE")
    else:
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
        
        print(compare_score(dealers_hand, players_hand))

    play_again = input(f"\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_again.lower() == 'y':
        start()

start()