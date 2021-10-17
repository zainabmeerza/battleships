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

    def __init__(self, board_size, number_of_ships, user_name, player =False):
        self.board_size = board_size
        self.number_of_ships = number_of_ships
        self.user_name = user_name
        self.player = player
        self.battleships = []
        self.guesses = []
        self.place_ships()

        
