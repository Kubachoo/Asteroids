import pygame
from constants import *
from player import*

def main():
    # initilizes pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # These are all the objects that can be updated
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Adds Player to both groups
    Player.containers = (updatable, drawable)

    player = Player(x, y)


    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        for object in updatable:
            object.update(dt)

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        # Limits frame rate to 60 fps
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
