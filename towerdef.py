import pygame
import time
import random
import player
from player import Player
#import baddie
#from baddie import Baddie

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
    screen.blit(baddie_img, (Baddie.x, Baddie.y))
    pygame.display.flip

black = (0, 0, 0)
white = (255, 255, 255)
size = [750, 500]
screen = pygame.display.set_mode(size)
player_img = pygame.image.load("sprites/cursor.png")
baddie_img = pygame.image.load("sprites/baddie.png")
lvl_1 = pygame.image.load("sprites/LEVEL_1.png")
lvl = 1
screen.blit(lvl_1, (0, 0))
screen.blit(player_img, (0, 0))
draw()

def main():
    pygame.init()
    p = Player()
    done = False

    # Level
    
    lvl1_board = [("X", 0, 350, 200),
                  ("Y", 150, 200 ,350),
                  ("X", 50, 150, 200),
                  ("Y", 50, 50, 150),
                  ("X", 50, 50, 400),
                  ("Y", 50, 400, 400),
                  ("X", 400, 400, 450)
    ]
    """ Idk what to do 'bout it, but put baddie code here"""
    #def pathx():
    #    for item in lvl1_board:
    #        print("hi")
    #pathx()
    #def pathy():
        
        
    # Events go here:    
    while True:
        if p.x <= 0:
            p.x = 0
        if p.x >= 700:
            p.x = 700
        if p.y <= 0:
            p.y = 0
        if p.y >= 450:
            p.y = 450
        
        draw_plr(p)
            
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
                    
                    
    
main()