import pygame

class Tower(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 1000
        self.y = 1000
        self.range = 150
        self.dmg = 50