import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):

        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4 , 12)
        self.color = 245, 200, 111
        self.speed = 18
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect. top
        self.y = float(self.rect.y)

    def update(self):
        """  перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """рисуем пулюб на кране """
        pygame.draw.rect(self.screen, self.color, self.rect)