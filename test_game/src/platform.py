import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Platform, self).__init__()
        self.image = pygame.Surface((32, 32))  # Предполагаем размер платформы 32x32
        self.image.fill((255, 255, 255))  # Заполняем белым цветом (или используйте загрузку изображения)
        self.rect = self.image.get_rect(topleft=position)
