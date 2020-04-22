import pygame

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        self.velocity = 1
        super().__init__()
        self.image = pygame.image.load("images/redcar.jpg")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y


    def move_down(self):
        self.rect.y += self.velocity