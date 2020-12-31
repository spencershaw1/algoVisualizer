import pygame
import random

# start up pygame and grab fonts
pygame.init()
pygame.font.init()

# set up screen dimensions
SCREENWIDTH = 1000
SCREENHEIGHT = 800

# initialize screen and caption
WINDOW = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
WINDOW.fill((0, 0, 0)) # black
pygame.display.set_caption("Python Algorithm Visualizer")



def main():
    # get font from pygame
    main_font = pygame.font.SysFont("arial", 50)

    # set up FPS
    FPS = 60
    clock = pygame.time.Clock()

    # create sorting buttons
    insertion_button = pygame.Rect(350, 75, 300, 100)
    selection_button = pygame.Rect(350, 185, 300, 100)
    merge_button = pygame.Rect(350, 295, 300, 100)
    heap_button = pygame.Rect(350, 405, 300, 100)
    quick_button = pygame.Rect(350, 515, 300, 100)
    shell_button = pygame.Rect(350, 625, 300, 100)


    # update display
    def redraw_window():

        # draw buttons
        pygame.draw.rect(WINDOW, (255, 255, 255), insertion_button)
        pygame.draw.rect(WINDOW, (255, 255, 255), selection_button)
        pygame.draw.rect(WINDOW, (255, 255, 255), merge_button)
        pygame.draw.rect(WINDOW, (255, 255, 255), heap_button)
        pygame.draw.rect(WINDOW, (255, 255, 255), quick_button)
        pygame.draw.rect(WINDOW, (255, 255, 255), shell_button)


        pygame.display.update()
    
    run = True
    # "game" loop
    while run:
        # ensure FPS
        clock.tick(FPS)

        # allow user to quit the visualizer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # store mouse position
                mouse_pos = event.pos

                # checks if mouse position is over the button
                if insertion_button.collidepoint(mouse_pos):
                    pass # do some stuff


        redraw_window()


main()