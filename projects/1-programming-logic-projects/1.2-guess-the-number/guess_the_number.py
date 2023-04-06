# To detect the Operational System
import platform

# To clear the terminal
import os

# To select a random number
import random

# Clear the terminal
def clear_terminal() -> None:
    """Clear the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


# Guess number
def guess_number() -> None:
    """Guess the random number"""

    # Get a random target
    target = random.randint(1, 100)

    while True:
        try:
            # Receive value
            guess = float(input("Try to guess the number: "))

            # Compare target and guess
            if guess == target:
                print("\nCongratulation!!!")
                break
            if guess > target:
                print("The guess is to high!\n")
            if guess < target:
                print("The guess is to low!\n")
        except ValueError:
            print("Error: Please enter a number between 1 and 100.")


def main() -> None:
    """Main program"""
    while True:
        # Reset the terminal
        clear_terminal()

        # Guess the number
        guess_number()

        # Re-run looping
        if input("\nDo you want to run again? (y/n): ").lower() not in ["y", "yes"]:
            break


if __name__ == "__main__":
    # Run the program
    main()
