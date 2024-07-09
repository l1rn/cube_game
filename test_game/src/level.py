import pygame
from platform import Platform
import os


class Level:
    def __init__(self, level_file):
        self.platforms = pygame.sprite.Group()
        self.spawn_point = (0, 0)  # Инициализация значения по умолчанию
        self.load_level(level_file)

    def load_level(self, level_file):
        if not os.path.isfile(level_file):
            raise FileNotFoundError(f"Level file '{level_file}' not found.")

        with open(level_file, 'r') as file:
            lines = file.readlines()
            for y, line in enumerate(lines):
                for x, char in enumerate(line.strip()):  # Убираем новые строки
                    if char == 'P':
                        platform = Platform((x * 32, y * 32))
                        self.platforms.add(platform)
                    elif char == 'S':
                        self.spawn_point = (x * 32, y * 32)

    def update(self):
        self.platforms.update()

    def draw(self, screen):
        self.platforms.draw(screen)
