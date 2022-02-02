import pygame

class Speed2(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 1000
        self.y = 1000
        self.range = 50
        self.dmg = 15