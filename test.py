# this is madde by ai and i was trying to make a copy like this but was not able to make it bc my motivation just fell off
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 900, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enemy Chase")

clock = pygame.time.Clock()

# Colors
WHITE = (245, 245, 245)
RED = (220, 70, 70)
GREEN = (70, 200, 70)
BLACK = (20, 20, 20)


class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, 40, 40)
        self.speed = 5
        self.health = 5

    def move(self):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_a]:
            dx -= self.speed

        if keys[pygame.K_d]:
            dx += self.speed

        if keys[pygame.K_w]:
            dy -= self.speed

        if keys[pygame.K_s]:
            dy += self.speed

        self.rect.x += dx
        self.rect.y += dy

        self.rect.clamp_ip(screen.get_rect())

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, self.rect)


class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT),
            30,
            30
        )

        self.speed = random.randint(2, 4)

    def update(self, player):

        if self.rect.centerx < player.rect.centerx:
            self.rect.x += self.speed
        elif self.rect.centerx > player.rect.centerx:
            self.rect.x -= self.speed

        if self.rect.centery < player.rect.centery:
            self.rect.y += self.speed
        elif self.rect.centery > player.rect.centery:
            self.rect.y -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)


class Game:

    def __init__(self):

        self.player = Player()

        self.enemies = []

        self.spawn_timer = 0

        self.font = pygame.font.SysFont(None, 30)

        self.running = True

    def spawn_enemy(self):
        self.enemies.append(Enemy())

    def update(self):

        self.player.move()

        self.spawn_timer += 1

        if self.spawn_timer >= 90:
            self.spawn_enemy()
            self.spawn_timer = 0

        for enemy in self.enemies:

            enemy.update(self.player)

            if enemy.rect.colliderect(self.player.rect):

                self.player.health -= 1

                enemy.rect.x = random.randint(0, WIDTH)
                enemy.rect.y = random.randint(0, HEIGHT)

        if self.player.health <= 0:
            self.running = False

    def draw(self):

        screen.fill(WHITE)

        self.player.draw(screen)

        for enemy in self.enemies:
            enemy.draw(screen)

        health = self.font.render(
            f"Health: {self.player.health}",
            True,
            BLACK
        )

        enemies = self.font.render(
            f"Enemies: {len(self.enemies)}",
            True,
            BLACK
        )

        screen.blit(health, (20, 20))
        screen.blit(enemies, (20, 60))

        pygame.display.flip()

    def run(self):

        while self.running:

            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.draw()


game = Game()
game.run()

pygame.quit()
