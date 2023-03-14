# To detect the Operational System
import platform

# To clear the terminal
import os

# To get the shape of the board
import numpy

# To place the mines
import random

# Clear the terminal
def clear_terminal() -> None:
    """Clear the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


# Build the board
def build_board(rows: int = 3, columns: int = 3, empty_value="") -> list:
    """Build an empty board

    Args:
        rows (int, optional): Board rows count. Defaults to 3.
        columns (int, optional): Board columns count. Defaults to 3.

    Returns:
        list: Empty board
    """

    return [[empty_value] * columns for row in range(rows)]


# Place mines
def place_mines(hidden_board: list, mines: list) -> list:
    """Place mines and add hints to environment

    Args:
        hidden_board (list): Board that will have the mines
        mines (list): List of coordenates

    Returns:
        list: board with mine placed
    """

    for mine in mines:
        row = mine[0]
        column = mine[1]

        # Place mine
        hidden_board[row][column] = "O"

        # Add 1 to environment
        add_1 = lambda place: 1 if place is "" else place + 1

        # Up add
        if row - 1 >= 0 and hidden_board[row - 1][column] != "O":
            hidden_board[row - 1][column] = add_1(hidden_board[row - 1][column])
        # Down add
        if row + 1 < len(hidden_board) and hidden_board[row + 1][column] != "O":
            hidden_board[row + 1][column] = add_1(hidden_board[row + 1][column])
        # Left add
        if column - 1 >= 0 and hidden_board[row][column - 1] != "O":
            hidden_board[row][column - 1] = add_1(hidden_board[row][column - 1])
        # Right add
        if column + 1 < len(hidden_board) and hidden_board[row][column + 1] != "O":
            hidden_board[row][column + 1] = add_1(hidden_board[row][column + 1])

        # Up Left add
        if (
            row - 1 >= 0
            and column - 1 >= 0
            and hidden_board[row - 1][column - 1] != "O"
        ):
            hidden_board[row - 1][column - 1] = add_1(hidden_board[row - 1][column - 1])
        # Up Right add
        if (
            row - 1 >= 0
            and column + 1 < len(hidden_board)
            and hidden_board[row - 1][column + 1] != "O"
        ):
            hidden_board[row - 1][column + 1] = add_1(hidden_board[row - 1][column + 1])
        # Down Left add
        if (
            row + 1 < len(hidden_board)
            and column - 1 >= 0
            and hidden_board[row + 1][column - 1] != "O"
        ):
            hidden_board[row + 1][column - 1] = add_1(hidden_board[row + 1][column - 1])
        # Down Right add
        if (
            row + 1 < len(hidden_board)
            and column + 1 < len(hidden_board)
            and hidden_board[row + 1][column + 1] != "O"
        ):
            hidden_board[row + 1][column + 1] = add_1(hidden_board[row + 1][column + 1])

    return hidden_board


# Reveal a place
def reveal_place(game_board: list, hidden_mines: list, row: int, column: int) -> list:
    """Reveal a place in the board

    Args:
        game_board (list): Game board
        hidden_mines (list): Board with mines
        row (int): row
        column (int): column

    Returns:
        list: Board with place revealed
    """

    if hidden_mines[row][column] == "O":
        game_board[row][column] = "X"
    elif hidden_mines[row][column] != "":
        game_board[row][column] = hidden_mines[row][column]
    else:
        game_board[row][column] = "-"

        # Up
        if row - 1 >= 0 and game_board[row - 1][column] is "":
            game_board = reveal_place(
                game_board=game_board,
                hidden_mines=hidden_mines,
                row=row - 1,
                column=column,
            )
        # Down
        if row + 1 < len(hidden_mines) and game_board[row + 1][column] is "":
            game_board = reveal_place(
                game_board=game_board,
                hidden_mines=hidden_mines,
                row=row + 1,
                column=column,
            )
        # Left
        if column - 1 >= 0 and game_board[row][column - 1] is "":
            game_board = reveal_place(
                game_board=game_board,
                hidden_mines=hidden_mines,
                row=row,
                column=column - 1,
            )
        # Right
        if column + 1 < len(hidden_mines) and game_board[row][column + 1] is "":
            game_board = reveal_place(
                game_board=game_board,
                hidden_mines=hidden_mines,
                row=row,
                column=column + 1,
            )

        # Up Left
        if row - 1 >= 0 and column - 1 >= 0 and game_board[row - 1][column - 1] is "":
            game_board = reveal_place(
                game_board=game_board,
                hidden_mines=hidden_mines,
                row=row - 1,
                column=column - 1,
            )
        # Up Right
        if (
            row - 1 >= 0
            and column + 1 < len(hidden_mines)
            and game_board[row - 1][column + 1] is ""
        ):
            game_board = reveal_place(
                game_board=game_board,
                hidden_mines=hidden_mines,
                row=row - 1,
                column=column + 1,
            )
        # Down Left
        if (
            row + 1 < len(hidden_mines)
            and column - 1 >= 0
            and game_board[row + 1][column - 1] is ""
        ):
            game_board = reveal_place(
                game_board=game_board,
                hidden_mines=hidden_mines,
                row=row + 1,
                column=column - 1,
            )
        # Down Right
        if (
            row + 1 < len(hidden_mines)
            and column + 1 < len(hidden_mines)
            and game_board[row + 1][column + 1] is ""
        ):
            game_board = reveal_place(
                game_board=game_board,
                hidden_mines=hidden_mines,
                row=row + 1,
                column=column + 1,
            )

    return game_board


# Build mines board
def build_mines(difficulty: int) -> list:
    """Build mines board

    Args:
        difficulty (int): Game difficulty

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        list: board with mines
    """

    # Define board size
    if difficulty == 1:
        board_size = 8
        mines_count = 7
    elif difficulty == 2:
        board_size = 14
        mines_count = 20
    else:
        board_size = 20
        mines_count = 50

    game_board = build_board(columns=board_size, rows=board_size)
    hidden_bombs = build_board(columns=board_size, rows=board_size)

    # Select mines positions
    mines = []
    for mine in range(mines_count):
        while True:
            row = random.randint(0, board_size - 1)
            column = random.randint(0, board_size - 1)

            if (row, column) not in mines:
                mines.append((row, column))
                break

    # Place mines
    hidden_bombs = place_mines(hidden_bombs, mines)

    return (hidden_bombs, game_board)


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
def update_board(game_board: list, hidden_mines: list, move: str) -> list:
    """Update the board with a new move

    Args:
        game_board (list): Game board
        hidden_mines (list): Mines board
        move (str): Row and column position

    Raises:
        ValueError: Move not in the board scope
        ValueError: Position is not empty

    Returns:
        list: Updated board
    """

    move = move.upper()

    columns_index = [index for index, char in enumerate(move) if char.isdigit()]

    # Check board scope
    if len(columns_index) == 0 or not move[0].isalpha():
        raise ValueError("Move not in the board scope")

    row = letter_count_to_int(move[: columns_index[0]]) - 1
    column = int(move[columns_index[0] :]) - 1

    # Check empty position
    if game_board[row][column] != "":
        raise ValueError("Position is not empty")

    # Reveal selected place
    game_board = reveal_place(
        game_board=game_board,
        hidden_mines=hidden_mines,
        row=row,
        column=column,
    )

    return game_board


# Check if the game ended
def check_end_game(game_board: list, hidden_mines: list) -> bool:
    """Check if the game ended

    Args:
        game_board (list): Game board
        hidden_mines (list): Board with mines

    Returns:
        bool: Ended or not
    """

    # Exploded mines check
    check_exploded = bool(sum([row.count("X") for row in game_board]))

    # Lose game
    if check_exploded:

        for row in range(len(hidden_mines)):
            for column in range(len(hidden_mines[row])):
                if hidden_mines[row][column] == "O" and game_board[row][column] is "":
                    game_board[row][column] = "X"

        clear_terminal()
        display_board(board=game_board)
        print(f"\nYou Lose! Better luck next time!")

        return True

    # Find if there are any places left
    count_mines = sum([row.count("O") for row in hidden_mines])
    count_empty_places = sum([row.count("") for row in game_board])

    # Win game
    if count_empty_places == count_mines:
        for row in range(len(hidden_mines)):
            for column in range(len(hidden_mines[row])):
                if hidden_mines[row][column] == "O" and game_board[row][column] is "":
                    game_board[row][column] = "O"

        clear_terminal()
        display_board(board=game_board)
        print(f"\nYou WIN! Congratulations!")
        return True

    # Not ended game
    return False


# Minesweeper Game
def minesweeper() -> None:
    """Play a Minesweeper game"""

    # Get difficulty
    difficulty = int(
        input(
            "Difficulties:\n\n1 - Easy\n2 - Normal\n3 - Hard\n\nSelect the difficulty: "
        )
    )

    # Validate difficulty
    if difficulty not in [1, 2, 3]:
        raise ValueError("Invalid difficulty")

    hidden_mines, game_board = build_mines(difficulty=difficulty)

    end_game = False

    while end_game == False:

        # Display board
        clear_terminal()
        display_board(game_board)

        # Wait for player move
        while True:
            try:
                player_move = input("\nSelect a place (Ex: B2): ")
                game_board = update_board(game_board, hidden_mines, player_move)
                if check_end_game(game_board, hidden_mines):
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
            # Start the game
            minesweeper()

            # Re-run looping
            if input("\nDo you want to run again? (y/n): ").lower() not in ["y", "yes"]:
                # Reset the terminal
                break

            # Reset the terminal
            clear_terminal()

        except Exception as e:
            print("\nAn unexpected error occurred")
            print(e)
            raise e
            break


if __name__ == "__main__":
    # Run the program
    main()
