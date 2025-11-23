# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 12:05:38 2025

@author: avgan
"""
# import random

# def play_guessing_game():
#     """
#     A simple number guessing game.
#     The user tries to guess a random number between 1 and 100.
#     """
#     # Generate a random number between 1 and 100 (inclusive)
#     secret_number = random.randint(1, 100)
#     guess = None
#     attempts = 0

#     print("Welcome to the Number Guessing Game!")
#     print("I have picked a number between 1 and 100. Try to guess it.")

#     # Loop until the user guesses the correct number
#     while guess != secret_number:
#         try:
#             # Get user input and convert it to an integer
#             guess_str = input("Enter your guess: ")
#             guess = int(guess_str)
#             attempts += 1

#             # Provide feedback on the guess
#             if guess < secret_number:
#                 print("Too low, try a higher number.\n")
#             elif guess > secret_number:
#                 print("Too high, try a lower number.\n")
#             else:
#                 # Correct guess, break the loop
#                 print(f"Congratulations! You guessed the number {secret_number} correctly!")
#                 print(f"It took you {attempts} attempts.\n")

#         except ValueError:
#             # Handle non-integer input gracefully
#             print("Invalid input. Please enter a valid integer.\n")

# if __name__ == "__main__":
#     play_guessing_game()

import random 

"""
A simple number guessing game.
he user tries to guess a random number between 1 and 100.
"""

number = random.randint(1, 100)
guess = 0
attempts = 0

print("Welcome To Number Guessing Game")
print("A Random Number is picked. Try and Guess!")

while guess != number:
    guess = int(input("Enter the guessed number: "))
    attempts += 1
    if guess < number :
        print("Guess is low! Try Higher")
    elif guess > number :
        print("Guess is high! Try Lower")
    else:
        print(f"You guessed the number {number} correctly. You Won!")
        print(f"It took you {attempts} attempts.\n")
        
    

        