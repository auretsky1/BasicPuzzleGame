""" This class handles the actual puzzle board as it is represented in code. It can create the board and can take
    custom sizes. It can activate and deactivate corresponding switches in code, as well as reset the state of the
    board. It checks for completion and can alter the puzzle accordingly. A new instance of this class should be
    created each time a new puzzle is desired. """
import PuzzleGenerator
import PuzzleGraphics


class PuzzleBoard(object):
    def __init__(self, size=3):
        # Create the puzzle board and default each cube to off position
        self.puzzle_board = []
        for x in range(0, size):
            puzzle_row = [0 for y in range(size)]
            self.puzzle_board.append(puzzle_row)

        # Acquire a trigger list given the size of this map
        self.trigger_list = PuzzleGenerator.generate_trigger_list(size)


        # Set the size of the board for this object (width = height = size)
        self.puzzle_board_size = size

    # Change cubes according to a provided number and returns True if board is complete
    def activate_board_location(self, location):
        """ This function will take a location (the actual physical location on the board starting with 1
        in the upper left and ending with n in the lower right where n is the number of cubes) and then access
        that location in the trigger list to see which cubes to invert from OFF/ON and vice versa. """
        for x in self.trigger_list[location-1]:
            # Get the 2D position of x so as to activate or deactivate that cube.
            (row, column) = self.convert_to_board_position(x)

            # If the cube is off turn it on and vise versa
            if self.puzzle_board[row][column] == 0:
                self.puzzle_board[row][column] = 1
            else:
                self.puzzle_board[row][column] = 0

        # Check if the board is complete and return this to the caller
        return self.check_board_completion()

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

    # Reset the entire board so all cubes are in the off state. This does not change the trigger list
    def reset_puzzle_board(self):
        for x in range(1, (self.puzzle_board_size**2) + 1):
            (row, column) = self.convert_to_board_position(x)
            self.puzzle_board[row][column] = 0

    # Check if the board is in a complete state and if so return true
    def check_board_completion(self):
        for x in range(len(self.puzzle_board)):
            if 0 in self.puzzle_board[x]:
                return False
        return True