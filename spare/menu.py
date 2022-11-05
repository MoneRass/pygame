import pygame
from map import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('This is very very fun game')

#play button
play_image = pygame.image.load('images/Icons_14.png').convert_alpha()
scoreboard_image = pygame.image.load('images/Icons_14.png').convert_alpha()
quit_image = pygame.image.load('images/Icons_14.png').convert_alpha()

#game name
fonts = pygame.font.Font('font/Liquefy.otf', 70)
game_name = fonts.render('Game name', True,(255,255,255))



class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.click=False

        self.surface = pygame.Surface((screen_width, screen_height))
        
    def trig(self, surface):
        triggered=False
        #mouse pos
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click==False:
                self.click=True
                triggered=True

            if pygame.mouse.get_pressed()[0] == 0:
                self.click=False


        surface.blit(self.image, (self.rect.x, self.rect.y))

        return triggered




play_button = Button(screen_width/2,200,play_image, 1.5)
quit_button = Button(screen_width/2,400,quit_image,1.5)

