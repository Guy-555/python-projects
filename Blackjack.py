import random

cards = [11, 2, 3, 4, 5 ,6 ,7, 8 ,9 ,10, 10, 10, 10]

restart = 'y'

def score(card_list):
    total_score = 0
    for card in card_list:
        total_score += card
    return total_score

def checker(player_com):
    for c in hands[player_com]:
        if score(hands[player_com]) > 21 and c == 11:
            hands[player_com][hands[player_com].index(c)] = 1
    if score(hands[player_com]) > 21 and player_com == "player":
        return "Player Lose"
    elif score(hands[player_com]) > 21 and player_com == "computer":
        return "Computer Lose"

while restart == 'y':
    hands = {
        "player": [],
        "computer": []
    }
    hit = 'y'
    result = ''
    computer_card = random.choice(cards)
    hands["computer"].append(computer_card)
    while hit == 'y':
        player_card = random.choice(cards)
        hands["player"].append(player_card)
        if score(hands["player"]) == 21:
            hit = 'Blackjack'
        if len(hands["player"]) >= 2 and score(hands["player"]) != 21:
            result = checker("player")
            if result != "Player Lose":
                print(f"Your cards: {hands["player"]}, current score: {score(hands["player"])}")
                print(f"Computer's first card: {hands["computer"][0]}")
                hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            else:
                hit = 'went over'
    while hit == 'n':
        computer_card = random.choice(cards)
        hands["computer"].append(computer_card)
        result = checker("computer")
        if result != "Computer Lose":
            r = random.randint(1, 10)
            if score(hands["computer"]) > 11 and (r > 10 - score(hands["computer"]) % 10 or score(hands["computer"]) >= 20):
                hit = 'no'
        else:
            hit = 'went over'

    print(f"Your final hand: {hands["player"]}, final score: {score(hands["player"])}")
    print(f"Computer's final hand: {hands["computer"]}, final score: {score(hands["computer"])}")

    if result == "Player Lose":
        print("You went over. You lose 😭")
    elif result == "Computer Lose":
        print("Opponent went over. You win 😁")
    elif score(hands["computer"]) == 21 and len(hands["computer"]) == 2:
        print("Lose, opponent has Blackjack 😱")
    elif score(hands["player"]) == 21 and len(hands["player"]) == 2:
        print("Win with a Blackjack 😎")
    elif score(hands["computer"]) < score(hands["player"]):
        print("You win 😃")
    elif score(hands["computer"]) > score(hands["player"]):
        print("You lose 😤")
    else:
        print("Draw 🙃")

    restart = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()