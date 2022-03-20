import random
import functools

# Setup

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

computer_hand = []
player_hand = []

# Computer cards


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
    else:
        computer_hand.append(11)
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
    else:
        player_hand.append(11)
        return new_card_key


print("Computer:")
computer_card1 = draw_card_computer()
print(computer_card1)
computer_card2 = draw_card_computer()
print("(facedown card) \nRevealed Total: " + str(computer_card1))
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
            another_Card = draw_card_player()
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
    another_Card = draw_card_computer()
    print(another_Card)
    computer_total = functools.reduce(lambda x, y: x + y, computer_hand)
    if (computer_total < player_total) and (computer_total <= 21):
        another_Card = draw_card_computer()
        computer_total = functools.reduce(lambda x, y: x + y, computer_hand)
        if (computer_total < player_total) and (computer_total <= 21):
            another_Card = draw_card_computer()
            computer_total = functools.reduce(lambda x, y: x + y, computer_hand)
print("Computer total:  " + str(computer_total))

if ((player_total <= 21) and (player_total > computer_total)) or computer_total > 21:
    print("Player has won!")
elif ((computer_total > player_total) and (computer_total <= 21)) or player_total > 21:
    print("Player has lost!")
else:
    print("Tie!")
