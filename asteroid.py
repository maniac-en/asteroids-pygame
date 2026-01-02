import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)  # get a random angle b/w 20 and 50
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid(self.position[0], self.position[-1], new_radius).velocity = (
            self.velocity.rotate(angle) * 1.2
        )
        Asteroid(self.position[0], self.position[-1], new_radius).velocity = (
            self.velocity.rotate(-angle) * 1.2
        )
