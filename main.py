import random

import config
from listing import create_deck, calculate_score, get_dealer_result


def play_round(balance):
    print(f"\n--- New Hand | Balance: ${balance} ---")
    bet = int(input(f"Enter bet (Min ${config.MIN_BET}): "))

    deck = create_deck()
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    print(f"Your hand: {[c['rank'] for c in player_hand]}")

    # Simple Hit/Stand loop
    while calculate_score(player_hand) < 21:
        action = input("Hit or Stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            print(f"Your hand: {[c['rank'] for c in player_hand]}")
        else:
            break

    p_score = calculate_score(player_hand)

    if p_score > 21:
        print("Bust! You lose.")
        return balance - bet


    d_score, msg = get_dealer_result(p_score)
    if msg: print(msg)
    print(f"Dealer Score: {d_score}")

    if d_score > 21 or p_score > d_score:
        print("You Win!")
        return balance + bet
    else:
        print("Dealer Wins. Rage much?")
        return balance - bet


# Start Game
current_balance = config.STARTING_BALANCE
while current_balance > 0:
    current_balance = play_round(current_balance)