import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Create the image for the asteroid
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        center = (int(self.radius), int(self.radius))
        pygame.draw.circle(self.image, (255, 255, 255), center, int(self.radius), width=2)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_vel1 = self.velocity.rotate(random_angle)
        new_vel2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vel1 * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_vel2 * 1.2
