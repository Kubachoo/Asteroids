import pygame
import sys
from constants import *
from player import*
from asteroid import*
from asteroidfield import*

def main():
    # initilizes pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # These are all the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Adds Player & Asteroid to thier respected groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroid = AsteroidField()
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        for object in updatable:
            object.update(dt)
        
        for asteroid in asteroids:
            for bullet in shots:
                if(asteroid.collisionCheck(bullet)):
                    asteroid.split()
                    bullet.kill()

        for asteroid in asteroids:
            if(asteroid.collisionCheck(player)):
                print("Game Over!")
                sys.exit()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        # Limits frame rate to 60 fps
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
