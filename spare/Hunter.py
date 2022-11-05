import pygame
from extension import import_folder
from map import *
class Hunter(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animation_sheet()
        self.frame_rate=0.10
        self.frame_index=0
        self.image = self.animations['idle'][self.frame_index]
        self.image = pygame.transform.scale(self.image, ((self.image.get_width()*3)-50,self.image.get_height()*3))
        self.rect = self.image.get_rect(topleft = pos)
        self.startPos=(300,420)
        
        #self.rect.topleft = [pos_x,pos_y]
       
        #Player Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 7
        self.jump_speed = -20
        self.gravity = 0.8
        self.dash_speed = 4
        self.ground = 1
        self.click = False

        self.atk = False
        self.death = False

        #Stat
        self.stats = {'health': 100,'stamina':60,'damage':10}
        self.health = self.stats['health']
        self.stamina = self.stats['stamina']
        
    def animation_sheet(self):
        path = 'images/PlayerSprite/'
        self.animations = {'idle':[], 'run':[], 'heavy_attack':[], 'light_attack':[], 'roll':[]}

        for animation in self.animations.keys():
            full_path = path + animation
            self.animations[animation] = import_folder(full_path)

    def control(self):
        self.moving = False
        key = pygame.key.get_pressed()

        if key[pygame.K_d]:
            self.direction.x = 1
            self.moving = True
            self.animate('run')
        elif key[pygame.K_a]:
            self.direction.x = -1
            self.moving = True
            self.animate('run')
        else:
            self.direction.x = 0
        if key[pygame.K_SPACE] and (self.ground == 1):
            self.moving = True
            self.jump()

        if key[pygame.K_z]:
            self.moving = True
            self.dash()
        #Mouse listener
        if pygame.mouse.get_pressed()[0] == 1 and self.click==False:
            self.attack()
            self.click=True
        if pygame.mouse.get_pressed()[0] == 0:
            self.click=False

        if pygame.mouse.get_pressed()[1] == 1 and self.click==False and self.atk==False:
            self.attack()
            self.frame_index=0
            self.click=True
        if pygame.mouse.get_pressed()[1] == 0:
            self.click=False


    def jump(self):
        self.direction.y = self.jump_speed
        self.ground = 0
        self.double_jump = 1

    def gravity_on(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
        if self.rect.y > screen_height+500:
            
            self.rect.x=0
            self.rect.y=0
          
    def animate(self, state):
        animation = self.animations[state]
        
        self.frame_index += self.frame_rate
        if self.frame_index>=len(animation):
            self.frame_index=0
            self.atk = False
        self.image = animation[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3,self.image.get_height()*3))
        
    def animation_state(self):
        if self.moving == False:
            self.animate('idle')
        
    

    def attack(self):
        self.atk=True
        
        self.moving = True
        self.animate('light_attack')

    def dash(self):
        self.direction.x = self.dash_speed
        self.animate('roll')

    def update(self):
        self.control()
        self.animation_state()

    def location(self):
        locationX = self.rect.x
        return locationX

Clock =  pygame.time.Clock()