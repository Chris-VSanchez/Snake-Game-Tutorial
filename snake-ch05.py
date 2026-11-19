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
class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]

    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)

            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

# Create Game class
class Game:                                     #5.1 - Game class definition
    def __init__(self):                         #5.2 - Game constructor
        self.snake = Snake()                    #5.3 - Instantiate a new Snake object within Game object
        self.food = Food()                      #5.4 - Instantiate a new Food object within Game object

    def draw(self):                             #5.5 - Draw the Game objects on screen
        self.snake.draw()                       #5.6 - Draw the Snake on screen
        self.food.draw()                        #5.7 - Draw the Food on screen

    def update(self):                           #5.8 - Update Game state
        self.snake.update()                     #5.9 - Update Snake position (Define snake.update later)

# pygame setup:
pygame.init()
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True

# food = Food()
food_surface = pygame.image.load("food.png")

# snake = Snake()

game = Game()                                   #5.10 - Instantiate a Game object and delete the instances of Snake and Food

# pygame "game loop:"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render Game
    screen.fill(GREEN)
    # food.draw()
    # snake.draw()
    game.draw()                                 #5.11 - Draw the Game to the screen and delete the old Snake and Food draws (Run #8)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

"""

Notes:
- For steps #5.1 to 5.11, explain how it's good practice to centralize game logic by creating Game class. Delete all instances of Snake and Food and replace with Game
    * Creating the Game class now will save a lot of rewriting for the next part

"""