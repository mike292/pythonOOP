import random

user_score = 0
computer_score = 0

print("Let's play.")

while True:

    if user_score >= 3:
        print("You have won!")
        break
    elif computer_score >= 3:
        print("Game over!")
        break

    player = input("Rock, Paper, Scissors? ").lower()

    if player == "rock" or player == "paper" or player == "scissors":
        random_number = random.randint(1, 3)
        computer = ""
        if random_number == 1:
            computer = "rock"
        elif random_number == 2:
            computer = "paper"
        else:
            computer = "scissors"

        if player == "rock":
            if computer == "rock":
                print("tie")
                continue
            elif computer == "paper":
                print("Computer is scissors, you lose!")
                computer_score += 1
                continue
            elif computer == "scissors":
                print("Computer is scissors, you win!")
                user_score += 1
        elif player == "paper":
            if computer == "rock":
                print("Computer is rock, you win!")
                user_score += 1
                continue
            elif computer == "paper":
                print("Tie")
                continue
            elif computer == "scissors":
                print("Computer is scissors, you lose!")
                computer_score += 1
                continue
        elif player == "scissors":
            if computer == "rock":
                print("Computer is rock, you lose!")
                computer_score += 1
                continue
            elif computer == "paper":
                print("Computer is scissors, you win!")
                user_score += 1
                continue
            elif computer == "scissors":
                print("Tie")
                continue

    else:
        print("Please type rock, paper and scissors only.")
