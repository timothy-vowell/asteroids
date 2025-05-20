import pygame

from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # our game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # screen.fill("black") - in the solution file
        pygame.Surface.fill(screen, color="black")
        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()