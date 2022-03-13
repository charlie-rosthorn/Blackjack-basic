import random

# Deck
deck = [
    2, 2, 2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    5, 5, 5, 5,
    6, 6, 6, 6,
    7, 7, 7, 7,
    8, 8, 8, 8,
    9, 9, 9, 9,
    10, 10, 10, 10,
    ]

# Computer cards

computer_card1 = random.choice(deck)
print("Computer number: " + str(computer_card1))
computer_card2 = random.choice(deck)
print("Computer number: " + str(computer_card2))
computer = computer_card1 + computer_card2
print("Total: " + str(computer))

# Initial Draw

user_card1 = random.choice(deck)
print("User number: " + str(user_card1))
user_card2 = random.choice(deck)
print("User number: " + str(user_card2))
user = user_card1 + user_card2
print("Total: " + str(user))

# Stick or Twist

if user < 21:
    question1 = input("Would you like to stick or twist?\n")
    if question1 == "twist":
        user_card3 = random.choice(deck)
        print("User number: " + str(user_card3))
        user = user_card1 + user_card2 + user_card3
        print("Current Total: " + str(user))
        if user_card3 + user < 21:
            question2 = input("Would you like to stick or twist?\n")
            if question2 == "twist":
                user_card4 = random.choice(deck)
                print("User number: " + str(user_card4))
                user = user_card1 + user_card2 + user_card3 + user_card4
                print("Current Total: " + str(user))
                if user_card3 + user_card4 + user < 21:
                    question3 = input("Would you like to stick or twist?\n")
                    if question3 == "twist":
                        user_card5 = random.choice(deck)
                        print("User number: " + str(user_card5))
                        user = user_card1 + user_card2 + user_card3 + user_card4 + user_card5
                        print("Current Total: " + str(user))


if user <= 21 and user > computer:
    computer_card3 = random.choice(deck)
    print("Computer number: " + str(computer_card3))
    computer = computer_card1 + computer_card2 + computer_card3
    print("Current Total: " + str(computer))
    if user <= 21 and user > computer:
        computer_card4 = random.choice(deck)
        print("Computer number: " + str(computer_card4))
        computer = computer_card1 + computer_card2 + computer_card3 + computer_card4
        print("Current Total: " + str(computer))
        if user <= 21 and user > computer:
            computer_card5 = random.choice(deck)
            print("Computer number: " + str(computer_card5))
            computer = computer_card1 + computer_card2 + computer_card3 + computer_card4 + computer_card5
            print("Current Total: " + str(computer))


# Results

if user <= 21 and (user > computer or computer > 21):
    print("User wins!")
elif user > 21 or (computer > user and computer < 22):
    print("Computer wins!")
else:
    print("Tie!")
