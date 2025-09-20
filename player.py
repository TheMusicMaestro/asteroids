import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        # Create the original image with the triangle pointing down
        size = self.radius * 2
        self.original_image = pygame.Surface((size, size), pygame.SRCALPHA)
        center = pygame.Vector2(self.radius, self.radius)

        # Triangle points relative to the center, pointing down
        forward = pygame.Vector2(0, 1)
        right = forward.rotate(90) * self.radius / 1.5
        a = forward * self.radius
        b = -forward * self.radius - right
        c = -forward * self.radius + right
        points = [a + center, b + center, c + center]

        pygame.draw.polygon(self.original_image, (255, 255, 255), points, width=2)

        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Rotate the image and update the rect
        self.image = pygame.transform.rotate(self.original_image, -self.rotation)
        self.rect = self.image.get_rect(center=self.position)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
