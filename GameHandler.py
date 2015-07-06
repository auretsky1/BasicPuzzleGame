import PuzzleBoard
import GameTimer
import pygame
import PuzzleGraphics


class GameHandler(object):
    # Default Constructor
    def __init__(self, game_screen):
        self.game_screen = game_screen

        # Set up the puzzle board to be used for this round
        self.puzzle_board = PuzzleBoard.PuzzleBoard(5)

        # Set up the graphical representation of the puzzle board as seen by the user
        self.puzzle_graphic = PuzzleGraphics.PuzzleGraphics(self.puzzle_board.puzzle_board_size)

        # Set the graphics representation of our trigger list
        self.puzzle_graphic.set_trigger_list(self.puzzle_board.trigger_list)
        self.puzzle_graphic.set_activation_list(self.puzzle_board.puzzle_board)

        # Create a timer to use for all game timing events
        self.game_timer = GameTimer.GameTimer()

        # These variables hold the current and previous mouse positions
        self.previous_position = pygame.mouse.get_pos()
        self.current_position = pygame.mouse.get_pos()

        # Create a string that holds the current time
        self.game_time = "0:00"

        # Create a pygame event that will be called each second to update the game timer
        pygame.time.set_timer(pygame.USEREVENT+1, 1000)

        # Set the timer font
        self.timer_font = pygame.font.SysFont("monospace", 24)

        # Create the image to be used for the background as a pygame surface
        self.background_image = pygame.image.load("Images/background.jpg").convert()

    # Handle Game Logic
    def game_logic(self):
        # If the current position is not the old position the player has moved the mouse
        if self.previous_position != self.current_position:
            # Set the previous position to the new position and process the change
            self.previous_position = self.current_position

            # Tell the GUI for the puzzle to update
            self.puzzle_graphic.update_mouse_pos(self.current_position)

        # Check to see if timer reached goal
        # todo: do something if timer has reached goal

    # Handle Drawing Game Objects
    def draw_game_objects(self):
        # Draw the game background
        self.game_screen.blit(self.background_image, [0, 0])

        # Draw the timer
        self.draw_timer(self.game_time)

        # Draw the puzzle board to the screen with highlighting
        puzzle_board = self.puzzle_graphic.draw_board
        self.game_screen.blit(puzzle_board, self.puzzle_graphic.board_position)

    # Handle User Input
    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            # todo: testing timer
            self.game_timer.countup(10)
        if event.type == pygame.USEREVENT+1:  # GameTimer tick
            self.game_time = self.game_timer.timer_update()
        if event.type == pygame.MOUSEMOTION:
            self.current_position = pygame.mouse.get_pos()

    # Draw the timer to the upper left corner of the screen
    def draw_timer(self, time_string):
        # Render the text using the current time
        display_time = self.timer_font.render(time_string, True, (255, 255, 255))

        # Blit the newly rendered text to the main game screen
        self.game_screen.blit(display_time, (0, 0))