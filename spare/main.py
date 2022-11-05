import pygame, sys
import score_board
from map import *
from Tile import Tiles
from level import Level
from menu import *
from score_board import name_box
from save import *

pygame.init()
clock = pygame.time.Clock()


def game():
    level = Level(level_map, screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('black')
        level.run()

        pygame.display.update()
        clock.tick(60)

def manage_menu():
        
        bg=pygame.image.load('images/bg.png').convert_alpha()
        bg=pygame.transform.scale(bg, (screen_width,screen_height))
        screen.blit(bg, (0,0))

        fonts = pygame.font.Font('font/Liquefy.otf', 150)
        game_name = fonts.render('Game name', True,(255,255,255))
        screen.blit(game_name,(50,20))

        
        if play_button.trig(screen):
            print("start")
            game()
        elif quit_button.trig(screen):
            print('exit')
            score_b()
            #sys.exit()

def score_b():
    

     while True:
        bg=pygame.image.load('images/bg.png').convert_alpha()
        bg=pygame.transform.scale(bg, (screen_width,screen_height))
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('black')
        
        readfile()

        pygame.display.update()
        clock.tick(60)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    manage_menu()

    pygame.display.update()
    clock.tick(60)


