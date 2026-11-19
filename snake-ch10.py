import pygame
from pygame.math import Vector2
import random

import ctypes                                   #10.1 - Import ctypes so that the game window does not scale
ctypes.windll.user32.SetProcessDPIAware()       #10.2 - Set the window to be aware of DPI-scaling and adjust accordingly

# Color Palette
GREEN = 0xaacc60
DARK_GREEN = 0x2b3318

# Grid Layout
cell_size = 30
number_of_cells = 25

# Border Layout
OFFSET = 75                                     #10.3 - Determine the width of the Game's border

# Create Food class:
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_random_pos(snake_body)

    def draw(self):
        food_rect = pygame.Rect(                #10.6 - Include the Game's border in the Food's draw calculation
            OFFSET + self.position.x * cell_size, OFFSET + self.position.y * cell_size, cell_size, cell_size)
        
        screen.blit(food_surface, food_rect)

    def generate_random_cell(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)

        position = Vector2(x, y)

        return position

    def generate_random_pos(self, snake_body):
        position = self.generate_random_cell()

        while position in snake_body:
            position = self.generate_random_cell()

        return position

# Create Snake class
class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]

        self.direction  = Vector2(1, 0)

        self.add_segment = False

    def draw(self):
        for segment in self.body:
            segment_rect = (                    #10.7 - Include the Game's border in the Snake's draw calculation (Run #21)
                OFFSET + segment.x * cell_size, OFFSET + segment.y * cell_size, cell_size, cell_size)
            
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)

        if self.add_segment == True:
            self.add_segment = False

        else:
            self.body = self.body[:-1]

    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        
        self.direction  = Vector2(1, 0)
        
# Create Game class
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.state = "RUNNING"

    def draw(self):
        self.snake.draw()
        self.food.draw()

    def update(self):
        if self.state == "RUNNING":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_edges()
            self.check_collision_with_body()

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
           self.food.position = self.food.generate_random_pos(self.snake.body)
           self.snake.add_segment = True        

    def check_collision_with_edges(self):
        if self.snake.body[0].x not in range(number_of_cells) or self.snake.body[0].y not in range(number_of_cells):
            self.gameOver()

    def check_collision_with_body(self):
        body = self.snake.body[1:]

        if self.snake.body[0] in body:
            self.gameOver()

    def gameOver(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "STOPPED"
            
# pygame setup:
pygame.init()

screen = pygame.display.set_mode(               #10.4 - Add the border size to each side of the screen's area
    (2 * OFFSET + cell_size * number_of_cells, 2 * OFFSET + cell_size * number_of_cells))

pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True

food_surface = pygame.image.load("food.png")

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

game = Game()

# pygame "game loop:"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SNAKE_UPDATE:
            game.update()

        # Keyboard Controls:
        if event.type == pygame.KEYDOWN:
            if game.state == "STOPPED":
                game.state = "RUNNING"

            if event.key in {pygame.K_UP, pygame.K_w} and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            
            elif event.key in {pygame.K_DOWN, pygame.K_s} and game.snake.direction != Vector2(0, -1): 
                game.snake.direction = Vector2(0, 1)

            elif event.key in {pygame.K_LEFT, pygame.K_a} and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)

            elif event.key in {pygame.K_RIGHT, pygame.K_d} and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)

    # Render Game
    screen.fill(GREEN)
    
    pygame.draw.rect(                           #10.5 - Draw a 5-pixel border around the Game's playable area (Run #20)
        screen, DARK_GREEN, (OFFSET - 5, OFFSET - 5, cell_size * number_of_cells + 10, cell_size * number_of_cells + 10), 5)
    
    game.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()

"""

Notes:
- For steps #10.1 to #10.2, import ctypes to avoid the Game's window being bigger than the monitor / screen size
- For steps #10.3 to #10.7, define the border size, create a visible border around the Game, and adjust draw calculations with the border in mind

"""