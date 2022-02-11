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

# Snipers (range towers)
from sniper import Sniper
r = Sniper()
from sniper2 import Sniper2
r2 = Sniper2()
from sniper3 import Sniper3
r3 = Sniper3()

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

frames_t = 0
frames_t2 = 0
frames_t3 = 0
def basic_frames():
    global frames_t
    global frames_t2
    global frames_t3
    if frames_t < 3:
        screen.blit(basic, (t.x, t.y))
    if frames_t > 3 and frames_t < 6:
        screen.blit(basic2, (t.x, t.y))
    if frames_t > 6 and frames_t < 9:
        screen.blit(basic3, (t.x, t.y))
    if frames_t > 9 and frames_t < 12:
        screen.blit(basic4, (t.x, t.y))
    if frames_t > 12 and frames_t < 15:
        screen.blit(basic5, (t.x, t.y))
    if frames_t > 15 and frames_t < 18:
        screen.blit(basic6, (t.x, t.y))
    if frames_t > 18 and frames_t < 21:
        screen.blit(basic7, (t.x, t.y))
    if frames_t > 21 and frames_t < 24:
        screen.blit(basic8, (t.x, t.y))
    if frames_t > 24 and frames_t < 27:
        screen.blit(basic9, (t.x, t.y))
    if frames_t > 27:
        screen.blit(basic10, (t.x, t.y))
        
    if frames_t2 < 3:
        screen.blit(basic, (t2.x, t2.y))
    if frames_t2 > 3 and frames_t2 < 6:
        screen.blit(basic2, (t2.x, t2.y))
    if frames_t2 > 6 and frames_t2 < 9:
        screen.blit(basic3, (t2.x, t2.y))
    if frames_t2 > 9 and frames_t2 < 12:
        screen.blit(basic4, (t2.x, t2.y))
    if frames_t2 > 12 and frames_t2 < 15:
        screen.blit(basic5, (t2.x, t2.y))
    if frames_t2 > 15 and frames_t2 < 18:
        screen.blit(basic6, (t2.x, t2.y))
    if frames_t2 > 18 and frames_t2 < 21:
        screen.blit(basic7, (t2.x, t2.y))
    if frames_t2 > 21 and frames_t2 < 24:
        screen.blit(basic8, (t2.x, t2.y))
    if frames_t2 > 24 and frames_t2 < 27:
        screen.blit(basic9, (t2.x, t2.y))
    if frames_t2 > 27:
        screen.blit(basic10, (t2.x, t2.y))
        
    if frames_t3 < 3:
        screen.blit(basic, (t3.x, t3.y))
    if frames_t3 > 3 and frames_t3 < 6:
        screen.blit(basic2, (t3.x, t3.y))
    if frames_t3 > 6 and frames_t3 < 9:
        screen.blit(basic3, (t3.x, t3.y))
    if frames_t3 > 9 and frames_t3 < 12:
        screen.blit(basic4, (t3.x, t3.y))
    if frames_t3 > 12 and frames_t3 < 15:
        screen.blit(basic5, (t3.x, t3.y))
    if frames_t3 > 15 and frames_t3 < 18:
        screen.blit(basic6, (t3.x, t3.y))
    if frames_t3 > 18 and frames_t3 < 21:
        screen.blit(basic7, (t3.x, t3.y))
    if frames_t3 > 21 and frames_t3 < 24:
        screen.blit(basic8, (t3.x, t3.y))
    if frames_t3 > 24 and frames_t3 < 27:
        screen.blit(basic9, (t3.x, t3.y))
    if frames_t3 > 27:
        screen.blit(basic10, (t3.x, t3.y))
    
    screen.blit(basic_range_ring_img, (t.x - 125, t.y - 125))
    screen.blit(basic_range_ring_img, (t2.x - 125, t2.y - 125))
    screen.blit(basic_range_ring_img, (t3.x - 125, t3.y - 125))

def draw_all(p):
    global frame_s
    global frame_s2
    global frame_s3
    screen.blit(lvl_1, (0, 0))
    
    if frame_s < 4:
        screen.blit(speed, (s.x, s.y))
    if frame_s >= 4:
        screen.blit(speed2, (s.x, s.y))
    screen.blit(speed_range_ring, (s.x - 50, s.y - 50))
    
    if frame_s2 < 4:
        screen.blit(speed, (s2.x, s2.y))
    if frame_s2 >= 4:
        screen.blit(speed2, (s2.x, s2.y))
    screen.blit(speed_range_ring, (s2.x - 50, s2.y - 50))
    
    if frame_s3 < 4:
        screen.blit(speed, (s3.x, s3.y))
    if frame_s3 >= 4:
        screen.blit(speed2, (s3.x, s3.y))
    screen.blit(speed_range_ring, (s3.x - 50, s3.y - 50))
    
    basic_frames()
    screen.blit(sniper, (r.x, r.y))
    screen.blit(sniper, (r2.x, r2.y))
    screen.blit(sniper, (r3.x, r3.y))
    if bosses == False:
        screen.blit(baddie_img, (b.x, b.y))
    if bosses == True:
        screen.blit(boss, (b.x, b.y))
    displaynum = font.render(str(watermelons), 1, white)
    screen.blit(displaynum, (560, 100))
    pygame.display.flip
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

basic = pygame.image.load("sprites/basic/basic.png")
basic2 = pygame.image.load("sprites/basic/basic2.png")
basic3 = pygame.image.load("sprites/basic/basic3.png")
basic4 = pygame.image.load("sprites/basic/basic4.png")
basic5 = pygame.image.load("sprites/basic/basic5.png")
basic6 = pygame.image.load("sprites/basic/basic6.png")
basic7 = pygame.image.load("sprites/basic/basic7.png")
basic8 = pygame.image.load("sprites/basic/basic8.png")
basic9 = pygame.image.load("sprites/basic/basic9.png")
basic10 = pygame.image.load("sprites/basic/basic10.png")

lvl_1 = pygame.image.load("sprites/LEVEL_1.png")
gam3over = pygame.image.load("sprites/gameov3r.png")
speed = pygame.image.load("sprites/speed.png")
speed2 = pygame.image.load("sprites/speed2.png")
speed_range_ring = pygame.image.load("sprites/speed_range_ring.png")
boss = pygame.image.load("sprites/boss.png")
sniper = pygame.image.load("sprites/heavy.png")

# Vars:
lvl = 0
screen.blit(lvl_1, (0, 0))
draw()
num_per_round = 2
watermelons = 30
rnd = 0
bosses = False
frame_s = 1
frame_s2 = 1
frame_s3 = 1
pygame.init()
font = pygame.font.SysFont("Times New Roman", 25)

def level_1():
    global rnd
    global num_per_round
    global watermelons
    global boss
    if b.hp > 0:
        if b.line == 0:
            b.X_RIGHT(200, 2.5)
        if b.line == 1:
            b.Y_UP(150, 2.5)
        if b.line == 2:
            b.X_LEFT(50, 2.5)
        if b.line == 3:
            b.Y_UP(50, 2.5)
        if b.line == 4:
            b.X_RIGHT(400, 2.5)
        if b.line == 5:
            b.Y_DOWN(400, 2.5)
        if b.line == 6:
            b.X_RIGHT(450, 2.5)
            b.line = 42
                    
        if b.line == 42:
            screen.blit(gam3over, (0, 0))  
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
            quit()
            
    if b.hp < 1:
        watermelons += 5
        b.hp_mod += .5
        print("you have", watermelons, "watermelons!")
        if num_per_round >= 0:
            b.x = 0
            b.y = 350
            b.hp = b.def_hp * b.hp_mod
            b.line = 0
            num_per_round -= 1
        
        if num_per_round == 0:
            
            if rnd == 3:
                bosses = False
                b.x = 0
                b.y = 350
                num_per_round = 1
                watermelons += 150
                b.pause = 1
                b.line = 0
                b.hp = 50000
                rnd = 999
            
            if rnd == 2:
                bosses = True
                b.x = 0
                b.y = 350
                num_per_round = 1
                watermelons += 100
                b.pause = 1
                b.line = 0
                b.hp = 50000
                rnd = 3
                
            if rnd == 1:
                b.x = 0
                b.y = 350
                num_per_round = 2
                watermelons += 100
                b.pause = 1
                b.hp = 450
                b.hp_mod += .25
                b.line = 0
                rnd = 2
            
            if rnd == 0:
                num_per_round = 5
                watermelons += 50
                b.hp = 450
                b.pause = 1
                b.line = 0
                rnd = 1
                
            if rnd == 999:
                print("You Win!")
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
            if towernum == 1:
                s2.x = p.x
                s2.y = p.y
            if towernum == 2:
                s3.x = p.x
                s3.y = p.y
        
        if towersel == "sniper":
            if towernum == 0:
                r.x = p.x
                r.y = p.y
            if towernum == 1:
                r2.x = p.x
                r2.y = p.y
            if towernum == 2:
                r3.x = p.x
                r3.y = p.y
                
    p = Player()
    done = False
        
    # Event loop:
    while True:
        global num_per_round
        global watermelons
        
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
            
            global frames_t
            global frames_t2
            global frames_t3
            
            if dist <= t.range:
                b.hp -= t.dmg
                frames_t += 1
            if dist2 <= t2.range:
                b.hp -= t2.dmg
                frames_t2 += 1
            if dist3 <= t3.range:
                b.hp -= t3.dmg
                frames_t3 += 1
                
            if dist > t.range:
                frames_t = 0
            if dist2 > t2.range:
                frames_t2 = 0
            if dist3 > t3.range:
                frames_t3 = 0
            
            if frames_t == 35:
                frames_t = 0
            if frames_t2 == 35:
                frames_t2 = 0
            if frames_t3 == 35:
                frames_t3 = 0
            
            speeddist = math.sqrt(((b.x + 25) - (s.x + 25))**2 + ((b.y + 25) - (s.y + 25))**2)
            speeddist2 = math.sqrt(((b.x + 25) - (s2.x + 25))**2 + ((b.y + 25) - (s2.y + 25))**2)
            speeddist3 = math.sqrt(((b.x + 25) - (s3.x + 25))**2 + ((b.y + 25) - (s3.y + 25))**2)

            speeddist -= 50
            speeddist2 -= 50
            speeddist3 -= 50
            
            global frame_s
            global frame_s2
            global frame_s3
            
            if frame_s > 8:
                frame_s = 0
            if frame_s2 > 8:
                frame_s2 = 0
            if frame_s3 > 8:
                frame_s3 = 0
                
            if speeddist <= s.range:
                b.hp -= s.dmg
                frame_s += 1
            if speeddist2 <= s2.range:
                b.hp -= s2.dmg
                frame_s2 += 1
            if speeddist3 <= s3.range:
                b.hp -= s3.dmg
                frame_s3 += 1
            
            sniperdist = math.sqrt(((b.x + 25) - (r.x + 25))**2 + ((b.y + 25) - (r.y + 25))**2)
            sniperdist2 = math.sqrt(((b.x + 25) - (r2.x + 25))**2 + ((b.y + 25) - (r2.y + 25))**2)
            sniperdist3 = math.sqrt(((b.x + 25) - (r3.x + 25))**2 + ((b.y + 25) - (r3.y + 25))**2)

            sniperdist -= 50
            sniperdist2 -= 50
            sniperdist3 -= 50
            
            if sniperdist <= r.range:
                b.hp -= r.dmg
            if sniperdist2 <= r2.range:
                b.hp -= r2.dmg
            if sniperdist3 <= r3.range:
                b.hp -= r3.dmg

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
                    if towersel == "basic":
                        if watermelons >= 25:
                            placetower()
                            towernum += 1
                            watermelons -= 25
                    if towersel == "speed":
                        if watermelons >= 30:
                            placetower()
                            towernum += 1
                            watermelons -= 30
                    if towersel == "sniper":
                        if watermelons >= 50:
                            placetower()
                            towernum += 1
                            watermelons -=50
                    
                    
                if event.key == pygame.K_1:
                    towersel = "basic"
                    
                if event.key == pygame.K_2:
                    towersel = "speed"
                    
                if event.key == pygame.K_3:
                    towersel = "sniper"
        
        if b.pause == 1:
            frames_t = 0
            frames_t2 = 0
            frames_t3 = 0
    
main()