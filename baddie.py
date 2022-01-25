import pygame

class Baddie(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.y = 350
        self.hp = 5
        self.line = 0
        baddie_img = pygame.image.load("sprites/baddie.png")
        lvl_1 = pygame.image.load("sprites/LEVEL_1.png")
            
    def X_RIGHT(self, limit, speed):
        while True:
            self.x += speed
            if self.x <= limit:
                self.line += 1

    def X_LEFT(self, limit, speed):
        while True:
            self.x -= speed
            if self.x >= limit:
                self.line += 1
                
    def Y_UP(self, limit, speed):
        while True:
            self.y -= speed
            if self.y >= limit:
                self.line += 1
                
    def Y_DOWN(self, limit, speed):
        while True:
            self.y += speed
            if self.y <= limit:
                self.line += 1