# To detect the Operational System
import platform

# To clear the terminal
import os


def clear_terminal():
    """Clear the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


def simple_calculator(n1: float, n2: float, operation: int) -> float:
    """Calculator

    Args:
        n1 (float): first number
        n2 (float): second number
        operation (int): selected operation

    Raises:
        ValueError: Division by zero
        ValueError: Invalid operation

    Returns:
        float: result
    """
    if operation == 1:
        return n1 + n2
    elif operation == 2:
        return n1 - n2
    elif operation == 3:
        return n1 * n2
    elif operation == 4:
        # Division by zero
        if n2 == 0:
            raise ValueError("Cannot divide by zero")
        return n1 / n2
    else:
        raise ValueError("Invalid operation")


def main():
    """Main program"""
    # Reset the terminal
    clear_terminal()
    while True:
        try:

            # Receive the inputs
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))
            operation = int(
                input("Select an operation (1=add, 2=subtract, 3=multiply, 4=divide): ")
            )

            # Compute the result
            result = simple_calculator(n1, n2, operation)

            # Show the result
            print(f"\nResult: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print("An unexpected error occurred")
            print(e)
        else:
            # Re-run looping
            if input("\nDo you want to run again? (y/n): ").lower() not in ["y", "yes"]:
                break
            # Reset the terminal
            clear_terminal()


if __name__ == "__main__":
    main()
