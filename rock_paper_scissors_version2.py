import random

player_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    player_pick = input("Choose rock/paper/scissors or q for quit: ").lower()

    if player_pick == "q":
        break

    if player_pick not in options:
        print("Please choose rock, paper or scissors.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    # print(computer_pick)

    if player_pick == "rock" and computer_pick == "scissors":
        player_score += 1
        print("Computer chose", computer_pick, "You won!")
    elif player_pick == "paper" and computer_pick == "rock":
        player_score += 1
        print("Computer chose", computer_pick, "You won!")
    elif player_pick == "scissors" and computer_pick == "paper":
        player_score += 1
        print("Computer chose", computer_pick, "You won!")
    else:
        if player_pick == computer_pick:
            print("It's a tie.")
            continue
        computer_score += 1
        print("Computer chose", computer_pick, "You lost!")

print("You're score is", player_score)
print("Computer's score is", computer_score)
print("Good bye.")
