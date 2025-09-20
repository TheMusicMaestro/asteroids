import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Create the image for the asteroid
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius, width=2)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
