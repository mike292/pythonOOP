print("Welcome to my computer quiz!")

playing = input("Do you want to play(yes/no)? ").lower()
print(playing)
score = 0

if playing != "yes":
    print("Quiting game!")
    quit()


print("Let's start playing!")

answer = input("What color is the sky?").lower()
if answer == "blue":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What color is a tree?").lower()
if answer == "green":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What color is a rock?").lower()
if answer == "grey":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What color is blood?").lower()
if answer == "red":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

print("You got " + str(score) + " correct answers!")
