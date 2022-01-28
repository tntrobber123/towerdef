import pygame
import baddie

class Tower(pygame.sprite.Sprite):
    def __init__(self):
        self.x =100
        self.y = 100
        self.speed = 1
        self.rng = 150
        self.dmg = 1