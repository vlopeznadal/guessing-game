"""A number-guessing game."""
import random

score = 0
# Put your code here    
def get_name():
    print("Hi, what's your name? ")
    name = input("Your name: ")
    return name

# create a function that would handle the guessing 
def guessing_game (name, score):
    print(f"{name}, I'm thinking of a number between 1 and 100.")
    print("Try to guess my number.")
    random_num = random.randint(1, 100)
    guess = int(input("enter your guess: "))

    counter = 0
    
    while guess != random_num:
        if guess < 1 or guess > 100:
            print('Choose a valid number between 1 and 100.')
        elif guess < random_num:
            print('Your guess is too low: try again.')
        else:
            print('Your guess is too high. Try again.')
        counter += 1
        guess = int(input('What is your new guess? '))
    
    if score > counter:
        score = counter
        
    print(f"Good job {name}! You found my number in {counter} tries! You're best score is {score}")

    answer = input("Would you like to play again? Enter y for yes or n for no.")

    if answer == 'y':
        guessing_game(name, score)
    else:
        print("Great job! See you later!")

player = get_name()
guessing_game(player, score)