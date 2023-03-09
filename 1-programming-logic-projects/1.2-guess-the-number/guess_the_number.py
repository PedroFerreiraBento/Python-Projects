# Guess the number definition
import random


def main():
    """Guess the number"""
    try:
        # Get a random target
        target = random.randint(1, 100)

        while True:
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

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    # Run the program
    main()

    # Re-run looping
    while input("\nDo you wan't to run again? (y/n)").lower() in ["y", "yes"]:
        main()
