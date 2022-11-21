import pygame

class Tiles(pygame.sprite.Sprite):
    def __init__(self, pos, size, surface):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft=pos)
        self.image = surface
       

    def update(self, x_shift):
        self.rect.x += x_shift
        