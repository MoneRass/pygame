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
game_state=0



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
    while True:
        bg=pygame.image.load('images/bg.png').convert_alpha()
        bg=pygame.transform.scale(bg, (screen_width,screen_height))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(bg, (0,0))

        fonts = pygame.font.Font('font/Liquefy.otf', 150)
        game_name = fonts.render('Game name', True,(255,255,255))
        screen.blit(game_name,(50,20))

        if play_button.trig(screen):
            print("start")
            enter_name()

        elif score_button.trig(screen):
            print('score')
            game_state=1
            score_b()
        elif quit_button.trig(screen):
            print('exit')
            sys.exit()
        pygame.display.update()
        clock.tick(60)

def score_b():
    

     while True:
        bg=pygame.image.load('images/bg.png').convert_alpha()
        bg=pygame.transform.scale(bg, (screen_width,screen_height))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        screen.blit(bg, (0,0))
        readfile()

        if back_button.trig(screen):
            manage_menu()

        pygame.display.update()
        clock.tick(60)

def enter_name():
    _name=''
    fonts = pygame.font.Font('font/Liquefy.otf', 100)
    
    text_box = pygame.Rect(screen_width/2-20,screen_height/2-10,0,100)

    while True:
        bg=pygame.image.load('images/bg.png').convert_alpha()
        bg=pygame.transform.scale(bg, (screen_width,screen_height))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(_name)
                    #retaurn _name
                    game()
                elif event.key == pygame.K_BACKSPACE:
                    _name = _name[:-1]
                    
                else:
                    _name += event.unicode
                    
        
        screen.blit(bg, (0,0))
        pygame.draw.rect(screen, 'white', text_box,2)
        
        display_name=fonts.render(_name, True,(255,255,255))
        screen.blit(display_name, (text_box.x+5,text_box.y+5))

        text_box.w = display_name.get_width()+10

        pygame.display.update()
        clock.tick(60)
    

 

manage_menu()


