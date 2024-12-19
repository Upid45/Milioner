import time
import random
import sys

win_points = 0
for number in range(10):
    if win_points == 3:
        break
    player = int(input("""Pick the item:
                1. Paper
                2. Rock
                3. Scissors
                """))
    if player == 1:
        print("Your item - Paper")
    elif player == 2:
        print("Your item - Rock")
    elif player == 3:
        print("Your item - Scissors")
    else:
        print("Unbelievable, you chose the Paper")
    comp = random.randrange(1, 3)
    if comp == 1:
        print("Enemy item - Paper")
    elif comp == 2:
        print("Enemy item - Rock")
    elif comp == 3:
        print("Enemy item - Scissors")
    else:
        print("HOW THIS IS HAPPEND?")
        sys.exit(0)
    if player == comp:
        print("Draw!")
        print(f"You win {win_points} times")
    elif player == 1 and comp == 2 or player == 2 and comp == 3 or player == 3 and comp == 1:
        print("You win!")
        win_points += 1
        print(f"You win {win_points} times")
    else:
        print("You lose!")
        print(f"You win {win_points} times")