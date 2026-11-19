import pygame
from pygame.math import Vector2
import random

# Color Palette
GREEN = 0xaacc60
DARK_GREEN = 0x2b3318

# Grid Layout
cell_size = 30
number_of_cells = 25

# Create Food class:
class Food:
    def __init__(self):
        self.position = self.generate_random_pos()

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        
        screen.blit(food_surface, food_rect)

    def generate_random_pos(self):
        x = random.randint(0, number_of_cells - 1) 
        y = random.randint(0, number_of_cells - 1)

        position = Vector2(x, y)
        
        return position

# Create Snake class
class Snake:                                    #4.1 - Snake class definition
    def __init__(self):                         #4.2 - Snake constructor
        self.body = [                           #4.3 - Initialize the Snake as a list of 3 objects [head, tail, tail, ...]
            Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]

    def draw(self):                             #4.4 - Draw method for Snake class, will draw every segment of the Snake on screen
        for segment in self.body:               #4.5 - For every segment of the Snake...
            segment_rect = (                    #4.6 - ...define a rectangular area with position (x, y) and dimensions (cell_size, cell_size) and...
                segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)

            # pygame.draw.rect(                 #4.7 - ...draw a DARK_GREEN rectangle on the screen with the area defined by food_rect
                # screen, DARK_GREEN, segment_rect)
            
            pygame.draw.rect(                   #4.10 - Change line #4.7 to give the Snake rounded segments to make each segment visible (Run #7)
                screen, DARK_GREEN, segment_rect, 0, 7)

# pygame setup:
pygame.init()
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True

food = Food()
food_surface = pygame.image.load("food.png")

snake = Snake()                                 #4.8 - Instantiate a new Snake object

# pygame "game loop:"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render Game
    screen.fill(GREEN)
    food.draw()
    snake.draw()                                #4.9 - Draw the Snake on the screen (Run #6)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

"""

Notes:
- For steps #4.1 to #4.10, we will be creating a Snake object, its constructor, and its graphics and rendering it on the screen
    * Note, Snake can be colored differently by matching segments to snake.body indices

"""