import pygame

class Sniper2(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 1000
        self.y = 1000
        self.range = 999
        self.dmg = 1