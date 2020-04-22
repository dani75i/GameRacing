import pygame

class Car(pygame.sprite.Sprite):

    def __init__(self):
        self.velocity = 5
        super().__init__()
        self.image = pygame.image.load("images/voiture.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.x = 340
        self.rect.y = 650

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
