"""Task 2: Number Guessing Game (with attempt counter bonus)"""
import random


def play():
    secret = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            break


def main():
    print("=== Number Guessing Game ===")
    while True:
        play()
        if input("Play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()