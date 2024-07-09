import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        x = min(0, x) # left
        y = (0, y) # top
        x = max(-(self.width - 1920), x)
        y = max(-(self.height - 1080), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)