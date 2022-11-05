from turtle import position
import pygame
from Tile import Tiles,StaticTile
from Hunter import Hunter
from map import tile_size, screen_width
from boss import Boss
from flyingEnemie import Flying_Bat

import random

spawn_index=0

class Level:
        def __init__(self, level_data, surface):
            self.display_surface = surface
            self.level_data = level_data
            self.setup_level(level_data)

            self.world_shift = 0
            self.bat_shift = 0
            self.spawn_index=0

            self.num_skull=0

        def setup_level(self, layout):
            self.Tile = pygame.sprite.Group()
            self.hunter = pygame.sprite.GroupSingle()
            self.boss = pygame.sprite.GroupSingle()
            self.bat = pygame.sprite.Group()
            self.play_image = pygame.image.load('images/middleground.png').convert_alpha()
            for row_index, row in enumerate(layout):
                for col_index, cell in enumerate(row):
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if cell == 'X':
                        tile_skin=pygame.image.load('images/Platform/FireTiles/Fire_9_16x16.png').convert_alpha()
                        tile_skin=pygame.transform.scale(tile_skin, (tile_size,tile_size))
                        tile = Tiles((x, y), tile_size,tile_skin)
                        
                        self.Tile.add(tile)
                    if cell == 'S':
                        tile_skin=pygame.image.load('images/Platform/FireTiles/Fire_8_16x16.png').convert_alpha()
                        tile_skin=pygame.transform.scale(tile_skin, (tile_size,tile_size))
                        tile = Tiles((x, y), tile_size,tile_skin)
                        
                        self.Tile.add(tile)

                    if cell == 'A':
                        tile_skin=pygame.image.load('images/Platform/FireTiles/Fire_4_16x16.png').convert_alpha()
                        tile_skin=pygame.transform.scale(tile_skin, (tile_size,tile_size))
                        tile = Tiles((x, y), tile_size,tile_skin)
                        
                        self.Tile.add(tile)

                    if cell == 'P':
                        hunter_sprite = Hunter((x, y))
                        self.hunter.add(hunter_sprite)
                    if cell == 'B':
                        boss_sprite = Boss((x, y))
                        self.boss.add(boss_sprite)

                    if cell == 'Z':
                        bat_surface=pygame.image.load('images/skull.png').convert_alpha()
                        bat_surface=pygame.transform.scale(bat_surface, (30,30))
                        bat_sprite = Flying_Bat((x, y), bat_surface)
                        self.bat.add(bat_sprite)
        
        def spawn_skull(self):
            
            self.spawn_rate=0.4
            
            self.max_skull=7
            positionY= random.randint(3,13)
            bat_surface=pygame.image.load('images/skull.png').convert_alpha()
            bat_surface=pygame.transform.scale(bat_surface, (30,30))
            self.spawn_index+=0.4
            
            bat_sprite = Flying_Bat((1280, positionY*60), bat_surface)
            
            if self.spawn_index>=100 and self.num_skull<=self.max_skull:
                self.bat.add(bat_sprite)
                self.num_skull+=1
                print('skull : ',self.num_skull)
                self.spawn_index=0

            for i in self.num_skull:
                self.bat.add(bat_sprite)
                self.num_skull+=1
                print('skull : ',self.num_skull)
                self.spawn_index=0
                
           
        def camera_x(self):
            hunter = self.hunter.sprite
            hunter_x = hunter.rect.centerx
            
            bat=self.bat.sprites
            
            direction_x = hunter.direction.x

            if hunter_x < screen_width / 4 and direction_x < 0:
                self.world_shift = 8
                self.bat_shift = -8
                hunter.speed = 0
            elif hunter_x > screen_width - (screen_width / 4) and direction_x > 0:
                self.world_shift = -8
                self.bat_shift = 8
                hunter.speed = 0
            else:
                self.world_shift = 0
                hunter.speed = 8
                self.bat_shift = 0
        def camera_y(self):
            hunter = self.hunter.sprite
            hunter_y = hunter.rect.centery
            direction_y = hunter.direction.y

            if hunter_y < screen_width / 4 and direction_y < 0:
                self.world_shift = 8
                self.bat_shift = 8
                hunter.speed = 0
            elif hunter_y > screen_width - (screen_width / 4) and direction_y > 0:
                self.world_shift = -8
                self.bat_shift = -8
                hunter.speed = 0
            else:
                self.world_shift = 0
                self.bat_shift = 0
                hunter.speed = 8

        def run(self):
            self.Tile.update(self.world_shift)
            self.Tile.draw(self.display_surface)
            self.camera_x()
            #self.camera_y()
            self.hunter.update()
            self.hunter.draw(self.display_surface)
            self.horizontal_collision()
            self.vertical_collision()

            self.boss.draw(self.display_surface)
            self.bat.draw(self.display_surface)

            self.bat.update(self.bat_shift)
            self.bat_collide()

            self.spawn_skull()


        def horizontal_collision(self):
            hunter = self.hunter.sprite
            hunter.rect.x += hunter.direction.x * hunter.speed

            for sprite in self.Tile.sprites():
                if sprite.rect.colliderect(hunter.rect):
                    
                    if hunter.direction.x < 0:#+
                        hunter.rect.left = sprite.rect.right
                    elif hunter.direction.x > 0:#-
                        hunter.rect.right = sprite.rect.left

        def vertical_collision(self):
            hunter = self.hunter.sprite
            hunter.gravity_on()

            for sprite in self.Tile.sprites():
                if sprite.rect.colliderect(hunter.rect):
                    if hunter.direction.y > 0:
                        hunter.rect.bottom = sprite.rect.top
                        hunter.ground = 1

                        hunter.direction.y = 0
                    elif hunter.direction.y < 0:
                        hunter.rect.top = sprite.rect.bottom
                        hunter.direction.y = 0

        def bat_collide(self):
            hunter = self.hunter.sprite

            for sprites in self.bat.sprites():
                if sprites.rect.colliderect(hunter.rect):
                    print('hit')

        