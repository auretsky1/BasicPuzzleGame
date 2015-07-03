import PuzzleBoard
import pygame
import PuzzleGraphics


class GameHandler(object):
    # Default Constructor
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.board_position = (100, 200)
        puzzle_board = PuzzleBoard.PuzzleBoard(3)
        puzzle_board.activate_board_location(1)
        puzzle_board.activate_board_location(9)
        puzzle_board.reset_puzzle_board()
        self.puzzle_graphic = PuzzleGraphics.PuzzleGraphics(3, self.board_position)

        pass

    # Handle Game Logic
    def game_logic(self):
        PuzzleGraphics.PuzzleGraphics.mouse_pos = pygame.mouse.get_pos()

    # Handle Drawing Game Objects
    def draw_game_objects(self):
        puzzle_board = self.puzzle_graphic.draw_cubes()
        self.game_screen.blit(puzzle_board, (self.board_position))

    # Handle User Input
    def process_event(self):
        pass