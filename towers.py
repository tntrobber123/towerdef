import pygame
from baddie import Baddie

b = Baddie()

class tower(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        self.rng = 0
        self.dmg = 0
    if b.pause == 1:
        print("pause")
        pass