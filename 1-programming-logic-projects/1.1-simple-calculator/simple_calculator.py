# Simple calculator definition
def simple_calculator(n1: float, n2: float, operation: int):
    """Simple calculator

    Args:
        n1 (float): First number
        n2 (float): Second number
        operation (int): Selected operation
            1 - addition
            2 - subtraction
            3 - multiplication
            4 - division.

    Raises:
        Exception: Invalid operation

    Returns:
        float: Result of the operation
    """

    # Addition
    if operation == 1:
        return n1 + n2
    # Subtraction
    elif operation == 2:
        return n1 - n2
    # Multiplication
    elif operation == 3:
        return n1 * n2
    # Division
    elif operation == 4:
        return n1 / n2
    # Raise invalid operation exception
    else:
        raise Exception("Invalid operation")


def main():
    """Execute Simple Calculator"""
    try:
        # Receive values
        n1 = float(input("Insert the 1º number: "))
        operation = int(
            input(
                """\nOperations: \n1 - addition\n2 - subtraction\n3 - multiplication\n4 - division\n\nSelected operation: """
            )
        )
        n2 = float(input("Insert the 2º number: "))

        # Get the result
        result = simple_calculator(n1=n1, n2=n2, operation=operation)

        # Show the result
        print("\nResult:", result)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    # Run the program
    main()

    # Re-run looping
    while input("\nDo you wan't to run again? (y/n)").lower() in ["y", "yes"]:
        main()
