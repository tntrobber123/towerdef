import pygame

class Tower2(pygame.sprite.Sprite):
    def __init__(self):
        self.x =100
        self.y = 100
        self.speed = 1
        self.range = 150
        self.dmg = 1