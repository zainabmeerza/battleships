from random import randint


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
    if 0 <= x < grid_size and 0 <= y < grid_size:
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
        for row in self.game_board:
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
            while (x, y) in self.battle_ship:
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
        """
        Displays the welcome screen, initialises the 
        game boards, and proceeds to start the game.
        """
        self.display_info()
        temporary_board = Board_game(self.board_size, self.number_of_ships,
                                     "Computer", player=False)
        self.computer_board = temporary_board
        player_name = input("Please enter your name: \n")
        print("-" * 150)
        temporary_board = Board_game(self.board_size, self.number_of_ships,
                                     player_name, player=True)
        self.player_board = temporary_board

        self.play_game()

    def play_game(self):
        """
        The main game loop that processes the guess and exits the game
        once it is complete or quits upon request by user playing.
        """

        while True:
            self.print_board()
            if self.game_over():
                if (self.scores['player']) > (self.scores['computer']):
                    print("                                    _          _ ")
                    print("                                   (_)        | |")
                    print(" _   _   ___   _   _     __      __ _  _ __   | |")
                    print("| | | | / _ \ | | | |    \ \ /\ / /| || '_ \  | |")
                    print("| |_| || (_) || |_| |     \ V  V / | || | | | |_|")
                    print(" \__, | \___/  \__,_|      \_/\_/  |_||_| |_| (_)")
                    print("  __/ |                                          ")
                    print(" |___/                                         \n")

                elif (self.scores['player']) < (self.scores['computer']):
                    print("                          _                     _ ")
                    print("                         | |                   | |")
                    print(" _   _   ___   _   _     | |  ___   ___   ___  | |")
                    print("| | | | / _ \ | | | |    | | / _ \ / __| / _ \ | |")
                    print("| |_| || (_) || |_| |    | || (_) |\__ \|  __/ |_|")
                    print(" \__, | \___/  \__,_|    |_| \___/ |___/ \___| (_)")
                    print("  __/ |                                           ")
                    print(" |___/                                          \n")
                else:
                    print(" _  _   _                       _                        _ ")
                    print("(_)| | ( )                     | |                      | |")
                    print(" _ | |_|/ ___      __ _      __| | _ __  __ _ __      __| |")
                    print("| || __| / __|    / _` |    / _` || '__|/ _` |\ \ /\ / /| |")
                    print("| || |_  \__ \   | (_| |   | (_| || |  | (_| | \ V  V / |_|")
                    print("|_| \__| |___/    \__,_|    \__,_||_|   \__,_|  \_/\_/  (_) \n")
                print(" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗    ")
                print(" █╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗   ")
                print(" █║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝   ")
                print(" █║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ")
                print(" ██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║██╗")
                print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝\n")
                print(f"{self.player_board.user_name}: " +
                      f"{self.scores['player']} VS. Computer: "
                      + f"{self.scores['computer']}")
                break

            # PLAYER TAKES A GUESS
            x, y = self.play_guess()
            while not self.guess_valid(x, y):
                x, y = self.play_guess()
            hit_player = self.computer_board.guess(x, y)

            # COMPUTER MAKES A GUESS
            x, y = random_coordinates(self.board_size)
            while self.player_board.guessed_already(x, y):
                x, y = random_coordinates(self.board_size)
            hit_computer = self.player_board.guess(x, y)

            # END OF A GAME ROUND
            self.round_score(hit_player, hit_computer)
            user_choice = input("Type \"quit\" to quit the game or any key " +
                                "to continue. \n")
            if user_choice == "quit":
                break

    def play_guess(self):
        """
        Asks the players for 2 numbers to pick a coordinate
        on the game board, and checks that the numbers entered
        are valid
        """
        while True:
            try:
                print("-" * 150)
                x = input("Guess a row: \n")
                x = int(x)
                y = input("Guess a column: \n")
                y = int(y)
                break
            except ValueError:
                print("Row and column must be valid numbers")

        return (x, y)

    def print_board(self):
        """
        Print the current board status on the screen
        """
        self.player_board.print_board()
        self.computer_board.print_board()

    def guess_valid(self, x, y):
        """
        Checks if the coordinates given are within the range of
        the board size, and if the coordinates have been repeated.   
        """
        if not validate_coordinates(x, y, self.board_size):
            print("Row and column must be a value between"
                  + f"0 and {self.board_size - 1}")
            return False
        if self.computer_board.guessed_already(x, y):
            print("You cannot guess the same coordinates more than once.")
            return False
        return True

    def game_over(self):
        """
        This will check if either player has sunk the
        other player's battleships
        """
        if self.scores["player"] >= self.number_of_ships or \
           self.scores["computer"] >= self.number_of_ships:
            return True
        return False

    def round_score(self, hit_player, hit_computer):
        """
        This will output the updated scores after each round
        """
        print("-" * 150)
        print(f"{self.player_board.user_name} guessed " +
              f"{self.computer_board.previous_guess()}")
        if hit_player:
            self.scores["player"] += 1
            print("That was a \033[1mHIT!\033[0m \n")
        else:
            print("That was a \033[1mMISS!\033[0m \n")
        print(f"Computer guessed {self.player_board.previous_guess()}")
        if hit_computer:
            self.scores["computer"] += 1
            print("That was a \033[1mHIT!\033[0m \n")
        else:
            print("That was a \033[1mMISS!\033[0m \n")
        print("The current scores are:")
        print(f"{self.player_board.user_name}: " +
              f"{self.scores['player']} VS. Computer: "
              + f"{self.scores['computer']}")
        print("-" * 150)

    def display_info(self):
        """
        Displays welcome message and information about the board
        """
        print("-" * 150)
        print("WELCOME TO A GAME OF BATTLESHIPS\n")
        print(f"Board Size: {self.board_size} x {self.board_size}.\n"
              f"Number of ships: {self.number_of_ships} \n")
        print("GAME INSTRUCTIONS:\n")
        print("Guess the ship coordinates of your opponent.\n"
              "Aim to HIT all the oponenets ships.\nEnter a"
              "row number and column number to guess the coordinates.")
        print("The top left corner is row: 0 and column: 0\n")
        print("--------------------- LEGEND -------------------------\n")
        print("(@) = a ship on the battlefield\n(*) = coordinates guessed are"
              + "a HIT!\n(X) = coordinates guessed are a MISS!\n")
        print("-" * 150)


# ASK THE USER WHAT GRID SIZE THEY WOULD LIKE TO PLAY ON
# THEN STARTS A NEW GAME
while True:
    print("\n")
    print("██████╗  █████╗ ████████╗████████╗██╗     ███████╗")
    print("██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝")   
    print("██████╔╝███████║   ██║      ██║   ██║     █████╗ ")    
    print("██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ")     
    print("██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗")  
    print("╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝")   
    print("   ███████╗██╗  ██╗██╗██████╗ ███████╗ ")
    print("   ██╔════╝██║  ██║██║██╔══██╗██╔════╝")
    print("   ███████╗███████║██║██████╔╝███████╗")
    print("   ╚════██║██╔══██║██║██╔═══╝ ╚════██║")
    print("   ███████║██║  ██║██║██║     ███████║")
    print("   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝\n")
    
    board_size = input("What grid size do you want to use? \n")
    
    print("                                ")
    print("                                ")
    print("  __ _   __ _  _ __ ___    ___  ")
    print(" / _` | / _` || '_ ` _ \  / _ \ ") 
    print("| (_| || (_| || | | | | ||  __/ ") 
    print(" \__, | \__,_||_| |_| |_| \___| ") 
    print("  __/ |                         ")
    print(" |___/                          ")
    print("\n")
    print("       _                _    _ ")
    print("      | |              | |  (_)")
    print("  ___ | |_  __ _  _ __ | |_  _  _ __    __ _         ")
    print("/ __|| __|/ _` || '__|| __|| || '_ \  / _` |         ")
    print("\__ \| |_| (_| || |   | |_ | || | | || (_| | _  _  _ ")
    print("|___/ \__|\__,_||_|    \__||_||_| |_| \__, |(_)(_)(_)")
    print("                                       __/ |         ")
    print("                                      |___/          ")
    print("\n")
    
    try:
        board_size = int(board_size)
        break
    except ValueError:
        print("Row and column must be numbers")

game = Battleships_game(board_size=board_size, number_of_ships=4)
game.start_game()