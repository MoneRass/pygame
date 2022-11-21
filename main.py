import pygame, sys
from level import Level,score
from menu import *
from save import readfile
from record import writefile
from map import level_map
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
game_state=0
current_map = level_map

def game():
    
    name = enter_name()
    mixer.music.load('audio/game.wav')
    mixer.music.play(-1)
    level = Level(level_map, screen)
    global score
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
       
        screen.fill('black')
        if(level.end_game()==False):level.run()
        elif(level.end_game()==True):
            if name=='':
                name='Anonymous'
            writefile(name,level.send_score())
            summ = level.summary(level.send_score())

            if summ == 0:
                level.reset_stat()
                manage_menu()
        
        pygame.display.update()
        clock.tick(60)

def manage_menu():
    mixer.music.load('audio/Caro.wav')
    mixer.music.play(-1)
    
    
    while True:
        bg=pygame.image.load('images/bg.png').convert_alpha()
        bg=pygame.transform.scale(bg, (screen_width,screen_height))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(bg, (0,0))

        fonts = pygame.font.Font('font/Liquefy.otf', 150)
        norsor_font = pygame.font.Font('font/Liquefy.otf', 30)

        game_name = fonts.render('runner of hermes', True,(255,100,100))
        norsor_name = norsor_font.render('65010452 Thummatos sribunna', True,(255,255,255))

        screen.blit(game_name,(screen_width/2-(game_name.get_width()/2),20))
        screen.blit(norsor_name, (screen_width/2+300,750))

        if play_button.trig(screen):
            print("start")
            
            game()
            

        elif score_button.trig(screen):
            print('score')
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
                    return _name
                    #game()
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
