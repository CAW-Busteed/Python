import pygame
import random
import time


#setup of caption, sounds, clock, intitialize
pygame.display.set_caption('Asteroids Clone')

clock = pygame.time.Clock()


#and the fundamental controls imports
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SW = 1600
SH = 1200
screen = pygame.display.set_mode((SW, SH))

#then come the assets
bg = pygame.image.load('Assets/starry_sky_bg.jpg')
bg = pygame.transform.scale(bg, (1600, 1200))
# TODO: animate gif, make black on icon transparent 
player_icon = pygame.image.load('Assets/player_ship.gif')
screen = pygame.display.set_mode((SW, SH))
gameover = False


class Player(object):
    def __init__(self):
        self.img = player_icon
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        #position shortcut?
        self.x = SW//2
        self.y = SH//2
    # TODO: change movement to orientation
    def draw(self, win):
        win.blit(self.img, [self.x, self.y, self.w, self.h])
    #copy-pasted from simple, need to figure out how to orient it
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# an alternative
#class Player(pygame.sprite.Sprite):
#    def __init__(self):
#        super(Player, self).__init__()
#        #convert optimizes, set color key determines which color code to make transparent
#        self.surf = pygame.image.load('Assets/player_ship.gif').convert()
#        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
#        self.rect = self.surf.get_rect()
player = Player()


pygame.mixer.init
pygame.init

def redrawGameWindow():
    screen.blit(bg, (0,0))
    player.draw(screen)
    pygame.display.update()

run = True
while run:
    clock.tick(60)
    if not gameover:
        #pass acts as a placeholder. Neat trick!
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                run = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            run = False
    redrawGameWindow()
pygame.quit()