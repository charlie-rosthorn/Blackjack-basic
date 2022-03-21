import random
import functools


def blackjack_game():

    deck = (
        "2", "2", "2", "2",
        "3", "3", "3", "3",
        "4", "4", "4", "4",
        "5", "5", "5", "5",
        "6", "6", "6", "6",
        "7", "7", "7", "7",
        "8", "8", "8", "8",
        "9", "9", "9", "9",
        "10", "10", "10", "10",
        "J", "J", "J", "J",
        "Q", "Q", "Q", "Q",
        "K", "K", "K", "K",
        "A", "A", "A", "A")

    twist_responses = ("Twist", "T", " Twist", " T")
    stick_responses = ("Stick", "S", " Stick", " S")

    computer_hand = [0]
    player_hand = [0]

    def draw_card_computer():

        new_card_key = random.choice(deck)
        if new_card_key.isdigit():
            computer_hand.append(int(new_card_key))
            return new_card_key
        elif new_card_key == "J":
            computer_hand.append(10)
            return new_card_key
        elif new_card_key == "Q":
            computer_hand.append(10)
            return new_card_key
        elif new_card_key == "K":
            computer_hand.append(10)
            return new_card_key
        elif new_card_key == "A" and (functools.reduce(lambda x, y: x + y, computer_hand) <= 10):
            computer_hand.append(11)
            return new_card_key
        elif new_card_key == "A":
            computer_hand.append(1)
            return new_card_key

    def draw_card_player():

        new_card_key = random.choice(deck)
        if new_card_key.isdigit():
            player_hand.append(int(new_card_key))
            return new_card_key
        elif new_card_key == "J":
            player_hand.append(10)
            return new_card_key
        elif new_card_key == "Q":
            player_hand.append(10)
            return new_card_key
        elif new_card_key == "K":
            player_hand.append(10)
            return new_card_key
        elif new_card_key == "A" and (functools.reduce(lambda x, y: x + y, player_hand) <= 10):
            player_hand.append(11)
            return new_card_key
        elif new_card_key == "A":
            player_hand.append(1)
            return new_card_key

    print("Computer:")
    computer_card1 = draw_card_computer()
    print(computer_card1)
    draw_card_computer()
    print("(face-down card) \nRevealed Total: " + str(computer_card1))
    computer_total = functools.reduce(lambda x, y: x + y, computer_hand)
    print("")
    print("Player:")
    player_card1 = draw_card_player()
    print(player_card1)
    player_card2 = draw_card_player()
    print(player_card2)
    player_total = functools.reduce(lambda x, y: x + y, player_hand)
    print("Player Total:  " + str(player_total))

    if player_total != 21:
        proceed = 0
        while proceed == 0:
            stick_or_twist = input("Would you like to twist or stick?\n").capitalize()
            if stick_or_twist in twist_responses:
                another_card = draw_card_player()
                print(another_card)
                player_total = functools.reduce(lambda x, y: x + y, player_hand)
                print("Player Total:  " + str(player_total))
                if player_total < 21:
                    proceed = 0
                if player_total > 21:
                    proceed = 1
            elif stick_or_twist in stick_responses:
                proceed += 1
            else:
                print("Sorry, please try again.")

    if (player_total <= 21) and (player_total >= computer_total):
        print("Computer's Turn")
        print("Computer Total:  " + str(computer_total))
        another_card = draw_card_computer()
        print(another_card)
        computer_total = functools.reduce(lambda x, y: x + y, computer_hand)
        if (computer_total < player_total) and (computer_total <= 21):
            another_card = draw_card_computer()
            print(another_card)
            computer_total = functools.reduce(lambda x, y: x + y, computer_hand)
            if (computer_total < player_total) and (computer_total <= 21):
                another_card = draw_card_computer()
                print(another_card)
                computer_total = functools.reduce(lambda x, y: x + y, computer_hand)

    print("Computer total:  " + str(computer_total))

    if ((player_total <= 21) and (player_total > computer_total)) or computer_total > 21:
        print("Player has won!")
        return 5
    elif ((computer_total > player_total) and (computer_total <= 21)) or player_total > 21:
        print("Player has lost!")
        return 4
    else:
        print("Tie! No points!")
        return 3


yes_responses = ("Yes", "Y", " Yeah", " Yep")
no_responses = ("No", "N", " Nah", " Nope")

game_total_player = 0
game_total_computer = 0

result = blackjack_game()
if result == 5:
    game_total_player += 1
    print(str(game_total_player) + " - " + str(game_total_computer))
elif result == 4:
    game_total_computer += 1
    print(str(game_total_player) + " - " + str(game_total_computer))
else:
    print(str(game_total_player) + " - " + str(game_total_computer))
replay_counter = 0
replay = input("Would you like to play again?\n").capitalize()
while replay_counter == 0:
    if replay in yes_responses:
        result = blackjack_game()
        if result == 5:
            game_total_player += 1
            print(str(game_total_player) + " - " + str(game_total_computer))
        elif result == 4:
            game_total_computer += 1
            print(str(game_total_player) + " - " + str(game_total_computer))
        else:
            print(str(game_total_player) + " - " + str(game_total_computer))
    if replay in no_responses:
        replay_counter += 1
    else:
        replay = input("Would you like to play again?\n").capitalize()

print("Grand Total: " + (str(game_total_player) + " - " + str(game_total_computer)))
if game_total_player > game_total_computer:
    print("Overall winner: Player!")
elif game_total_computer > game_total_player:
    print("Overall winner: Computer!")
else:
    print("Overall Tie!")
print("Bye for now!")
