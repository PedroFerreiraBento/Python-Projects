# To detect the Operational System
import platform

# To clear the terminal
import os

# To generate random passwords
import random

# Clear the terminal
def clear_terminal() -> None:
    """Clear the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


# Get password parameters
def get_pwd_params() -> dict:
    """Get parameter to generate a password

    Raises:
        ValueError: Invalid length size
        ValueError: Invalid numbers option
        ValueError: Invalid lowercase letters option
        ValueError: Invalid uppercase letters option
        ValueError: Invalid symbol option

    Returns:
        dict: Parameter to password generation
    """
    while True:
        try:
            # Length of the password
            length = int(input("Insert the length of password: "))
            if length <= 0:
                raise ValueError("Invalid length size!")

            # Include numbers
            clear_terminal()
            numbers = int(
                input("Include numbers: \n\n0 - No\n1 - Yes\n\nSelect the option: ")
            )
            if numbers not in [0, 1]:
                raise ValueError("Invalid numbers option!")

            # Include lowercase letters
            clear_terminal()
            lowercase_letters = int(
                input(
                    "Include lowercase letters: \n\n0 - No\n1 - Yes\n\nSelect the option: "
                )
            )
            if lowercase_letters not in [0, 1]:
                raise ValueError("Invalid lowercase letters option!")

            # Include uppercase letters
            clear_terminal()
            uppercase_letters = int(
                input(
                    "Include uppercase letters: \n\n0 - No\n1 - Yes\n\nSelect the option: "
                )
            )
            if uppercase_letters not in [0, 1]:
                raise ValueError("Invalid uppercase letters option!")

            # Include symbols
            clear_terminal()
            symbols = int(
                input("Include symbols: \n\n0 - No\n1 - Yes\n\nSelect the option: ")
            )
            if symbols not in [0, 1]:
                raise ValueError("Invalid symbols option!")

            # Allow repeated characters
            clear_terminal()
            repeated = int(
                input(
                    "Allow repeated characters: \n\n0 - No\n1 - Yes\n\nSelect the option: "
                )
            )
            if repeated not in [0, 1]:
                raise ValueError("Invalid allow repeated option!")
            clear_terminal()

            # Return parameters
            return {
                "length": length,
                "numbers": bool(numbers),
                "lowercase_letters": bool(lowercase_letters),
                "uppercase_letters": bool(uppercase_letters),
                "symbols": bool(symbols),
                "repeated": bool(repeated),
            }

        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("An unexpected error occurred")
            print(e)


# Get count of each type
def get_types_count(
    length: int,
    repeated: bool,
    count_types: int,
    include_numbers: bool,
    include_lowercase_letters: bool,
    include_uppercase_letters: bool,
    include_symbols: bool,
) -> dict:
    """Get count types

    Args:
        length (int): Length of the password
        repeated (bool): Allow repeated characters
        count_types (int): Number of types
        include_numbers (bool): Include numbers
        include_lowercase_letters (bool): Include lowercase letters
        include_uppercase_letters (bool): Include uppercase letters
        include_symbols (bool): Include symbols characters

    Returns:
        dict: Number of characters from each type
    """

    rest = 0

    # Numbers
    if include_numbers:
        count_numbers = length // count_types

        if length % count_types == 1:
            count_numbers += 1

        if not repeated and count_numbers > 10:
            rest += count_numbers - 10
            count_numbers = 10
    else:
        count_numbers = 0

    # Lowercase characters
    if include_lowercase_letters:
        count_lower = length // count_types

        if length % count_types == 2:
            count_lower += 1

        if not repeated and count_lower > 26:
            rest += count_lower - 26
            count_lower = 26
    else:
        count_lower = 0

    # Uppercase characters
    if include_uppercase_letters:
        count_upper = length // count_types

        if length % count_types == 3:
            count_upper += 1

        if not repeated and count_upper > 26:
            rest += count_upper - 26
            count_upper = 26
    else:
        count_upper = 0

    # Symbols
    if include_symbols:
        count_symbols = length // count_types

        if not repeated and count_symbols > 26:
            rest += count_symbols - 26
            count_symbols = 26
    else:
        count_symbols = 0

    # Fill no repeated
    if rest > 0:
        if count_numbers < 10:
            missing_numbers = 10 - count_numbers
            count_fill = missing_numbers if rest - missing_numbers >= 0 else rest
            count_numbers += count_fill
            rest -= count_fill
        if count_lower < 26:
            missing_lower = 26 - count_lower
            count_fill = missing_lower if rest - missing_lower >= 0 else rest
            count_lower += count_fill
            rest -= count_fill
        if count_upper < 26:
            missing_upper = 26 - count_upper
            count_fill = missing_upper if rest - missing_upper >= 0 else rest
            count_upper += count_fill
            rest -= count_fill
        if count_symbols < 33:
            missing_symcount_symbols = 33 - count_symbols
            count_fill = (
                missing_symcount_symbols
                if rest - missing_symcount_symbols >= 0
                else rest
            )
            count_symbols += count_fill
            rest -= count_fill

    return {
        "numbers": count_numbers,
        "lower": count_lower,
        "upper": count_upper,
        "symbols": count_symbols,
    }


# Generate password
def generate_password(
    length: int,
    include_numbers: bool,
    include_lowercase_letters: bool,
    include_uppercase_letters: bool,
    include_symbols: bool,
    repeated: bool,
) -> str:
    """Generate password

    Args:
        length (int): Length of the password
        include_numbers (bool): Include numbers
        include_lowercase_letters (bool): Include lowercase letters
        include_uppercase_letters (bool): Include uppercase letters
        include_symbols (bool): Include symbols characters
        repeated (bool): Allow repeated characters

    Raises:
        ValueError: No character type selected
        ValueError: Many types selected
        ValueError: Not enough available characters

    Returns:
        str: Generated password
    """

    characters = {
        "numbers": list("0123456789"),
        "lower": list("abcdefghijklmnopqrstuvwxyz"),
        "upper": list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        "symbols": list("`~!@#$%^&*()-_=+[]\{}|;':\",./<> ?"),
    }

    count_types = 0
    max_length = 0

    # Count types of characters the password will include
    if include_numbers:
        count_types += 1
        max_length += 10
    if include_lowercase_letters:
        count_types += 1
        max_length += 26
    if include_uppercase_letters:
        count_types += 1
        max_length += 26
    if include_symbols:
        count_types += 1
        max_length += 33

    # No type selected
    if count_types == 0:
        raise ValueError(
            "No character type selected: Plese select at least 1 character type!"
        )

    # More types than password charactes
    if count_types > length:
        raise ValueError(
            f"Many types selected: You select {count_types} types but the length of password is {length}"
        )

    # Length higher than available characters
    if not repeated and length > max_length:
        raise ValueError(
            f"Not enough available characters: For the selected parameters there are {max_length} available character but the requested lenght is {length}"
        )

    # Get how many character each type will have
    types_counts = get_types_count(
        count_types=count_types,
        include_numbers=include_numbers,
        include_lowercase_letters=include_lowercase_letters,
        include_uppercase_letters=include_uppercase_letters,
        include_symbols=include_symbols,
        length=length,
        repeated=repeated,
    )

    password = ""

    for index in range(length):
        available_types = [
            char_type for char_type, count in types_counts.items() if count != 0
        ]
        selected_type = random.choice(available_types)
        selected_character = random.choice(characters[selected_type])

        password += selected_character

        if not repeated:
            characters[selected_type].remove(selected_character)
            types_counts[selected_type] -= 1

    return password


def main() -> None:
    """Main program"""
    # Reset the terminal
    clear_terminal()

    while True:

        try:
            # Get password parameters
            parameters = get_pwd_params()

            # Generate password
            password = generate_password(
                length=parameters["length"],
                include_numbers=parameters["numbers"],
                include_lowercase_letters=parameters["lowercase_letters"],
                include_uppercase_letters=parameters["uppercase_letters"],
                include_symbols=parameters["symbols"],
                repeated=parameters["repeated"],
            )

            # Display the password
            print(f"\nPassword: {password}")

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
