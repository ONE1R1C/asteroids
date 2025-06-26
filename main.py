import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

exit = False

def main():
    pygame.init()
    clock = pygame.time.Clock()

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Makes the screen black
        pygame.Surface.fill(screen, (0,0,0,))

        # Rotation of player
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
            

        # Player drawing
        for drawn in drawable:
            drawn.draw(screen)

        # Redrawing the screen
        pygame.display.flip()

        # Calculate Deltatime and limits to 60 fps
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
