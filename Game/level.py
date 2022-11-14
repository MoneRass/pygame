from turtle import position
import pygame,sys
from Tile import Tiles,StaticTile
from Hunter import Hunter,hp
from map import tile_size, screen_width,screen_height
from flyingEnemie import Flying_Bat
from item_box import ItemBox
from game_ui import Stamina_bar
from menu import screen
from portal import Portal

import random

spawn_index=0
enemies_list=[]
score_font = pygame.font.Font('font/Liquefy.otf', 75)
start_ticks=pygame.time.get_ticks()
font = pygame.font.Font('font/Liquefy.otf', 110)


class Level:
        def __init__(self, level_data, surface):
            self.display_surface = surface
            self.level_data = level_data
            self.setup_level(level_data)

            self.world_shift = 0

            self.player_score = 200

            self.bat_shift = 0
            self.spawn_index=0
            self.hit=False
            self.num_skull=0

            self.hp=100
            self.speed_buff=0
            self.jump_buff=0

            self.hitted=False
            self.end=False
            self.screen = screen

        def setup_level(self, layout):
            self.Tile = pygame.sprite.Group()
            self.item = pygame.sprite.Group()
            self.portals = pygame.sprite.Group()
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

                    if cell == 'C':
                        item_skin=pygame.image.load('images/Icons_14.png').convert_alpha()
                        item_skin=pygame.transform.scale(item_skin, (tile_size,tile_size))
                        self.item_sprite = ItemBox((x,y), tile_size,item_skin)
                        
                        self.item.add(self.item_sprite)

                    if cell == 'P':
                        self.hunter_sprite = Hunter((x, y))
                        self.hunter.add(self.hunter_sprite)
                    if cell == 'B':
                        boss_sprite = Boss((x, y))
                        self.boss.add(boss_sprite)

                    if cell == 'Z':
                        bat_surface=pygame.image.load('images/skull.png').convert_alpha()
                        bat_surface=pygame.transform.scale(bat_surface, (30,30))
                        self.bat_sprite = Flying_Bat((x, y), bat_surface)
                        self.bat.add(self.bat_sprite)

                    if cell == 'T':
                        self.portal_skin=pygame.image.load('images/Green.png').convert_alpha()
                        self.portal_skin=pygame.transform.scale(self.portal_skin, (tile_size,tile_size))
                        self.port = Portal((x, y), tile_size,self.portal_skin)
                        
                        self.portals.add(self.port)
        
        def spawn_skull(self):
            hunter = self.hunter.sprite
            self.spawn_rate=0.4
            
            self.max_skull=15
            positionY= random.randint(3,13)
            bat_surface=pygame.image.load('images/skull.png').convert_alpha()
            bat_surface=pygame.transform.scale(bat_surface, (30,30))
            self.spawn_index+=0.4
            
            self.bat_sprite = Flying_Bat((1280, positionY*60), bat_surface)
        
            if self.spawn_index>=100:
                self.bat.add(self.bat_sprite)
                #self.bat_sprite.add(self.bat)
                self.num_skull+=1
                print('skull : ',self.num_skull)
                self.spawn_index=0

            for sprites in self.bat.sprites():
                if sprites.rect.colliderect(hunter.rect):
                    self.hunter_sprite.damage()
                    self.end=True
                    self.bat.remove(sprites)
                    
        def camera_x(self):
            hunter = self.hunter.sprite
            hunter_x = hunter.rect.centerx
            
            bat=self.bat.sprites
            
            direction_x = hunter.direction.x

            if hunter_x < screen_width / 2 and direction_x < 0:
                self.world_shift = 8
                self.bat_shift = -8
                hunter.speed = 0
            elif hunter_x > screen_width - (screen_width / 2) and direction_x > 0:
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
            #self.get_damage()

            self.boss.draw(self.display_surface)
            self.bat.draw(self.display_surface)
            self.item.draw(self.display_surface)
            self.portals.draw(self.display_surface)

            self.bat.update(self.bat_shift,self.hitted)
            self.port.update(self.world_shift)
            self.score(self.hunter_sprite.return_hunter_score())

            self.spawn_skull()

            self.item.update(self.world_shift)
            self.chest_collide()

            self.UI()

            if(self.end==True):
                self.end_game()
                

        def horizontal_collision(self):
            hunter = self.hunter.sprite
            hunter.rect.x += hunter.direction.x * hunter.speed
            
            for sprite in self.Tile.sprites():
                if sprite.rect.colliderect(hunter.rect):
                    
                    if hunter.direction.x < 0:#+
                        hunter.rect.left = sprite.rect.right
                    elif hunter.direction.x > 0:#-
                        hunter.rect.right = sprite.rect.left

        def chest_collide(self):
            hunter = self.hunter.sprite
            
            for item in self.item.sprites():
                if item.rect.colliderect(hunter.rect):
                    random_item=random.randint(1,3)
                    self.hp+=10
                    self.show_buff('hp',item)
                    

        def UI(self):
            stamina_bar = Stamina_bar(self.hunter_sprite.stamina, 100)          
            stamina_bar.draw(self.hunter_sprite.stamina)
                    
        def score(self,score):  
            self.display_score1=score_font.render('score : ', True,(255,255,255))
            self.display_score2=score_font.render(str(score), True,(255,255,255))
            self.screen.blit(self.display_score1, (screen_width/1.5, 20))
            self.screen.blit(self.display_score2, (screen_width/1.5+200, 20))

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

        def show_buff(self,buff,item):
            start = pygame.time.get_ticks()
            seconds=(pygame.time.get_ticks()-start_ticks)/1000
            if seconds<10:
                self.display_buff=score_font.render(buff, True,(255,255,255))
                self.screen.blit(self.display_buff, (screen_width/2,12))
            else:
                self.item.remove(item)
                seconds=0
            print(seconds)

        def end_game(self):
            return self.end

        def summary(self,score):
            self.key = pygame.key.get_pressed()

            bg=pygame.image.load('images/bg.png').convert_alpha()
            bg=pygame.transform.scale(bg, (screen_width,screen_height))
                
            self.screen.blit(bg, (0,0))
            self.game_over = font.render('game over : ', True,(255,255,255))
            self.press_any = font.render('press any key', True,(255,255,255))
            self.your_score = font.render(str(score), True,(255,255,255))

            self.screen.blit(self.game_over, (screen_width/2, (screen_height/2)-60))
            self.screen.blit(self.your_score, (screen_width/2, (screen_height/2)+20))
            self.screen.blit(self.press_any, (screen_width/2, (screen_height/2)+40))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
                if event.type == pygame.KEYDOWN:
                    return 0
            
        def send_score(self):
            return self.hunter_sprite.return_hunter_score()
                    

        