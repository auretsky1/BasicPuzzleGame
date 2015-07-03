import PuzzleBoard
import pygame


class GameHandler(object):
    # Default Constructor
    def __init__(self):
        puzzle_board = PuzzleBoard.PuzzleBoard(3)
        puzzle_board.activate_board_location(1)
        puzzle_board.activate_board_location(9)
        puzzle_board.reset_puzzle_board()
        pass

    # Handle Game Logic
    def game_logic(self):
        pass

    # Handle Drawing Game Objects
    def draw_game_objects(self):
        pass

    # Handle User Input
    def process_event(self):
        pass