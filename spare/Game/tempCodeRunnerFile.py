import pygame, sys
from map import *
from Tile import Tiles
from level import Level
from menu import *

pygame.init()
clock = pygame.time.Clock()
level = Level(level_map, screen)

menu_screen=False

def manage_menu():
        if play_button.draw(screen):
            print("start")
        elif quit_button.draw(screen):
            print('exit')
            sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()