from random import randint
from art import *

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def total(total_cards):
    total_value = sum(total_cards)
    if total_value > 21 and 11 in total_cards:
        total_cards[total_cards.index(11)] = 1
        total_value = sum(total_cards)
    return total_value


player_card = []
computer_card = []

should_continue = True
while should_continue:
    player_card.clear()
    computer_card.clear()
    do_you_want_to_continue = input("Do you want to play a blackjack game? Type 'y' or 'n': ").lower()

    if do_you_want_to_continue != 'y':
        should_continue = False
        continue


    print(logo)
    player_card.extend([cards[randint(0, len(cards) - 1)], cards[randint(0, len(cards) - 1)]])
    computer_card.append(cards[randint(0, len(cards) - 1)])

    print(f"Your cards: {player_card}, current score: {total(player_card)}")
    print(f"Computer's first card: {computer_card[0]}")

    play_again = True
    while play_again:
        to_get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if to_get_card == 'y':
            player_card.append(cards[randint(0, len(cards) - 1)])
            print(f"Your cards: {player_card}, current score: {total(player_card)}")

            if total(player_card) > 21:
                print(f"Your final hand: {player_card}, final score: {total(player_card)}")
                print(f"Computer's final hand: {computer_card}, final score: {total(computer_card)}")
                print("You went over. You lose 😭")
                play_again = False
        else:
            while total(computer_card) < 17:
                computer_card.append(cards[randint(0, len(cards) - 1)])

            print(f"Your final hand: {player_card}, final score: {total(player_card)}")
            print(f"Computer's final hand: {computer_card}, final score: {total(computer_card)}")

            if total(player_card) > 21:
                print("You went over. You lose 😭")
            elif total(computer_card) > 21:
                print("Computer went over. You win!")
            elif total(player_card) > total(computer_card):
                print("You win!")
            elif total(player_card) < total(computer_card):
                print("You lose.")
            else:
                print("It's a draw.")

            play_again = False
