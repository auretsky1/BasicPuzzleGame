""" The purpose of this class is to test the puzzle generation algorithm in text form. The output will appear in
    the python console. The proper way to activate or deactivate cubes is to type the corresponding number. """
import PuzzleGenerator


class PuzzleTester(object):
    # Constructor - Assumes 3X3 puzzle but can be customized with 'size'
    def __init__(self, size=3):
        # Create the puzzle board and default each cube to off position
        self.puzzle_board = []
        for x in range(0, size):
            puzzle_row = [0 for y in range(size)]
            self.puzzle_board.append(puzzle_row)

        # Acquire a trigger list given the size of this map
        self.trigger_list = PuzzleGenerator.generate_trigger_list(size)

        # Set the size of the board for this object
        self.puzzle_board_size = size

        # Perform a test print-out of the newly generated board
        self.print_puzzle_board()

    # Print the current list to the screen
    def print_puzzle_board(self):
        """ Prints out a text representation of our puzzle board. This is done using text-blocks in rows where an
        'X' represents an off cube and a 'O' represents an on cube. """
        for x in range(len(self.puzzle_board)):
            for y in range(len(self.puzzle_board[x])):
                if self.puzzle_board[x][y] == 0:
                    print("[X]", end=" ")
                else:
                    print("[O]", end=" ")
            print("\n", end="")

    # Change cubes according to a provided number
    def activate_board_location(self, location):
        """ This function will take a location (the actual physical location on the board starting with 1
        in the upper left and ending with n in the lower right where n is the number of cubes) and then access
        that location in the trigger list to see which cubes to invert from OFF/ON and vice versa. """
        for x in self.trigger_list[location-1]:
            # Get the 2D position of x so as to activate or deactivate that cube.
            (row, column) = self.convert_to_board_position(location)

            # If the cube is off turn it on and vise versa
            if self.puzzle_board[row][column] == 0:
                self.puzzle_board[row][column] = 1
            else:
                self.puzzle_board[row][column] = 0

    # Calculate the 2D position of the cube on the map from a 1D location given.
    def convert_to_board_position(self, location):
        """ This function takes a 1D position (such as cube 8 of 9) and turns that into a 2D value
        to be returned as a tuple such as (3, 2). """
        # Set the location to be 0-indexed
        location -= 1

        # Determine the row and column of this point
        puzzle_row = location // self.puzzle_board_size
        puzzle_column = location % self.puzzle_board_size

        # Return this value as a tuple
        return puzzle_row, puzzle_column