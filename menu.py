import pygame

screen_width=1280
screen_height=780

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('65010452 Thummatos sribunna')

#game name
fonts = pygame.font.Font('font/Liquefy.otf', 70)
game_name = fonts.render('Game name', True,(255,255,255))

play = fonts.render('play', True,(255,255,255))
score_board = fonts.render('scoreboard', True,(255,255,255))
exit_game = fonts.render('exit', True,(255,255,255))
back = fonts.render('back', True,(255,255,255))



class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = image
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




play_button = Button(screen_width/2-(play.get_width()/2),200,play, 1.5)
score_button = Button(screen_width/2-(score_board.get_width()/2)-50,400,score_board, 1.5)
quit_button = Button(screen_width/2-(exit_game.get_width()/2),600,exit_game,1.5)

back_button = Button(1000,200,back, 1.5)

