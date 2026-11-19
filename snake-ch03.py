import pygame
from pygame.math import Vector2                     #3.6 - Import Vector2 from pygame.math so that we can give objects positions
import random                                       #3.16 - Import random so that we can create random spawn points for the Food

# Color Palette
GREEN = 0xaacc60
DARK_GREEN = 0x2b3318

# Grid Layout
cell_size = 30                                      #3.1 - Cell area
number_of_cells = 25                                #3.2 - Cell amount

# Create Food class:
class Food:                                         #3.4 - Food class definition
    def __init__(self):                             #3.5 - Food constructor
        # self.position = Vector2(5, 6)             #3.7 - Initialize a Food object to spawn at (5, 6)
        self.position = self.generate_random_pos()  #3.21 - Change line #3.7 to initialize a Food object to spawn at a random position (Run #5 multiple times)

    def draw(self):                                 #3.8 - Draw method for Food class, will draw a Food object on screen at self.position
        food_rect = pygame.Rect(                    #3.9 - Define a rectangular area for the Food with position (x, y) and dimensions (cell_size, cell_size)
            self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)

        # pygame.draw.rect(                         #3.10 - Draw a DARK_GREEN rectangle on the screen with the area defined by food_rect
            # screen, DARK_GREEN, food_rect)

        screen.blit(food_surface, food_rect)        #3.14 - Draw the image onto the rectangular area and delete line #3.10 (Run #4)

    def generate_random_pos(self):                  #3.15 - Randomize Position method for Food class, will create a random (x, y) position for the Food
        x = random.randint(                         #3.17 - Create a random x coordinate
            0, number_of_cells - 1)

        y = random.randint(                         #3.18 - Create a random y coordinate
            0, number_of_cells - 1)

        position = Vector2(x, y)                    #3.19 - Create a Vector2 using the x and y coordinates
        
        return position                             #3.20 - Return the position

# pygame setup:
pygame.init()

screen = pygame.display.set_mode(                   #3.3 - Change the resolution to reflect the new grid-behavior; it is still 750 x 750
    (cell_size * number_of_cells, cell_size * number_of_cells))

pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True

food = Food()                                       #3.11 - Instantiate a new Food object
food_surface = pygame.image.load("food.png")        #3.13 - Give the Food object an image

# pygame "game loop:"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render Game
    screen.fill(GREEN)
    food.draw()                                     #3.12 - Draw the Food on the screen (Run #3)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

"""

Notes:
- For steps #3.1 to #3.3, explain how we're going to reinterpret the screen as a grid to make rendering easier 
- For steps #3.4 to #3.14, we will be creating a Food object, its constructor, and its graphics and rendering it onto the screen
- For steps #3.14 to #3.21, we will be making the Food object appear on random spots on the screen

"""