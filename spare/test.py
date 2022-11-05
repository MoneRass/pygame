import pygame, sys

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
#test_tile = pygame.sprite.Group(Tiles((100, 100), 200,'images/Platform/FireTiles/Fire_9_16x16.png'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen.fill('black')
   
    pygame.display.update()
    clock.tick(60)
