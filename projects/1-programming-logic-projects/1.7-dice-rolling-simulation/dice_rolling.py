# To detect the Operational System
import platform

# To clear the terminal
import os

# To roll the dices
import random

# Clear the terminal
def clear_terminal() -> None:
    """Clear the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


# Roll dices
def roll_dices(dices: int, sides: int, rolls: int) -> list:
    """Roll dices

    Args:
        dices (int): Number of dices
        sides (int): Number of sides
        rolls (int): Number of rolls

    """

    # Just for break line on results display
    print()

    # Roll and display results
    for roll in range(1, rolls + 1):
        # Store the roll results
        results = []

        # Roll each dice
        for dice in range(dices):
            results.append(random.randint(1, sides))

        # Display roll results
        print(f"Results of roll number {roll}: {results}")


def main() -> None:
    """Main program"""
    # Reset the terminal
    clear_terminal()

    while True:

        try:
            # Number of dices
            dices = int(input("Insert the number of dices: "))

            # Sides of dices
            sides = int(input("Insert the number of sides: "))

            # Number of dices
            rolls = int(input("Insert the number of rolls: "))

            # Sort the numbers
            sorted_numbers = roll_dices(
                dices=dices,
                sides=sides,
                rolls=rolls,
            )

            # Re-run looping
            if input("\nDo you want to run again? (y/n): ").lower() not in ["y", "yes"]:
                # Reset the terminal
                break

            # Reset the terminal
            clear_terminal()

        except ValueError as e:
            print(f"\nError: {e}")

        except Exception as e:
            print("\nAn unexpected error occurred")
            print(e)


if __name__ == "__main__":
    # Run the program
    main()
