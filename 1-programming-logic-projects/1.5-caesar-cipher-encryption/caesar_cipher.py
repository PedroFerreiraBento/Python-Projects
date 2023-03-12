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


# Caesar Cipher
def caesar_cipher(convertion: int, shifts: int, message: str) -> str:
    """Encrypt or Decrypt using caesar cipher

    Args:
        convertion (int): Convertion type
            1 - Encrypt
            2 - Decrypt
        shifts (int): Number of backshifts
        message (str): The message

    Raises:
        UnicodeTranslateError: Message has some char that are not in the english alphabet

    Returns:
        str: Encrypted or Decrypted text
    """

    # Lower the message to facilitate the convertion
    message = message.lower()

    # Encrypt or Decrypt change shifts
    shifts = shifts if convertion == 1 else shifts * -1

    # Validate message chars
    for char in message:
        if char != " " and (ord(char) < 97 or ord(char) > 122):  # 97 = "a", 122 = "z"
            raise UnicodeTranslateError(
                "Invalid char in message: Please use the english alphabet"
            )

    # Chipher a word
    chipher = lambda word: "".join(
        (chr((ord(char) - 97 - shifts) % 26 + 97) for char in word)
    )

    # Chipher the paragraph
    return " ".join((chipher(word) for word in message.split(sep=" ")))


def main() -> None:
    """Main program"""
    # Reset the terminal
    clear_terminal()

    while True:

        try:
            # Select convertion type
            convertion = int(
                input(
                    "Convertions:\n1 - Encrypt\n2 - Decrypt\n\nSelect the convertion: "
                )
            )
            if convertion not in [1, 2]:
                raise ValueError("Invalid convertion type!")

            # Get the shifts
            shifts = int(input("Insert the shifts: "))

            # Get the message
            message = input("\nInsert the message: ")

            # Cipher the message
            cipher = caesar_cipher(
                convertion=convertion,
                shifts=shifts,
                message=message,
            )

            # Show the results
            print(f"\nResult: {cipher}")

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
