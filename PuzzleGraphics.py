""" This class will be responsible for drawing the cubes to the game screen and updating the highlighting in accordance
    with which ones are on and off as well as where the user's mouse is located. These changes can be called as functions
    by an outside module or class with the relevant data needed to make a change"""
import pygame
from GlobalConstants import *


class PuzzleGraphics(object):

    # get the position of the mouse
    def __init__(self, size=3):
        # Get the size of the puzzle board
        self.size = size

        # Sets size of puzzle board image
        self.width = SCREEN_SIZE[0] // 2
        self.length = SCREEN_SIZE[1] // 2
        self.puzzle_area = (self.width, self.length)

        # Set the unit for each cube
        self.cube_width = self.puzzle_area[0] // self.size
        self.cube_length = self.puzzle_area[1] // self.size

        # Get the position of the puzzle board that is drawn to the screen
        self.board_position = self.set_position()

        # Creates a surface for the puzzle board
        self.puzzle_image = pygame.Surface([self.puzzle_area[0], self.puzzle_area[1]])
        self.puzzle_image.fill(BLACK)

        # Get the maximum number that is possible for this grid size
        self.n_max = self.size ** 2

        # Creates the images of the cube
        self.on_cube = self.create_image('Images/lightblue.jpg')
        self.off_cube = self.create_image('Images/gray.jpg')

        # Create a list of surfaces that will hold each cube
        self.puzzle_board = self.create_cube_surface()

        # Gets the position of the mouse
        self.mouse_pos = (0, 0)

        # Draw Board
        self.draw_board = self.draw_puzzle_board()

        self.trigger_list = []
        self.activations = []

    # sets the trigger list
    def set_trigger_list(self, trigger_list):
        self.trigger_list = trigger_list

    def set_activation_list(self, activation_list):
        self.activations = activation_list

    # Sets cube to on
    def change_to_on(self, x):
        check_on_value = self.on_cube.get_at((0, 0))
        check_off_value = self.off_cube.get_at((0, 0))
        check_current_value = self.puzzle_board[x].get_at((0, 0))
        for y in range(len(self.trigger_list[x])):
            element = self.trigger_list[x][y] - 1
            if check_on_value == check_current_value:
                self.puzzle_board[element].blit(self.off_cube, [0, 0])
            if check_off_value == check_current_value:
                self.puzzle_board[element].blit(self.on_cube, [0, 0])

    # Sets all cubes to off depending on there activation status
    def change_to_off(self):
        for x in range(len(self.activations)):
            for y in range(len(self.activations[x])):
                row = x // self.size
                column = y % self.size
                element = (x * self.size) + y
                if self.activations[row][column] == 0:
                    self.puzzle_board[element].blit(self.off_cube, [0, 0])
                else:
                    self.puzzle_board[element].blit(self.on_cube, [0, 0])

    # converts the mouse position to a location in a list
    def convert_to_list_position(self):
        y_pos = self.mouse_pos[0] // self.cube_width
        x_pos = self.mouse_pos[1] // self.cube_length
        list_location = (x_pos * self.size) + y_pos
        return list_location

    # Checks to see if mouse is hovering over a cube
    def is_highlighted(self):
        if self.mouse_pos[0] < 0 or self.mouse_pos[0] > self.puzzle_area[0] - 1\
                or self.mouse_pos[1] < 0 or self.mouse_pos[1] > self.puzzle_area[1] - 1:
            return False
        else:
            return True

    # Loads and creates an image
    def create_image(self, name):
        # Loads the image
        image = pygame.image.load(name).convert()

        # Resizes image to fit grid unit
        new_image = pygame.transform.scale(image, (self.cube_width, self.cube_length))
        return new_image

    # Sets the position of the puzzle board image on the game screen
    def set_position(self):
        screen_center_x = SCREEN_SIZE[0] // 2
        screen_center_y = SCREEN_SIZE[1] // 2
        position_x = screen_center_x - (self.puzzle_area[0]//2)
        position_y = screen_center_y - (self.puzzle_area[1]//2)
        return position_x, position_y

    # Creates a list of cube surfaces
    def create_cube_surface(self):
        cube_surface = []
        for x in range(self.n_max):
            cube = pygame.Surface([self.cube_width, self.cube_length])
            cube.blit(self.off_cube, [0, 0])
            cube_surface.append(cube)
        return cube_surface

    # Updates the position of the mouse in relation to the board position
    def update_mouse_pos(self, mouse_pos):
        mouse_x = mouse_pos[0] - self.board_position[0]
        mouse_y = mouse_pos[1] - self.board_position[1]
        self.mouse_pos = (mouse_x, mouse_y)

        # Check if highlighted
        if self.is_highlighted():
            # Call convert to list position
            list_location = self.convert_to_list_position()
            # Call turn_off_cubes
            self.change_to_off()
            # Turn on cubes for the list position
            self.change_to_on(list_location)
            self.draw_puzzle_board()
        else:
            self.change_to_off()
            self.draw_puzzle_board()

    def draw_puzzle_board(self):
        # Draws cubes to puzzle board surface
        for x in range(self.n_max):
            puzzle_row = x // self.size
            puzzle_column = x % self.size
            cube_x = puzzle_column * self.cube_length
            cube_y = puzzle_row * self.cube_width
            self.puzzle_image.blit(self.puzzle_board[x], [cube_x, cube_y])

        return self.puzzle_image





