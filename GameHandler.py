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
        self.puzzle_graphic = PuzzleGraphics.PuzzleGraphics(3)
        trigger_list = self.puzzle_graphic.get_trigger_list(puzzle_board.trigger_list)
        self.mouse_move = 0
        pass

    # Handle Game Logic
    def game_logic(self):
        if self.mouse_move == 1:
            mouse_pos = pygame.mouse.get_pos()
            self.puzzle_graphic.update_mouse_pos(mouse_pos)
        else:
            pass

    # Handle Drawing Game Objects
    def draw_game_objects(self):
        puzzle_board = self.puzzle_graphic.draw_board
        self.game_screen.blit(puzzle_board, self.puzzle_graphic.board_position)
    # Handle User Input
    def process_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.mouse_move = 1
        else:
            self.mouse_move = 0