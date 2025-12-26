from circleshape import CircleShape
from constants import *
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            new_vec1 = self.velocity.rotate(random_angle)
            new_vec2 = self.velocity.rotate(random_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            smol_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            smol_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            smol_asteroid1.velocity = new_vec1 * 1.2
            smol_asteroid2.velocity = new_vec2 * 1.2


        