import random

print("===================================")
print("       ROCK PAPER SCISSORS")
print("===================================")

# Available choices
choices = ["rock", "paper", "scissors"]

# Scoreboard
player_score = 0
computer_score = 0
draws = 0

while True:

    print("\n========== GAME MENU ==========")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    print("===============================")

    user_choice = input("\nEnter your choice (1-4): ")

    if user_choice == "4":
        break

    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice! Try again.")
        continue

    # Get player choice
    player = choices[int(user_choice) - 1]

    # Computer randomly selects
    computer = random.choice(choices)

    print("\nYou selected:", player)
    print("Computer selected:", computer)

    # Decide the winner
    if player == computer:
        print("\nIt's a Draw!")
        draws += 1

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("\nCongratulations! You Won!")
        player_score += 1

    else:
        print("\nComputer Wins!")
        computer_score += 1

    # Display current score
    print("\n========== SCOREBOARD ==========")
    print("Your Score:", player_score)
    print("Computer Score:", computer_score)
    print("Draws:", draws)
    print("================================")

# Final result
print("\n========== FINAL RESULT ==========")

print("Your Total Wins:", player_score)
print("Computer Wins:", computer_score)
print("Total Draws:", draws)

if player_score > computer_score:
    print("\nYou are the Overall Winner!")

elif computer_score > player_score:
    print("\nComputer is the Overall Winner!")

else:
    print("\nThe Game Ends in a Tie!")

print("\nThank you for playing!")
print("===================================")
