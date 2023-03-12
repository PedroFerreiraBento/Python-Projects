# To detect the Operational System
import platform

# To clear the terminal
import os

# Clear the terminal
def clear_terminal() -> None:
    """Clear the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


# Get the largest number
def largest_number(numbers: str) -> float:
    """Find the largest number

    Args:
        numbers (str): List of numbers separated by comma

    Returns:
        float: largest number
    """

    list_of_numbers = list(map(float, numbers.split(sep=",")))

    return max(list_of_numbers)


def main() -> None:
    """Main program"""
    # Reset the terminal
    clear_terminal()
    while True:

        try:
            # Get the numbers
            numbers = input("Insert a list of numbers(Example: 20, 31, 44, 32): ")

            # Find the largest number
            largest = largest_number(numbers)

            # Show the results
            print(f"\nResult: {largest}")

            # Re-run looping
            if input("\nDo you want to run again? (y/n): ").lower() not in ["y", "yes"]:
                # Reset the terminal
                break

            # Reset the terminal
            clear_terminal()

        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print("An unexpected error occurred")
            print(e)


if __name__ == "__main__":
    # Run the program
    main()
