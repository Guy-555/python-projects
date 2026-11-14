import random

def game_set(difficulty):
    if difficulty == 'hard':
        return 5
    elif difficulty == 'easy':
        return 10
    else:
        print("Invalid.")
        return 10

def game_process(guess, number):
    if number == guess:
        print("Correct.")
        return 0
    elif guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    if attempts == 1:
        print(f"You've run out of guesses. It was {number}.")
    else:
        print("Guess again.")
    return attempts - 1

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy or 'hard': ").lower()
attempts = 0
attempts = game_set(difficulty)

number = random.randint(1, 100)

while attempts:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = game_process(guess, number)