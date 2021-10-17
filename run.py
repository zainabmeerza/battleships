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

