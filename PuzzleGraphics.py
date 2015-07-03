""" This class will be responsible for drawing the cubes to the game screen and updating the highlighting in accordance
    with which ones are on and off as well as where the user's mouse is located. These changes can be called as functions
    by an outside module or class with the relevant data needed to make a change"""
import pygame
import PuzzleBoard
from GlobalConstants import *



class PuzzleGraphics(object):

    # get the position of the mouse
    mouse_pos = None
    def __init__(self, size=3, board_position=(0,0)):
        # Get the size of the puzzle board
        self.size = size
        # Get the position of the puzzle board that is drawn to the screen
        self.board_position = board_position
        # Size of the puzzle board
        self.puzzle_area = (400, 400)
        # Creates a surface for the puzzle board
        self.puzzle_image = pygame.Surface([self.puzzle_area[0], self.puzzle_area[1]])
        self.puzzle_image.fill(BLACK)
        # Get the maximum number that is possible for this grid size
        self.max_cubes = self.size ** 2
        # Set the unit for each cube
        self.cube_width = self.puzzle_area[0]/self.size
        self.cube_length = self.puzzle_area[1]/self.size
        # Creates the images of the cube
        self.on_cube = self.create_image('Images/lightblue.png')
        self.off_cube = self.create_image('Images/gray.png')

    # Checks to see if mouse is hovering over a cube
    def is_highlighted(self, position):
        # Gets the position of the mouse in relation to the board position
        mouse_pos = PuzzleGraphics.mouse_pos
        mouse_x = mouse_pos[0] - self.board_position[0]
        mouse_y = mouse_pos[1] - self.board_position[1]
        if position[0] <= mouse_x <= position[0] + self.cube_width and position[1] <= mouse_y <= position[1] + \
                self.cube_length:
            return True
        else:
            return False
    # Loads and creates an image
    def create_image(self, Name):
        # Loads the image
        image = pygame.image.load(Name).convert()
        # Resizes image to fit grid unit
        new_image = pygame.transform.scale(image, (int(self.cube_width), int(self.cube_length)))
        return new_image

    # Draws the cubes for the puzzle
    def draw_cubes(self):
        # Checks to see if cube is being highlighted by mouse
        highlight = []
        for x in range(self.max_cubes):
            highlight.append([x])
            for y in range(self.max_cubes):
                highlight[x].append(y)
                cube_x = y * self.cube_width
                cube_y = x * self.cube_length
                position = (cube_x, cube_y)
                if self.is_highlighted(position):
                    highlight[x][y] = 0
                else:
                    highlight[x][y] = 1
        # Creates and draws cube to puzzle board surface
        for x in range(self.max_cubes):
            for y in range(self.max_cubes):
                cube = pygame.Surface([self.cube_width, self.cube_length])
                rect = cube.get_rect()
                if highlight[x][y] == 0:
                    cube.blit(self.on_cube, [0, 0])
                else:
                    cube.blit(self.off_cube, [0,0])
                cube_x = x * self.cube_length
                cube_y = y * self.cube_width
                self.puzzle_image.blit(cube, [cube_y, cube_x])

        return self.puzzle_image









