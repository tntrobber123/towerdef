import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.y = 0
    def move_right(self):
        self.x += 50
    def move_left(self):
        self.x -= 50
    def move_up(self):
        self.y -= 50
    def move_down(self):
        self.y += 50