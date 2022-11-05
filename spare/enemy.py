import pygame
import test

class Enemy():
    def __init__(self,size,x,y):
        super().__init__(size,x,y)
        self.x=x
        self.y=y
        self.attack=False
        self.detect=False
        self.path=[self.x,self.end]
        self.space=4
        
        self.speed=3
        self.hitbox = (self.x+20,self.y,28,60)
        self.body=pygame.draw.rect(test.win, (0,255,0), (100,100,32,60))

    def move(self):
        if self.x+self.space<self.path[1]:
            self.x+=self.speed

    def draw(self,win):
        self.move()
        pygame.draw.rect(win, (0,0,255), self.hitbox,2)