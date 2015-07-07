""" This class handles all the data required for the current game instance. When the user makes a selection from the
    menu (or goes back to the menu and makes a new selection) a new instance of this class is created and  handles
    updating things such as new goal time, time requirements, etc. """
import GameTimer
import pygame
from GlobalConstants import *


class GameInstance(object):
    # Constructor
    def __init__(self, game_mode=0, board_size=3):
        # Create a timer to use for all game timing events
        self.game_timer = GameTimer.GameTimer()

        # The time goal of the current game instance (in seconds)
        self.time_goal = 0

        # The current score of the player (equal to the number of levels completed)
        self.game_score = 0

        # Current game board size
        self.board_size = board_size

        # Make sure board size is within bounds
        if self.board_size < 3:
            self.board_size = 3
        if self.board_size > 10:
            self.board_size = 10

        # Set the value of the current game mode
        self.game_mode = game_mode

        # Create a new version of the selected game mode
        self.initialize_game_mode(game_mode)

    # Setup the initial conditions for each specific game mode
    def initialize_game_mode(self, game_mode):
        # (1 = endless, 2 = time trial, 3 = race mode)
        if game_mode == 1:
            # Set the timer to count up infinitely as a reference for the player
            self.game_timer.countup_forever()
        elif game_mode == 2:
            # Set the initial time for the 3X3 board to 3 minutes.
            self.game_timer.countdown(180)

            # Set the initial board_size for this mode to be 3X3
            self.board_size = 3
        elif game_mode == 3:
            # Set the timer to count up infinitely until the player completes the mode
            self.game_timer.countup_forever()

            # Set the initial board_size for this mode to be 3X3
            self.board_size = 3

    # Allow the caller to trigger a timer update and process game modes accordingly
    def update_time(self):
        # Update the timer by one second
        current_time = self.game_timer.timer_update()

        # Check if the goal time has been reached and act accordingly for each game mode
        if self.game_timer.timer_check() and self.game_mode == 2:
            return "Time Out", "Score:" + str(self.game_score)

        # Check to see if we are in mode 3 and finished the last board
        if self.game_mode == 3 and self.board_size == 11:
            return "Finished! " + current_time, "Score:" + str(self.game_score)

        # Time has either not run out or we are in mode 1/3, return time & score
        return current_time, "Score:" + str(self.game_score)

    # Allow the caller to trigger a board completion iterating the score by 1
    def board_complete(self):
        # Update the score by 1
        self.game_score += 1

        # Pass back to the caller the required size of the new board and set the timer accordingly
        if self.game_mode == 1:
            # Just return the same board size to be used again
            return self.board_size
        elif self.game_mode == 2:
            # Increase the board size by 1
            self.board_size += 1

            # If we've reached 11 set back to 3
            if self.board_size == 11:
                self.board_size = 3

            # Increase the timer for the next level of time-trial
            self.game_timer.countdown((self.board_size * (self.board_size - 2) * 60))

            # Return board size to the caller
            return self.board_size
        elif self.game_mode == 3:
            # Increase the board size by 1
            self.board_size += 1

            # If we've reached 11 the mode is finished
            if self.board_size == 11:
                return 0  # 0 Represents a finished state





