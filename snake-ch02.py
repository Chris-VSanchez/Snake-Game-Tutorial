import pygame

# Color Palette
GREEN = 0xaacc60                                #2.13
DARK_GREEN = 0x2b3318                           #2.14

# pygame setup:
pygame.init()                                   #2.1 - Initialize pygame
screen = pygame.display.set_mode((750, 750))    #2.2 - Set the screen resolution
pygame.display.set_caption("Snake Game")        #2.3 - Title game window
clock = pygame.time.Clock()                     #2.4 - Set game clock
running = True                                  #2.5 - Meta game state

# pygame "game loop:"
while running:                                  #2.6 - Loop repeats while game is running
    for event in pygame.event.get():            #2.7 - Get every event that occurs in the game
        if event.type == pygame.QUIT:           #2.8 - If the user closes the window...
            running = False                     #2.9 - ...set running to false and exit the loop to exit the game
    
    # Render Game
    screen.fill(GREEN)                          #2.15 - Change the background color to GREEN (Run #2)

    pygame.display.update()                     #2.11 - Refresh the screen after every frame 
    clock.tick(60)                              #2.12 - Set FPS (Run #1)

pygame.quit()                                   #2.10

"""

Notes:
- For steps #2.1 to #2.5, explain how we initialize the library and the variables necessary for running the game on a screen
- For steps #2.6 to #2.12, go through the game loop pattern, explaining how we check for events and how we draw the game to the screen
- For steps #2.13 to #2.15, explain how we want to create a background color for the game, then show how we can apply that color to the screen
    * Note, the color can be in 3 forms: Hex - 0x......, RGB - (R, G, B), and Text - "color"

"""