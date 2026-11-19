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

        self.direction  = Vector2(1, 0)         #6.1 - Create a direction for the Snake to move in (Express it as a Vector2 going to the right by 1 unit)

    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)

            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

    def update(self):                           #6.2 - Update method for Snake class, will update the Snake's position
        self.body = self.body[:-1]              #6.3 - Select every segment of the Snake's head except for the last one

        self.body.insert(                       #6.4 - Insert a segment at the front of the Snake to simulate motion in the given direction
            0, self.body[0] + self.direction)

# Create Game class
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def draw(self):
        self.snake.draw()
        self.food.draw()

    def update(self):
        self.snake.update()

# pygame setup:
pygame.init()
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True

food_surface = pygame.image.load("food.png")

SNAKE_UPDATE = pygame.USEREVENT                 #6.6 - Use USEREVENT to create a custom event for the Snake's state update
pygame.time.set_timer(SNAKE_UPDATE, 200)        #6.7 - Set the Snake to move in its current direction once every 200ms

game = Game()

# pygame "game loop:"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SNAKE_UPDATE:          #6.8 - Check if the Snake's state has updated
            game.update()                       #6.9 - Update the Game's state to reflect the Snake's slower movement (Run #10)

        # Keyboard Controls:
        if event.type == pygame.KEYDOWN:        #6.10 to #6.18 - Define keyboard controls for the Game (Run #11)
            if event.key in {pygame.K_UP, pygame.K_w} and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)               # Move Snake UP if not moving down
            
            elif event.key in {pygame.K_DOWN, pygame.K_s} and game.snake.direction != Vector2(0, -1): 
                game.snake.direction = Vector2(0, 1)                # Move Snake DOWN if not moving up

            elif event.key in {pygame.K_LEFT, pygame.K_a} and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)               # Move Snake LEFT if not moving right

            elif event.key in {pygame.K_RIGHT, pygame.K_d} and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)                # Move Snake RIGHT if not moving left

    # game.update()                             #6.5 - Run game.update() to show that the Snake is moving too fast, then delete (Run #9)

    # Render Game
    screen.fill(GREEN)
    game.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()

"""

Notes:
- For steps #6.1 to #6.5, we give the Snake a direction and an Update method to simulate movement in a given direction; it will move too fast at this point
- For steps #6.6 to #6.9, we set the Snake to move at a given speed so that the Snake's update is not tied to the Game's FPS
- For steps #6.10 to #6.18, we define keyboard controls for the game (WASD and UP, DOWN, LEFT, and RIGHT)

"""