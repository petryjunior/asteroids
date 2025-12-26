import pygame
import sys
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for item in asteroids:
            for shot in shots:
                if item.collides_with(shot):
                    log_event("asteroid_shot")
                    item.split()
                    pygame.sprite.Sprite.kill(shot)
            if item.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
    

if __name__ == "__main__":
    main()
