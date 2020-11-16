import random

print("Number guessing game")

number = random.randint(1, 15)
chances = 5

print("Guess a number between 1 to 15.")
print("You have 5 chances")
print("")

while chances > 0:
    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("Congratulation YOU WON!!!")
        exit()

    elif guess < number:
        print("Your guess was lower than the actual number. Guess a number higher than", guess)
        print("You have", chances-1, "more chances")
        print("")


    else:
        print("Your guess was higher than the actual number. Guess a number lower than", guess)
        print("You have", chances-1, "more chances")
        print("")

    chances = chances - 1

if not chances > 0:
    print("YOU LOSE!!! The number is", number)
    exit()