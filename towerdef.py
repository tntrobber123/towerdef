import pygame
import time
import random
import math
from player import Player
from baddie import Baddie
b = Baddie()
# Basic (basic towers)
from towers import Tower
t = Tower()
from towers2 import Tower2
t2 = Tower2()
from towers3 import Tower3
t3 = Tower3()
# Gatlings (speed towers)
from speedtwr import Speed
s = Speed()
from speedtwr2 import Speed2
s2 = Speed2()
from speedtwr3 import Speed3
s3 = Speed3()


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
    screen.blit(speed, (s.x, s.y))
    screen.blit(speed_range_ring, (s.x - 50, s.y - 50))
    screen.blit(speed, (s2.x, s2.y))
    screen.blit(speed_range_ring, (s2.x - 50, s2.y - 50))
    screen.blit(speed, (s3.x, s3.y))
    screen.blit(speed_range_ring, (s3.x - 50, s3.y - 50))
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
speed = pygame.image.load("sprites/speed.png")
speed_range_ring = pygame.image.load("sprites/speed_range_ring.png")
lvl = 0
screen.blit(lvl_1, (0, 0))
draw()
num_per_round = 3
watermelons = 25

def level_1():
    global num_per_round
    global watermelons
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
            
    if b.hp < 1:
        watermelons += 5
        if num_per_round >= 0:
            b.x = 0
            b.y = 350
            b.hp = 500
            b.line = 0
            num_per_round -= 1
            
        if num_per_round < 0:
            print("you win!")
            pygame.quit()
            quit()

def main():
    towernum = 0
    towersel = "basic"
    roundnum = 0

    def placetower():
        if towersel == "basic":
            if towernum == 0:
                t.x = p.x
                t.y = p.y
            if towernum == 1:
                t2.x = p.x
                t2.y = p.y
            if towernum == 2:
                t3.x = p.x
                t3.y = p.y
                
        if towersel == "speed":
            if towernum == 0:
                s.x = p.x
                s.y = p.y
        if towersel == "speed":
            if towernum == 1:
                s2.x = p.x
                s2.y = p.y
        if towersel == "speed":
            if towernum == 2:
                s3.x = p.x
                s3.y = p.y
        
    pygame.init()
    p = Player()
    done = False
        
    # Events go here:    
    while True:
        global num_per_round
        if towernum == 3:
            towernum = 0
        if b.pause == 0:
            level_1()
            
            
            # Basic tower code:
            dist = math.sqrt(((b.x + 25) - (t.x + 25))**2 + ((b.y + 25) - (t.y + 25))**2)
            dist2 = math.sqrt(((b.x + 25) - (t2.x + 25))**2 + ((b.y + 25) - (t2.y + 25))**2)
            dist3 = math.sqrt(((b.x + 25) - (t3.x + 25))**2 + ((b.y + 25) - (t3.y + 25))**2)
            dist -= 50
            dist2 -= 50
            dist3 -= 50
            
            if dist <= t.range:
                b.hp -= t.dmg
            if dist2 <= t2.range:
                b.hp -= t2.dmg
            if dist3 <= t3.range:
                b.hp -= t3.dmg
            
            speeddist = math.sqrt(((b.x + 25) - (s.x + 25))**2 + ((b.y + 25) - (s.y + 25))**2)
            speeddist2 = math.sqrt(((b.x + 25) - (s2.x + 25))**2 + ((b.y + 25) - (s2.y + 25))**2)
            speeddist3 = math.sqrt(((b.x + 25) - (s3.x + 25))**2 + ((b.y + 25) - (s3.y + 25))**2)

            speeddist -= 50
            speeddist2 -= 50
            speeddist3 -= 50
            
            if speeddist <= s.range:
                b.hp -= s.dmg
                print(b.hp)
            if speeddist2 <= s2.range:
                b.hp -= s2.dmg
                print(b.hp)
            if speeddist3 <= s3.range:
                b.hp -= s3.dmg
                print(b.hp)

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
                    
                if event.key == pygame.K_1:
                    towersel = "basic"
                    
                if event.key == pygame.K_2:
                    towersel = "speed"
                    
                if event.key == pygame.K_3:
                    towersel = "sniper"
                    
                    
    
main()