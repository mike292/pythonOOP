import random

# r1 = random.randrange(10)  # 0 to 9 does not use the last number
# r2 = random.randrange(-5, 10)  # -5 to 9
# print(r2)
# r3 = random.randint(-2, 10)  # uses the last number / must have 2 arguments

range = input("Type a number: ")

if range.isdigit():
    range = int(range)
    if range < 1:
        print("Type a number greater than.")
        quit()
else:
    print("Please type a number.")
    quit()

random_number = random.randint(0, range)
guesses = 0
# input_number = input("What is the number? ")
# input_number = int(input_number)

# if input_number == random_number:
#     print("You're correct!")
# else:
#     print("Incorrect! The number is: " + str(random_number))


while True:
    input_number = input("What is the number? ")
    # input_number = int(input_number)

    if input_number.isdigit():
        input_number = int(input_number)
    else:
        print("Please type a numbers.")
        continue

    guesses += 1
    if input_number == random_number:
        print("You got it!")
        break
    else:
        if input_number > random_number:
            print("You are above the number.")
        else:
            print("You are below the number.")

print("You got it in", guesses, "guesses")
