import pygame

class Baddie(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, x, y, time):
        pass
    # Need to make its x & y equal that of the array in towerdef.py... but how?