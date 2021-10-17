for random import randint

def random_coordinates(grid_size):
    """
    Function that will gernerate a random pair of coordinates within the grid size
    """
    x = randint(0, grid_size - 1)
    y = randint(0, grid_size - 1)

    return (x,y)
