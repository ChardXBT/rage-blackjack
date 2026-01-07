import random


def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [{'rank': r, 'suit': s} for s in suits for r in ranks]


def calculate_score(hand):
    score = 0
    aces = 0
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
              'A': 11}

    for card in hand:
        score += values[card['rank']]
        if card['rank'] == 'A':
            aces += 1

    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score


def get_dealer_result(player_score):
    if player_score >= 19:
        return 21, "DEALER MAGICALLY GOT 21! (Rage Logic Active)"

    # Otherwise, normal dealer logic
    dealer_score = random.randint(17, 26)  # Simulating draw
    return dealer_score, ""