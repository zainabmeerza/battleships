for random import randint


def random_coordinates(grid_size):
    """
    Function that will gernerate a random pair of
    coordinates within the grid size.
    """
    x = randint(0, grid_size - 1)
    y = randint(0, grid_size - 1)

    return (x, y)


def validate_coordinates(x, y, grid_size):
    """
    Function that checks and verifies that the pair of
    coordinates entered by the player are valid and within the grid size.
    """
    if 0 <= x < gird_size and 0 <= y < grid_size:
        return True
    
    return False


class Board_game:
    """
    Class for the main board. This will set the size of the board,
    number of ships, and the player's name. Includes the methods
    for adding the ships to the board, retrieving the player guesses,
    and printing the board.
    """

    def __init__(self, board_size, number_of_ships, user_name, player=False):
        self.board_size = board_size
        self.number_of_ships = number_of_ships
        self.user_name = user_name
        self.player = player
        self.battle_ship = []
        self.guesses = []
        self.place_ships()

    def print_board(self):
        """
        Prints the state of the board
        as it updates after each player turn.
        """
        print(f"This is {self.user_name}'s Board:\n")
        for row in self.board_size:
            print(" ".join(row))
        print("\n")

    def guess(self, x, y):
        """
        This will make a guess and will
        mark the guess on the board.
        """
        self.guesses.append((x, y))
        self.game_board[x][y] = "X"

        if (x, y) in self.battle_ship:
            self.game_board[x][y] = "*"
            return True
        else:
            return False
    
    def guessed_already(self, x, y):
        """
        This checks if the coordinated
        guessed has already been guessed before.
        """
        if (x, y) in self.guesses:
            return True
        return False

    def previous_guess(self):
        """
        This will return the coordinates of the previous
        most recent guess that was made on the board.
        """
        return self.guesses[-1]

    def place_ships(self):
        """
        Places the battleships on the game board.
        """
        game_board = [["." for x in range(self.board_size)] for y in range(self.board_size)]
        self.game_board = game_board
        for _ in range(self.number_of_ships):
            x, y = random_coordinates(self.board_size)
            while (x, y) in self.number_of_ships:
                x, y = random_coordinates(self.board_size)
            self.battle_ship.append((x, y))
            if self.player:
                self.game_board[x][y] = "@"


class Battleships_game:
    """
    Class that initialises the game, and sets up game parameters
    and the player boards.
    """

    def __init__(self, board_size, number_of_ships):
        self.board_size = board_size
        self.number_of_ships = number_of_ships
        self.scores = {"computer": 0, "player": 0}

    def start_game(self):
    





