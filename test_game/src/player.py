import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Player, self).__init__()
        self.image = pygame.Surface((32, 32))  # Размер игрока 32x32
        self.image.fill((0, 255, 0))  # Зеленый цвет для игрока
        self.rect = self.image.get_rect(topleft=position)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.5
        self.jump_strength = -10

    def update(self, level):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        else:
            self.velocity.x = 0

        if keys[pygame.K_SPACE] and self.on_ground(level):
            self.velocity.y = self.jump_strength

        self.apply_gravity()
        self.rect.x += self.velocity.x
        self.check_collisions(level, 'horizontal')
        self.rect.y += self.velocity.y
        self.check_collisions(level, 'vertical')

    def apply_gravity(self):
        self.velocity.y += self.gravity

    def on_ground(self, level):
        self.rect.y += 1
        collisions = pygame.sprite.spritecollide(self, level.platforms, False)
        self.rect.y -= 1
        return bool(collisions)

    def check_collisions(self, level, direction):
        collisions = pygame.sprite.spritecollide(self, level.platforms, False)
        for platform in collisions:
            if direction == 'horizontal':
                if self.velocity.x > 0:
                    self.rect.right = platform.rect.left
                elif self.velocity.x < 0:
                    self.rect.left = platform.rect.right
                self.velocity.x = 0
            elif direction == 'vertical':
                if self.velocity.y > 0:
                    self.rect.bottom = platform.rect.top
                elif self.velocity.y < 0:
                    self.rect.top = platform.rect.bottom
                self.velocity.y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
