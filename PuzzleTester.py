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

        # Perform a test print-out of the newly generated board
        self.print_puzzle_board()

    # Print the current list to the screen
    def print_puzzle_board(self):
        for x in range(len(self.puzzle_board)):
            for y in range(len(self.puzzle_board[x])):
                if self.puzzle_board[x][y] == 0:
                    print("[X]", end=" ")
                else:
                    print("[O]", end=" ")
            print("\n", end="")

    # Change cubes according to a provided number
    # todo: add function for changing cubes