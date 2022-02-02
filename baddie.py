import pygame

class Baddie(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.y = 350
        self.hp = 500
        self.line = 0
        self.pause = 1
        baddie_img = pygame.image.load("sprites/baddie.png")
        lvl_1 = pygame.image.load("sprites/LEVEL_1.png")
            
    def X_RIGHT(self, limit, speed):
        if self.x <= limit:
            self.x += speed
        else:
            self.line += 1
            
    def X_LEFT(self, limit, speed):
        if self.x >= limit:
            self.x -= speed
        else:
            self.line += 1
            
    def Y_DOWN(self, limit, speed):
        if self.y <= limit:
            self.y += speed
        else:
            self.line += 1
            
    def Y_UP(self, limit, speed):
        if self.y >= limit:
            self.y -= speed
        else:
            self.line += 1