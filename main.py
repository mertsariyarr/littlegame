import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    #groups ----
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers(updatable, drawable, shots)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2) 
    dt = 0

    while True:
        for event in pygame.event.get(): #if user pushes close button on the screen it will stop the loop and close the window
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for object in asteroids:
            if object.collisions(player) == True:
                    print("Game over!")
                    sys.exit()

        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        
        pygame.display.flip()

        dt = clock.tick(60) / 1000 #limit the framerate to 60 fps


if __name__ == "__main__":
    main()