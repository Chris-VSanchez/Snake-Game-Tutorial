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
    def __init__(self, snake_body):                                 #7.12 - Include snake_body as a parameter of the Food constructor
        self.position = self.generate_random_pos(snake_body)        #7.13 - Pass snake_body into generate_random_pos()

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        
        screen.blit(food_surface, food_rect)

    def generate_random_cell(self):                                 #7.6 - Rename the generate_random_pos function to generate_random_cell to make this logic easily repeatable
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)

        position = Vector2(x, y)
        
        return position

    def generate_random_pos(self, snake_body):                      #7.7 - Rewrite the generate_random_pos() method to account for the position of the Snake's body
        position = self.generate_random_cell()                      #7.8 - Set the Food's position to a random cell

        while position in snake_body:                               #7.9 - While the Food's position overlaps with the Snake's body...
            position = self.generate_random_cell()                  #7.10 - ...set the Food's position to another random cell

        return position                                             #7.11 - Return the position

# Create Snake class
class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]

        self.direction  = Vector2(1, 0)

    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)

            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

    def update(self):
        self.body = self.body[:-1]

        self.body.insert(0, self.body[0] + self.direction)

# Create Game class
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)                           #7.18 - Pass self.snake.body into the Food's constructor 

    def draw(self):
        self.snake.draw()
        self.food.draw()

    def update(self):
        self.snake.update()
        self.check_collision_with_food()                            #7.3 - Check this conditional with every Game update

    def check_collision_with_food(self):                            #7.1 - Method to check if the Snake's head has collided with the Food
        if self.snake.body[0] == self.food.position:                #7.2 - Check if the Snake's head is on the same cell as the Food
            # print("Eating Food")                                  #7.4 - Log the interaction in the console, then delete (Run #12)
            # self.food.position = self.food.generate_random_pos()  #7.5 Generate a new position for the Food (Run #13)
            self.food.position = self.food.generate_random_pos(     #7.19 Pass self.snake.body into generate_random_pos() (Run #14)
                self.snake.body)
            
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
- For steps #7.1 to #7.5, we program the interaction between the Snake's head and the Food to simulate the Snake "eating" the Food
- For steps #7.6 to #7.19, explain that there's a small chance that the Food could spawn on the Snake's head, so we have to change the way the Food spawns in

"""