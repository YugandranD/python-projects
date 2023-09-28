# rock paper scissor game with best of three wins
import random

# intiallizing player and computer wins

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    choices = ["rock", "paper", "scissor"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissor: ").lower()

    if player == computer:
        print("computer:", computer)
        print("player:", player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("Computer wins!")
            computer_wins += 1

        elif computer == "scissor":
            print("computer:", computer)
            print("player:", player)
            print("You win!")
            player_wins += 1

    elif player == "paper":
        if computer == "scissor":
            print("computer:", computer)
            print("player:", player)
            print("Computer wins!")
            computer_wins += 1

        elif computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("You win!")
            player_wins += 1

    elif player == "scissor":
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("Computer wins!")
            computer_wins += 1

        elif computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("You win!")
            player_wins += 1

    print("Player wins:", player_wins)
    print("Computer wins:", computer_wins)

    if player_wins < 2 and computer_wins < 2:
        play_again = input("Play again? (yes or no): ").lower()

        if play_again != "yes":
            break

print("Bye!")

