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


# Palindrome Checker
def palindrome_checker(text: str) -> bool:
    """Check if a word, phrase, number, or other sequence of characters reads the same forward and backward.

    Args:
        text (str): Text that will be checked

    Returns:
        bool: Is palindrome or not
    """

    text = text.lower()

    return text == text[::-1]


def main() -> None:
    """Main program"""
    # Reset the terminal
    clear_terminal()

    while True:

        try:
            # Get text
            text = input("Insert the text: ")

            # Check if is palindrome
            is_palindrome = palindrome_checker(text=text)

            # Display the password
            print(f"\nPalindrome: {is_palindrome}")

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
