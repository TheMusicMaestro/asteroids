import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_LIFETIME

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.lifetime = SHOT_LIFETIME

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        center = (self.radius, self.radius)
        pygame.draw.circle(self.image, (255, 255, 255), center, int(self.radius))
        self.rect = self.image.get_rect(center=(x,y))

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
        self.lifetime -= dt
        if self.lifetime < 0:
            self.kill()
