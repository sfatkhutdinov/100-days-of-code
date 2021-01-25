import random
from art import logo

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")
winning_number = random.randint(1, 100)
attempts = 10
if difficulty == "hard":
    attempts = 5
game_over = False
while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > winning_number:
        print("Too high")
        attempts -= 1
    elif guess < winning_number:
        print("Too low")
        attempts -= 1
    else:
        attempts -= attempts
        print(f"You got it! The number was {winning_number}")
        print("You won!")
        game_over = True
    if attempts == 0:
        print("You lost")
        game_over = True
