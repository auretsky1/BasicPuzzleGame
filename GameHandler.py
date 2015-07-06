import PuzzleBoard
import GameInstance
import pygame
import PuzzleGraphics


class GameHandler(object):
    # Default Constructor
    def __init__(self, game_screen):
        self.game_screen = game_screen

        # This variable will hold the game instance after the user has made a menu selection
        self.game_instance = GameInstance.GameInstance(1)

        # Set up the puzzle board to be used for this round
        self.puzzle_board = PuzzleBoard.PuzzleBoard(self.game_instance.board_size)

        # Set up the graphical representation of the puzzle board as seen by the user
        self.puzzle_graphic = PuzzleGraphics.PuzzleGraphics(self.puzzle_board.puzzle_board_size)

        # Set the graphics representation of our trigger list
        self.puzzle_graphic.set_trigger_list(self.puzzle_board.trigger_list)
        self.puzzle_graphic.set_activation_list(self.puzzle_board.puzzle_board)

        # These variables hold the current and previous mouse positions
        self.previous_position = pygame.mouse.get_pos()
        self.current_position = pygame.mouse.get_pos()

        # Create a string that holds the current time
        self.game_time_and_score = ["0:00", "Score:0"]

        # Create a pygame event that will be called each second to update the game timer
        pygame.time.set_timer(pygame.USEREVENT+1, 1000)

        # Set the timer font
        self.game_font = pygame.font.SysFont("monospace", 24)

        # Create the image to be used for the background as a pygame surface
        self.background_image = pygame.image.load("Images/background.jpg").convert()

        self.mouse_down = 0

    # Handle Game Logic
    def game_logic(self):
        # If the current position is not the old position the player has moved the mouse
        if self.previous_position != self.current_position:
            # Set the previous position to the new position and process the change
            self.previous_position = self.current_position
            # Tell the GUI for the puzzle to update
            self.puzzle_graphic.update_mouse_pos(self.current_position)
        if self.mouse_down == 1:
            location = self.puzzle_graphic.activate_cube(self.current_position)
            if not location:
                self.mouse_down = 0
            else:
                is_board_complete = self.puzzle_board.activate_board_location(location)
                self.puzzle_graphic.set_activation_list(self.puzzle_board.puzzle_board)
                self.puzzle_graphic.change_to_off()
                self.puzzle_graphic.draw_puzzle_board()
                self.mouse_down = 0
                if is_board_complete:
                    self.puzzle_board.reset_puzzle_board()
                    self.game_instance.board_complete()

    # Handle Drawing Game Objects
    def draw_game_objects(self):
        # Draw the game background
        self.game_screen.blit(self.background_image, [0, 0])

        # Draw the timer
        self.draw_timer_and_score(self.game_time_and_score)

        # Draw the puzzle board to the screen with highlighting
        puzzle_board = self.puzzle_graphic.draw_board
        self.game_screen.blit(puzzle_board, self.puzzle_graphic.board_position)

    # Handle User Input
    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.reinitialize_game(1)
            elif event.key == pygame.K_2:
                self.reinitialize_game(2)
            elif event.key == pygame.K_3:
                self.reinitialize_game(3)
            elif event.key == pygame.K_a and self.game_instance.game_mode == 1:
                self.reinitialize_game(4)
            elif event.key == pygame.K_s and self.game_instance.game_mode == 1:
                self.reinitialize_game(5)

        if event.type == pygame.USEREVENT+1:  # GameTimer tick
            self.game_time_and_score = self.game_instance.update_time()
        if event.type == pygame.MOUSEMOTION:
            self.current_position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_down = 1

    # Draw the timer to the upper left corner of the screen
    def draw_timer_and_score(self, time_and_score_string):
        # Full display text combining time and score
        display_text = time_and_score_string[0] + " " + time_and_score_string[1]

        # Render the text using the current time
        display_render = self.game_font.render(display_text, True, (255, 255, 255))

        # Blit the newly rendered text to the main game screen
        self.game_screen.blit(display_render, (0, 0))

    # Alter the game mode and reinitialize components
    def reinitialize_game(self, game_mode):
        # Check if game_mode is over 3 for mode 1 increase/decrease
        if game_mode == 4:
            # User hit A so board shrinks by 1
            board_size = self.game_instance.board_size - 1

            # User hit A so the mode is still 1
            game_mode = 1
        elif game_mode == 5:
            # User hit S so board shrinks by 1
            board_size = self.game_instance.board_size + 1

            # User hit S so the mode is still 1
            game_mode = 1
        else:
            # User entered moe 2 or 3
            board_size = 3

        # Create a new game instance
        self.game_instance = GameInstance.GameInstance(game_mode, board_size)

        # Set up the puzzle board to be used for this round
        self.puzzle_board = PuzzleBoard.PuzzleBoard(self.game_instance.board_size)

        # Set up the graphical representation of the puzzle board as seen by the user
        self.puzzle_graphic = PuzzleGraphics.PuzzleGraphics(self.puzzle_board.puzzle_board_size)

        # Set the graphics representation of our trigger list
        self.puzzle_graphic.set_trigger_list(self.puzzle_board.trigger_list)
        self.puzzle_graphic.set_activation_list(self.puzzle_board.puzzle_board)
