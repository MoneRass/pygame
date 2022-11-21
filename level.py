import pygame,sys
from pygame import mixer
from Tile import Tiles
from Hunter import Hunter
from flyingEnemie import Flying_Bat
from item_box import ItemBox
from game_ui import Stamina_bar
from menu import screen
from portal import Portal
from map import all_map
import random

spawn_index=0
enemies_list=[]
score_font = pygame.font.Font('font/Liquefy.otf', 75)
start_ticks=pygame.time.get_ticks()
font = pygame.font.Font('font/Liquefy.otf', 110)

tile_size = 60
screen_width = 1280
screen_height = 780

hp=3
score=0

class Level:
        def __init__(self, level_data, surface):
            self.display_surface = surface
            self.level_data = level_data
            self.setup_level(level_data)

            self.world_shift = 0

            self.player_score = 200
            self.buffed=False
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
            self.prev_map = 0

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
            global hp
            global score
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
                    if self.hunter_sprite.block()==False:
                        dmg_sound = mixer.Sound('audio/dmg.wav')
                        dmg_sound.play()
                        self.hunter_sprite.damage()
                        score-=100
                        hp-=1
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

            if hunter_y < screen_height / 4 and direction_y < 0:
                self.world_shift = 8
                
                self.bat_shift = 8
                hunter.speed = 0
            elif hunter_y > screen_height - (screen_width / 4) and direction_y > 0:
                self.world_shift = -8
                self.bat_shift = -8
                hunter.speed = 0
            else:
                self.world_shift = 0
                self.bat_shift = 0
                hunter.speed = 8

        def run(self):
            global hp
            global score
            self.Tile.update(self.world_shift)
            self.Tile.draw(self.display_surface)
            self.camera_x()
            #self.camera_y()
            self.hunter.update()
            self.hunter.draw(self.display_surface)
            self.hp_display(str(hp))
            
            self.horizontal_collision()
            self.vertical_collision()
            #self.get_damage()

            self.boss.draw(self.display_surface)
            self.bat.draw(self.display_surface)
            self.item.draw(self.display_surface)
            self.portals.draw(self.display_surface)

            self.bat.update(self.bat_shift,self.hitted)
            self.port.update(self.world_shift)
            self.score(score)

            self.spawn_skull()

            self.item.update(self.world_shift)
            self.chest_collide()
            self.portal_collide()

            self.UI()
            
            if hp<=0:
                self.end=True
                self.end_game()

            if self.end==True or self.hunter_sprite.force()==True:
                self.end=True
    
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
            global hp
            global score
            
            
            for item in self.item.sprites():
                if item.rect.colliderect(hunter.rect):
                    sound = mixer.Sound('audio/chest.wav')
                    sound.play()
                    buff_stat=['plus_hp','plus_sc','minus_sc','refill_stamina']
                    n=random.choice(buff_stat)
                    if n==buff_stat[0]:
                        hp+=1
                        print(hp)
                    elif n==buff_stat[1]:
                        score+=500
                        print(score)
                    elif n==buff_stat[2]:
                        score-=500
                        print(score)
                    elif n==buff_stat[3]:
                        self.hunter_sprite.refill_stamina()

                    self.item.remove(item)

        def portal_collide(self):
            global score
            hunter = self.hunter.sprite
            for portals in self.portals.sprites():
                if portals.rect.colliderect(hunter.rect):
                    sound = mixer.Sound('audio/portal.wav')
                    sound.play()
                    score+=1000
                    n = random.randint(0,3)
                    
                    if n==self.prev_map:
                        n = random.randint(0,1)
                    else:
                        self.setup_level(all_map[n])
                        self.prev_map = n
                    print(n)

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

        def end_game(self):
            return self.end

        def summary(self,score):
            
            self.key = pygame.key.get_pressed()
            press_font = pygame.font.Font('font/Liquefy.otf', 30)

            bg=pygame.image.load('images/bg.png').convert_alpha()
            bg=pygame.transform.scale(bg, (screen_width,screen_height))
                
            self.screen.blit(bg, (0,0))
            self.game_over = font.render('game over : ', True,(255,255,255))
            self.press_any = press_font.render('press "E" key to continue', True,(255,255,255))
            self.your_score = font.render(str(score), True,(255,255,255))
            
            self.screen.blit(self.game_over, (screen_width/2-(self.game_over.get_width()/2), 60))
            self.screen.blit(self.your_score, (screen_width/2-(self.your_score.get_width()/2), (screen_height/2)-20))
            self.screen.blit(self.press_any, (screen_width/2-(self.press_any.get_width()/2), (screen_height)-60))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        return 0
            
        def send_score(self):
            global score
            return score

        def reset_stat(self):
            global score
            global hp
            self.bat_sprite.reset_speed()
            hp=3
            score=0
            
                                
        def hp_display(self,hp):
           
            hp_font = pygame.font.Font('font/Liquefy.otf', 30)
            hp_num = hp_font.render(hp, True,(255,255,255)) 
            heart_image = pygame.image.load('images/hp.png')
            
            self.screen.blit(hp_num,(75,20))
            self.screen.blit(heart_image, (10,10))
        