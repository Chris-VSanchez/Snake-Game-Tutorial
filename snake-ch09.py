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
    def __init__(self, snake_body):
        self.position = self.generate_random_pos(snake_body)

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        
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
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)

        if self.add_segment == True:
            self.add_segment = False

        else:
            self.body = self.body[:-1]

    def reset(self):                                                #9.8 - Method to reset the Snake's size, position, and direction
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]   #9.9 - Reset the Snake's size to 3 segments at the starting position
        
        self.direction  = Vector2(1, 0)                             #9.10 - Reset the Snake's direction to be facing right
        
# Create Game class
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.state = "RUNNING"                                      #9.12 - Create an internal Game state in the Game's constructor

    def draw(self):
        self.snake.draw()
        self.food.draw()

    def update(self):
        if self.state == "RUNNING":                                 #9.14 - Move all of the Game's updates inside an in-statement (Run #17)
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_edges()                       #9.4 - Check this conditional with every Game update
            self.check_collision_with_body()                        #9.21 - Check this conditional with every Game Update (Run #19)

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
           self.food.position = self.food.generate_random_pos(self.snake.body)
           self.snake.add_segment = True        

    def check_collision_with_edges(self):                           #9.1 - Method to check whether the Snake has gone out of bounds
        if( self.snake.body[0].x not in range(number_of_cells) or   #9.2 - If the Snake's head has collided with the borders...
            self.snake.body[0].y not in range(number_of_cells)):
            self.gameOver()                                         #9.3 - ...call Game Over method (Define game.gameOver next)

    def check_collision_with_body(self):                            #9.17 - Method to check whether the Snake has collided with itself
        body = self.snake.body[1:]                                  #9.18 - Define the Snake's body as every segment after the head

        if self.snake.body[0] in body:                              #9.19 - If the Snake's head touches its body...
            self.gameOver()                                         #9.20 - ...call Game Over method

    def gameOver(self):                                             #9.5 - Method to restart the game on Game Over
        # print("Game Over")                                        #9.6 - Log the interaction in the console, then delete (Run #16)
        self.snake.reset()                                          #9.7 - Reset the Snake's position (Define snake.reset next)
        self.food.position = self.food.generate_random_pos(         #9.11 - Spawn the food elsewhere
            self.snake.body)
        self.state = "STOPPED"                                      #9.13 - Change the Game's state so that it is paused on reset        
            
# pygame setup:
pygame.init()
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
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
            if game.state == "STOPPED":                             #9.15 - If the Game has ended...
                game.state = "RUNNING"                              #9.16 - ...press any key to restart (Run #18)

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
    game.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()

"""

Notes:
- For steps #9.1 to #9.6, we define a new method necessary for checking whether the Snake has left the playable area and create a new Game Over method
- For steps #9.7 to #9.10, we create a new method to reset the Snake's state to its initial state
- For steps #9.11 to #9.16, we finish the Game Over method and introduce an internal Game state that requires user input to start a new Game
- For steps #9.17 to #9.21, we define a new method necessary for checking whether the Snake has collided with itself and call the newely-created Game Over method

"""