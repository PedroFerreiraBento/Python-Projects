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


# Sort numbers
def sort_numbers(sort_method: int, list_of_numbers: str) -> list:
    """Sort a list of numbers in ascending or descending order

    Args:
        sort_method (int): Sort method
            1 - Ascending
            2 - Descending
        list_of_numbers (str): Comma separated numbers

    Raises:
        ValueError: Invalid list of numbers received

    Returns:
        list: Sorted numbers
    """

    try:
        # Convert string to list of numbers
        list_of_numbers = list(map(float, list_of_numbers.split(sep=",")))
    except ValueError:
        raise ValueError("Invalid list of numbers received!")

    # Sorted numbers
    list_of_numbers.sort()

    # Descending sort
    if sort_method == 2:
        list_of_numbers.reverse()

    # Return the sorted list
    return list_of_numbers


def main() -> None:
    """Main program"""
    # Reset the terminal
    clear_terminal()

    while True:

        try:
            # Select sort method
            sort_method = int(
                input(
                    "Sorts:\n1 - Ascending\n2 - Descending\n\nSelect the sort method: "
                )
            )
            # Validate sort method
            if sort_method not in [1, 2]:
                raise ValueError("Invalid sort method selected!")

            # Get the list of numbers
            list_of_numbers = input(
                "\nInsert a list of numbers(Example: 20, 31, 44, 32): "
            )

            # Sort the numbers
            sorted_numbers = sort_numbers(
                sort_method=sort_method,
                list_of_numbers=list_of_numbers,
            )

            # Show the results
            print(f"\nResult: {sorted_numbers}")

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
