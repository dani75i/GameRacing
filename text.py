import pygame


class Text:

    def __init__(self):
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.message = ''
        self.text = self.font.render(self.message, True, self.green, self.blue)
        self.textRect = self.text.get_rect()
        self.textRect.center = (170, 350)

    def start_message(self):
        self.message = "CLICK SPACE!"
        self.text = self.font.render(self.message, True, self.green, self.blue)
        return self.text

    def end_message(self):
        self.message = "GAME OVER"
        self.text = self.font.render(self.message, True, self.green, self.blue)
        return self.text

    def win_message(self):
        self.message = "You WIN !!!"
        self.text = self.font.render(self.message, True, self.green, self.blue)
        return self.text

    def time_message(self, time):
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.message = time
        self.textRect.center = (470, 50)
        self.text = self.font.render(self.message, True, self.black, self.white)
        return self.text
