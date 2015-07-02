import PuzzleTester
import pygame


class GameHandler(object):
    # Default Constructor
    def __init__(self):
        # todo: replace this with a class used specifically for graphic processing instead of text
        self.puzzle_tester = PuzzleTester.PuzzleTester(3)
        pass

    # Handle Game Logic
    def game_logic(self):
        # todo: replace this when switching over to graphic interface
        selected_location = int(input("\nPlease input the next block location: "))
        self.puzzle_tester.activate_board_location(selected_location)
        pass

    # Handle Drawing Game Objects
    def draw_game_objects(self):
        # todo: replace this when switching over to graphic interface
        self.puzzle_tester.print_puzzle_board()
        pass

    # Handle User Input
    def process_event(self):
        pass