import pygame

class Sniper(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 1000
        self.y = 1000
        self.range = 500
        self.dmg = 1