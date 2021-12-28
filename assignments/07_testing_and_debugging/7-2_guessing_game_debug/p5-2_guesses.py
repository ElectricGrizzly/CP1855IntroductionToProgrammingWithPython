#!/usr/bin/env python3

import random

def display_title():
    print("Guess the number!")
    print()

def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    print("I'm thinking of a number from 1 to " + str(limit) + "\n")
    count = 0
    while True:
        guess = int(input("Your guess: "))
        count += 1  # all conditionals use count += 1, so moved it outside conditionals
                    # this is because provided sample output shows 7 tries with 7 input values and not 6
                    # the original only incremented when incorrect, so tries = # guesses - 1, not like the sample output
                    # where tries = # guesses
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        elif guess == number:
            print("You guessed it in " + str(count) + " tries.\n")
            return

def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        limit = get_limit()
        play_game(limit)
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

