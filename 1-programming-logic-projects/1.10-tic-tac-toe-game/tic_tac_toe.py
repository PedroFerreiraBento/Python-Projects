# To detect the Operational System
import platform

# To clear the terminal
import os

# To get the shape of the board
import numpy

# Clear the terminal
def clear_terminal() -> None:
    """Clear the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


# Build the board
def build_board(rows: int = 3, columns: int = 3) -> list:
    """Build an empty board

    Args:
        rows (int, optional): Board rows count. Defaults to 3.
        columns (int, optional): Board columns count. Defaults to 3.

    Returns:
        list: Empty board
    """

    return [[""] * columns for row in range(rows)]


# Int to Letters Count
def convert_to_letters_count(num: int) -> str:
    """Convert a number to a letters count.

    Args:
        num (int): Decimal count

    Examples:
        >>> convert_to_letters_count(1)
        'A'
        >>> convert_to_letters_count(5)
        'E'
        >>> convert_to_letters_count(27)
        'AA'
        >>> convert_to_letters_count(28)
        'AB'

    Raises:
        ValueError: Number below zero

    Returns:
        str: Letter value
    """

    if num <= 0:
        raise ValueError("Number below zero")

    # Create a mapping of numbers to letters
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = {}
    for i in range(1, 27):
        mapping[i] = letters[i - 1]

    result = ""
    while num > 0:
        num, remainder = divmod(num - 1, 26)
        result = mapping[remainder + 1] + result

    return result


# Letter count to int
def letter_count_to_int(text: str) -> int:
    """Convert letter count to int

    Args:
        text (str): Letter count value

    Returns:
        int: Integer result
    """

    result = 0
    for char in text:
        result = result * 26 + (ord(char) - ord("A") + 1)

    return result


# Display board
def display_board(board: list) -> None:
    """Display a given board

    Args:
        board (list): 3x3 Board
    """

    rows, columns = numpy.shape(board)

    h_spaces = len(str(columns)) + 2
    v_spaces = (rows // 26) + 3

    # Display first row
    print(
        f"|{'':^{v_spaces}}|"
        + "|".join([f"{column:^{h_spaces}}" for column in range(1, columns + 1)])
        + "|"
    )

    # Display game rows
    for row in range(1, rows + 1):
        print(
            f"|{convert_to_letters_count(row):^{v_spaces}}|"
            + "|".join([f"{position:^{h_spaces}}" for position in board[row - 1]])
            + "|"
        )


# Update board
def update_board(board: list, move: str, player: int) -> list:
    """Update the board with a new move

    Args:
        board (list): Game board
        move (str): Row and column position
        player (int): Player

    Raises:
        ValueError: Move not in the board scope
        ValueError: Position is not empty
        ValueError: Invalid player

    Returns:
        list: Updated board
    """

    move = move.upper()

    # Check board scope
    if len(move) != 2 or not move[0].isalpha() or not move[1].isdigit():
        raise ValueError("Move not in the board scope")

    # Check empty position
    if board[letter_count_to_int(move[0]) - 1][int(move[1]) - 1] != "":
        raise ValueError("Position is not empty")

    # Check player
    if player not in [1, 2]:
        raise ValueError("Invalid player")

    # Fill position
    board[letter_count_to_int(move[0]) - 1][int(move[1]) - 1] = (
        "X" if player == 1 else "O"
    )

    return board


# Check if the game ended
def check_end_game(board: list, player: int) -> bool:
    """Check if the game ended

    Args:
        board (list): Board game
        player (int): Player

    Raises:
        ValueError: Invalid player

    Returns:
        bool: Ended or not
    """

    # Player validation
    if player not in [1, 2]:
        raise ValueError("Invalid player")

    # Check horizontal
    horizontal_check = True in [len(set(row)) == 1 and bool(row[0]) for row in board]

    # Check vertical
    vertical_check = False
    for column_index in range(len(board[0])):
        column = [row[column_index] for row in board]
        if len(set(column)) == 1 and bool(column[0]):
            vertical_check = True
            break

    # Diagonal check
    diagonal_1 = len(set([board[0][0], board[1][1], board[2][2]])) == 1 and bool(
        board[0][0]
    )
    diagonal_2 = len(set([board[0][2], board[1][1], board[2][0]])) == 1 and bool(
        board[0][2]
    )
    diagonal_check = diagonal_1 or diagonal_2

    ended_game = horizontal_check or vertical_check or diagonal_check

    if ended_game:
        clear_terminal()
        display_board(board=board)
        print(f"\nPlayer {player} Win! Congratulations!")
    else:
        # Check tie
        if True not in ["" in row for row in board]:
            clear_terminal()
            display_board(board=board)
            print("\nGame tied! Better luck next time!")
            ended_game = True

    # Check if game ended
    return ended_game


# Tic Tac Toe Game
def tic_tac_toe_game() -> None:
    """Play a Tic Tac Toe game"""

    board = build_board(rows=3, columns=3)
    end_game = False

    while end_game == False:

        # Display board
        clear_terminal()
        display_board(board)

        # Wait for player 1
        while True:
            try:
                print("\nPlayer 1 Turn!")
                player_1_move = input("Select a place (Ex: B2): ")
                board = update_board(board, player_1_move, 1)
                if check_end_game(board, 1):
                    end_game = True
                break
            except ValueError as e:
                print(f"Error: {e}")

        # Break if game is ended
        if end_game:
            break

        # Display board
        clear_terminal()
        display_board(board)

        # Wait for player 2
        while True:
            try:
                print("\nPlayer 2 Turn!")
                player_2_move = input("Select a place (Ex: B2): ")
                board = update_board(board, player_2_move, 2)
                if check_end_game(board, 2):
                    end_game = True
                break
            except ValueError as e:
                print(f"Error: {e}")


def main() -> None:
    """Main program"""
    # Reset the terminal
    clear_terminal()

    while True:

        try:
            tic_tac_toe_game()

            # Re-run looping
            if input("\nDo you want to run again? (y/n): ").lower() not in ["y", "yes"]:
                # Reset the terminal
                break

            # Reset the terminal
            clear_terminal()

        except Exception as e:
            print("\nAn unexpected error occurred")
            print(e)
            break


if __name__ == "__main__":
    # Run the program
    main()
