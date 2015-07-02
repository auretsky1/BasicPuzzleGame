import GameHandler
import pygame
from GlobalConstants import *

# Variables
is_game_running = True

# Initialize PyGame
pygame.init()
pygame.font.init()

# Setup the program window
pygame.display.set_caption("Puzzle Game")

# Initialize the screen
# FIXME: game_screen = pygame.display.set_mode(SCREEN_SIZE, SCREEN_FLAGS, SCREEN_DEPTH)
game_handler = GameHandler.GameHandler()

# Create the game clock
game_clock = pygame.time.Clock()

# Main game loop
while is_game_running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
        if event.type == pygame.KEYDOWN:
            game_handler.process_event(event)

    # Do game logic
    game_handler.game_logic()

    # Clear the screen
    # FIXME: game_screen.fill(BLACK)

    # Draw game objects
    game_handler.draw_game_objects()

    # Draw the screen
    # FIXME: pygame.display.flip()

    # Frame-rate
    game_clock.tick(60)