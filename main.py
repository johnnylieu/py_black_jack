import random
import art

def start():
    end_game = False

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    dealers_hand = []
    players_hand = []

    print(art.logo)

    players_hand.append(random.choice(cards))
    dealers_hand.append(random.choice(cards))
    players_hand.append(random.choice(cards))
    dealers_hand.append(random.choice(cards))

    print(f'Your cards: {players_hand}, current score: {sum(players_hand)}')
    print(f'Dealer\'s first card: {dealers_hand[0]}\n')

    if sum(dealers_hand) == 21:
        print("Dealer wins.")
    elif sum(players_hand) == 21:
        print("You win!")
    else:
        while end_game == False:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")

            if hit.lower() == 'y':
                players_hand.append(random.choice(cards))
                print(f'\nYour cards: {players_hand}, current score: {sum(players_hand)}')
                print(f'Dealer\'s first card: {dealers_hand[0]}\n')

                if sum(players_hand) >= 21:
                    end_game = True

            elif hit.lower != 'y':
                while (sum(dealers_hand) < 21) and (sum(dealers_hand) <= sum(players_hand)) and (sum(players_hand) < 21) and (sum(dealers_hand) < 17):
                    dealers_hand.append(random.choice(cards))
                print(f'\nYour cards: {players_hand}, current score: {sum(players_hand)}')
                print(f'Dealer\'s cards: {dealers_hand}, current score: {sum(dealers_hand)}\n')
                end_game = True

        if (sum(dealers_hand) == 21) or (sum(players_hand) > 21):
            print("YOU LOSE 💸")
        elif (sum(dealers_hand) < 21) and (sum(dealers_hand) > sum(players_hand)):
            print("YOU LOSE 💸")
        elif sum(players_hand) > 21:
            print("YOU LOSE 💸")
        elif sum(players_hand) == 21:
            print("💵 YOU WIN")
        elif (sum(players_hand) < 21) and (sum(players_hand) > sum(dealers_hand)):
            print("💵 YOU WIN")
        elif sum(dealers_hand) > 21:
            print("💵 YOU WIN")
        elif sum(dealers_hand) == sum(players_hand):
            print("🤝🏽 IT'S A TIE")

    play_again = input(f"\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_again.lower() == 'y':
        start()

start()