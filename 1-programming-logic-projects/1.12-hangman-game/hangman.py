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


# Get random word
def get_random_word(category: int) -> str:
    """Get random word based on category

    Args:
        category (int): Category of word.
            1 - Animals
            2 - Fruits
            3 - Colors

    Raises:
        ValueError: Invalid category

    Returns:
        str: Generated word
    """

    # Validate category
    if category not in [1, 2, 3]:
        raise ValueError("Invalid category")

    choices = {
        1: [
            "lion",
            "tiger",
            "leopard",
            "jaguar",
            "cheetah",
            "cougar",
            "lynx",
            "bobcat",
            "ocelot",
            "caracal",
            "elephant",
            "rhinoceros",
            "hippopotamus",
            "giraffe",
            "zebra",
            "kangaroo",
            "koala",
            "wombat",
            "platypus",
            "panda",
            "red panda",
            "grizzly bear",
            "polar bear",
            "black bear",
            "brown bear",
            "sloth bear",
            "wolf",
            "coyote",
            "fox",
            "jackal",
            "hyena",
            "badger",
            "weasel",
            "otter",
            "ferret",
            "mongoose",
            "meerkat",
            "raccoon",
            "opossum",
            "armadillo",
            "porcupine",
            "deer",
            "elk",
            "moose",
            "caribou",
            "buffalo",
            "bison",
            "antelope",
            "gazelle",
        ],
        2: [
            "apple",
            "banana",
            "orange",
            "strawberry",
            "kiwi",
            "blueberry",
            "grape",
            "watermelon",
            "pineapple",
            "mango",
            "pomegranate",
            "peach",
            "pear",
            "apricot",
            "raspberry",
            "blackberry",
            "cherry",
            "cranberry",
            "fig",
            "grapefruit",
            "guava",
            "lemon",
            "lime",
            "lychee",
            "papaya",
            "passionfruit",
            "persimmon",
            "plum",
            "prickly pear",
            "pumpkin",
            "quince",
            "rambutan",
            "starfruit",
            "tangerine",
            "cantaloupe",
            "honeydew",
            "dragonfruit",
            "mulberry",
            "boysenberry",
            "elderberry",
            "gooseberry",
            "kiwano",
            "kumquat",
            "mulberry",
            "nectarine",
            "olive",
            "plantain",
            "tangelo",
        ],
        3: [
            "red",
            "green",
            "blue",
            "yellow",
            "pink",
            "purple",
            "orange",
            "brown",
            "black",
            "white",
            "gray",
            "silver",
            "gold",
            "maroon",
            "navy",
            "turquoise",
            "magenta",
            "teal",
            "beige",
            "lavender",
            "violet",
            "sky blue",
            "olive",
            "cream",
            "khaki",
            "mustard",
            "rust",
            "coral",
            "salmon",
            "peach",
            "lime",
            "forest green",
            "mint",
            "aqua",
            "indigo",
            "chartreuse",
            "fuchsia",
            "crimson",
            "marigold",
            "scarlet",
            "mauve",
            "rose",
            "taupe",
            "pale yellow",
            "baby blue",
            "dark green",
            "steel blue",
            "plum",
        ],
    }

    return random.choice(choices[category])


# Display hangman
def display_hangman(guess_word: list, guess_letters: list, attempts_left: int) -> None:
    """Display hangman game

    Args:
        guess_word (list): Current game word
        guess_letters (list): Guessed letters
        attempts_left (int): Number of attempts left

    Args:
        board (list): 3x3 Board
    """

    head = f"o" if attempts_left < 6 else ""
    body = f"|" if attempts_left < 5 else ""
    l_arm = f"/" if attempts_left < 4 else ""
    r_arm = f"\ " if attempts_left < 3 else ""
    l_foot = f"/ " if attempts_left < 2 else ""
    r_foot = f"\ " if attempts_left < 1 else ""

    print(f"Attempts left: {attempts_left}")
    print(f"Guessed letters: {guess_letters}")
    print(f"")
    print(f" _________")
    print(f"|         |")
    print(f"|         |")
    print(f"|         o")
    print(f"|        /|\ ")
    print(f"|        / \ ")
    print(f"|")
    print(f"|   _________")
    print(f"|  |         |")
    print(f"|  |         {head}")
    print(f"|  |        {l_arm}{body}{r_arm}")
    print(f"|  |        {l_foot}{r_foot}")
    print(f"|__|")
    print(f"")
    print(f"Guess the word: {' '.join(guess_word)}")


# Check if the game ended
def check_end_game(game_board: list, hidden_mines: list) -> bool | int:
    """Check if the game ended

    Args:
        game_board (list): Game board
        hidden_mines (list): Board with mines

    Returns:
        bool, int: Game ended check and result
            -1 - Lost game
             0 - Not ended
             1- won
    """

    # Exploded mines check
    check_exploded = bool(sum([row.count("X") for row in game_board]))

    # Lost game
    if check_exploded:

        for row in range(len(hidden_mines)):
            for column in range(len(hidden_mines[row])):
                if hidden_mines[row][column] == "O" and game_board[row][column] is "":
                    game_board[row][column] = "X"

        return True, -1

    # Find if there are any places left
    count_mines = sum([row.count("O") for row in hidden_mines])
    count_empty_places = sum([row.count("") for row in game_board])

    # won game
    if count_empty_places == count_mines:
        for row in range(len(hidden_mines)):
            for column in range(len(hidden_mines[row])):
                if hidden_mines[row][column] == "O" and game_board[row][column] is "":
                    game_board[row][column] = "O"

        return True, 1

    # Not ended game
    return False, 0


# Get category
def get_category() -> int:
    """Get the category from user input."""
    return int(
        input(
            "Categories:\n\n1 - Animals\n2 - Fruits\n3 - Colors\n\nSelect a category: "
        )
    )


# Initialize game
def initialize_game(category: int) -> tuple:
    """Initialize a game with a random word and other variables.

    Args:
        category (int): Category of the word
            1 - Animals
            2 - Fruits
            3 - Colors

    Returns:
        tuple containing

        - target_word (list): Selected word
        - guess_word (list): Current game word
        - attempts_left (int): Number of attempts left
        - guess_letters (list): Previous guessed letters
    """
    target_word = list(get_random_word(category=category))
    guess_word = list("_" * len(target_word))
    attempts_left = 6
    guess_letters = []

    # Fill spaces in the word
    if " " in target_word:
        guess_word[target_word.index(" ")] = "-"

    return target_word, guess_word, attempts_left, guess_letters


# Get player guess
def get_guess(
    target_word: list, guess_word: list, guess_letters: list, attempts_left: int
) -> tuple:
    """Get a guess from the user, validate it, and return it.

    Args:
        target_word (list): Selected word
        guess_word (list): Current game word
        guess_letters (list): Guessed letters
        attempts_left (int): Number of attempts left

    Returns:
        tuple containing

        - guess_word (list): Current game word
        - guess_letters (list): Previous guessed letters
        - attempts_left (int): Number of attempts left
    """
    while True:
        try:
            guess = input("\nSelect a letter: ").lower()

            # Guess validation
            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Invalid guess")

            # Guess validation
            if guess in guess_letters:
                raise ValueError("Letter already used")

            # Register letter
            guess_letters.append(guess)

            # Has the letter
            if guess in target_word:
                # Fill letter
                for index, letter in enumerate(target_word):
                    if guess == target_word[index]:
                        guess_word[index] = guess

            # Dont has the letter
            else:
                attempts_left -= 1

            return guess_word, guess_letters, attempts_left

        except ValueError as e:
            print(f"Error: {e}")


# Check if the game is lost
def is_game_lost(attempts_left: int) -> bool:
    """Return True if the game is lost, False otherwise.

    Args:
        attempts_left (int): Number of attempts left

    Returns:
        bool: is game lost
    """
    if attempts_left == 0:
        print("\nYou lost! Better luck next time!")
        return True
    return False


# Check if the game is won
def is_game_won(guess_word: list) -> bool:
    """Return True if the game is won, False otherwise.

    Args:
        guess_word (list): Current game word

    Returns:
        bool: is game lost
    """
    if "_" not in guess_word:
        print("\nYou won! Congratulation!")
        return True
    return False


def hangman() -> None:
    """Play a hangman game."""
    category = get_category()
    target_word, guess_word, attempts_left, guess_letters = initialize_game(category)

    end_game = False
    while not end_game:
        clear_terminal()
        display_hangman(
            guess_word=guess_word,
            guess_letters=guess_letters,
            attempts_left=attempts_left,
        )

        guess_word, guess_letters, attempts_left = get_guess(
            target_word, guess_word, guess_letters, attempts_left
        )

        if is_game_lost(attempts_left):
            end_game = True

        if is_game_won(guess_word):
            end_game = True


def main() -> None:
    """Main program"""
    # Reset the terminal
    clear_terminal()

    while True:

        try:
            # Start the game
            hangman()

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


r"""
 _________
|         |
|         o
|        /|\
|        / \
|
|   _________
|  |         |
|  |         o
|  |        /|\
|  |        / \
|__|

Guess the word: _ _ _ _ _ _ 

"""
