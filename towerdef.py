import pygame
import time
import random
import math
import player
from player import Player
import baddie
from baddie import Baddie
b = Baddie()
import towers

from towers import Tower
t = Tower()
import towers2

from towers2 import Tower2
t2 = Tower2()
import towers3

from towers3 import Tower3
t3 = Tower3()

def draw():
    pygame.display.flip()
    
def draw_plr(p):
    screen.blit(lvl_1, (0, 0))
    screen.blit(player_img, (p.x, p.y))
    pygame.display.flip()
    
def draw_lvl1():
    screen.blit(lvl_1, (0, 0))
    pygame.display.flip()

def draw_baddie():
    screen.blit(lvl_1, (0, 0))
    screen.blit(baddie_img, (b.x, b.y))
    pygame.display.flip()

def draw_all(p):
    screen.blit(lvl_1, (0, 0))
    screen.blit(basetower_img, (t.x, t.y))
    screen.blit(basic_range_ring_img, (t.x - 125, t.y - 125))
    screen.blit(basetower_img, (t2.x, t2.y))
    screen.blit(basic_range_ring_img, (t2.x - 125, t2.y - 125))
    screen.blit(basetower_img, (t3.x, t3.y))
    screen.blit(basic_range_ring_img, (t3.x - 125, t3.y - 125))
    screen.blit(baddie_img, (b.x, b.y))
    screen.blit(player_img, (p.x, p.y))
    pygame.display.flip()

# Load in all the code for images and stuff
black = (0, 0, 0)
white = (255, 255, 255)
size = [750, 500]
screen = pygame.display.set_mode(size)
basic_range_ring_img = pygame.image.load("sprites/basic_range_ring.png")
player_img = pygame.image.load("sprites/cursor.png")
baddie_img = pygame.image.load("sprites/baddie.png")
basetower_img = pygame.image.load("sprites/basic.png")
lvl_1 = pygame.image.load("sprites/LEVEL_1.png")
gam3over = pygame.image.load("sprites/gameov3r.png")
lvl = 0
screen.blit(lvl_1, (0, 0))
draw()
num_per_round = 3


def level_1():
    if b.hp > 0:
        if b.line == 0:
            b.X_RIGHT(200, 5)
        if b.line == 1:
            b.Y_UP(150, 5)
        if b.line == 2:
            b.X_LEFT(50, 5)
        if b.line == 3:
            b.Y_UP(50, 5)
        if b.line == 4:
            b.X_RIGHT(400, 5)
        if b.line == 5:
            b.Y_DOWN(400, 5)
        if b.line == 6:
            b.X_RIGHT(450, 5)
            b.line = 42
                    
        if b.line == 42:
            screen.blit(gam3over, (0, 0))  
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
            quit()

def main():
    towernum = 0
    roundnum = 0

    def placetower():
        if towernum == 0:
            t.x = p.x
            t.y = p.y
        if towernum == 1:
            t2.x = p.x
            t2.y = p.y
        if towernum == 2:
            t3.x = p.x
            t3.y = p.y
        
    pygame.init()
    p = Player()
    done = False
        
    # Events go here:    
    while True:
        global num_per_round
        if towernum == 3:
            towernum = 0
        if b.pause == 0:
            # Baddie code
            if b.hp < 0:
                if num_per_round > 0:
                    b.x = 0
                    b.y = 350
                    b.line = 0
                    num_per_round -= 1
                    
            # Tower code:
            dist = math.sqrt(((b.x + 25) - (t.x + 25))**2 + ((b.y + 25) - (t.y + 25))**2)
            dist2 = math.sqrt(((b.x + 25) - (t2.x + 25))**2 + ((b.y + 25) - (t2.y + 25))**2)
            dist3 = math.sqrt(((b.x + 25) - (t3.x + 25))**2 + ((b.y + 25) - (t3.y + 25))**2)
            dist -= 50
            if dist <= t.range:
                b.hp -= t.dmg
            if dist2 <= t2.range:
                b.hp -= t2.dmg
            if dist3 <= t3.range:
                b.hp -= t3.dmg
            # Baddie code:
            
        if p.x <= 0:
            p.x = 0
        if p.x >= 700:
            p.x = 700
        if p.y <= 0:
            p.y = 0
        if p.y >= 450:
            p.y = 450
        
        draw_all(p)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RIGHT:
                    p.move_right()
                    draw_lvl1()
                    screen.blit(player_img, (p.x, p.y))
                    draw()
                if event.key == pygame.K_LEFT:
                    p.move_left()
                    draw_lvl1()
                    screen.blit(player_img, (p.x, p.y))
                    draw()
                if event.key == pygame.K_UP:
                    p.move_up()
                    draw_lvl1()
                    screen.blit(player_img, (p.x, p.y))
                    draw()
                if event.key == pygame.K_DOWN:
                    p.move_down()
                    draw_lvl1()
                    screen.blit(player_img, (p.x, p.y))
                    draw()
                if event.key == pygame.K_RETURN:
                    if b.pause == 1:
                        b.pause = 0
                    else:
                        b.pause = 1
                    
                if event.key == pygame.K_SPACE:
                    placetower()
                    towernum += 1
                    
                    
    
main()