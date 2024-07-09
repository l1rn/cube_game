import pygame
import sys
import os
from player import Player
from level import Level
from camera import Camera

# Инициализация Pygame
pygame.init()

# Настройка окна
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Моя Игра")

# Загрузка уровня
level_file_path = os.path.join('test_game','levels', 'level1.txt')
if not os.path.isfile(level_file_path):
    print(f"Error: Level file '{level_file_path}' not found.")
    sys.exit(1)

current_level = Level(level_file_path)

# Создание игрока
player = Player(current_level.spawn_point)

# Camera
camera = Camera(len(current_level.platforms) * 32, len(current_level.platforms)*32)

# Основной цикл игры
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление игрока и уровня
    player.update(current_level)
    current_level.update()

    # Обновление камеры
    camera.update(player)

    # Обновление экрана
    screen.fill((0, 0, 0))
    current_level.draw(screen)
    player.draw(screen)
    pygame.display.flip()

    # Установка FPS
    clock.tick(60)

pygame.quit()
sys.exit()
