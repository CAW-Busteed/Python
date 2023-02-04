import pygame
import random
import time
import math
from pygame.math import Vector2

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

SW = 400
SH = 300

PLAYER_ICON = pygame.image.load('Assets/player_ship.gif')
BG = pygame.image.load('Assets/starry_sky_bg.jpg')
BG = pygame.transform.scale(BG, (SW, SH))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()

        self.surf = PLAYER_ICON.convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

        # set initial position and angle
        self.x = SW // 2
        self.y = SH // 2
        self.angle = 0

        #supposed to determine rotation of player
        # self.rotatedSurf = pygame.transform.rotate(self.rect, self.angle)
        #properly centers
        # self.rotatedRect = self.rotatedSurf.get_rect()
        # self.rotatedRect.center = (self.x, self.y)

        #using math to properly set parameters
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))

        #gives us x and y of front ship to determine projectile direction when shot
        # w = self.rect.width
        # h = self.rect.height
        # self.head = (self.x + self.cosine * self.w // 2,
        #              self.y - self.sine * self.h // 2)

    def draw(self, screen):
        # win.blit(self.rect, [self.x, self.y, self.w, self.h])
        #the following will track sprite turn
        screen.blit(self.surf, self.rect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.rect, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        #to reset. The turtorial had a + \/ rather than a *, could he have made a msitake?
        self.head = (self.x + self.cosine + self.w // 2,
                     self.y - self.sine * self.h // 2)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.rect, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        #to reset
        self.head = (self.x + self.cosine + self.w // 2,
                     self.y - self.sine * self.h // 2)

    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.rect, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        #to reset
        self.head = (self.x + self.cosine + self.w // 2,
                     self.y - self.sine * self.h // 2)
        #inverse to decvelerate?

    #copy-pasted from simple, need to figure out how to orient it
    # def update(self, pressed_keys):
    #     if pressed_keys[K_UP]:
    #         player.moveForward()
    #     #for deceleration it would be player.Brake
    #     # if pressed_keys[K_DOWN]:
    #     #    self.rect.move_ip(0, 5)
    #     if pressed_keys[K_LEFT]:
    #         player.turnLeft()
    #     if pressed_keys[K_RIGHT]:
    #         player.turnRight()


SCREEN = pygame.display.set_mode((SW, SH))

clock = pygame.time.Clock()
player = Player()


def redrawGameWindow():
    # SCREEN.blit(BG, (0, 0))
    # player.draw(SCREEN)
    # pygame.display.update()
    

    player.surf = pygame.transform.rotate(player.surf, -40)
    player.surf = pygame.transform.scale(player.surf, (110, 110))
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(player.surf, pygame.Rect(100, 100, 100, 100))
    pygame.display.update()



#setup of caption, sounds, clock, intitialize
def initialize():
    pygame.display.set_caption('Asteroids Clone')
    #then come the assets

    # TODO: animate gif
    SCREEN = pygame.display.set_mode((SW, SH))

    pygame.mixer.init()
    pygame.init()


initialize()

run = True
gameover = False

while run:
    clock.tick(20)
    # if not gameover:
        #pass acts as a placeholder. Neat trick!
        #already imported controls
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     player.turnLeft()
        # if keys[pygame.K_RIGHT]:
        #     player.turnRight()
        # if keys[pygame.K_UP]:
        #     player.moveForward()
        # # translate coordinates to keep player in bounds
        # #OR make it so screen follows player
        # if player.rect.left < -10:
        #     player.rect.left = -10
        # if player.rect.right > SW:
        #     player.rect.right = SW
        # if player.rect.top <= -10:
        #     player.rect.top = -10
        # if player.rect.bottom >= SH:
        #     player.rect.bottom = SH

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == KEYDOWN:
            #want to add controls to player: orient (r&l keys) accelerate (up), brake(down), and eventually shoot (sending a projectile with spacebar)
            #pygame.transform.rotate() by 2-4 degrees for orientation
            # Acceleration is cumulative, so every second of KEYDOWN_UP should increase velocity on an axis for a maximum of 299
            #brake would reduce speed on axis until -20 (backing up slowly in comparison)
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                run = False

            #elif event.key == K_RIGHT:
            #    player.img= pygame.transform.rotate(PLAYER_ICON, -90).convert()
            #elif event.key == K_LEFT:
            #    player.img= pygame.transform.rotate(PLAYER_ICON, 90).convert()
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            run = False
    redrawGameWindow()

pygame.quit()

# an alternative
#class Player(pygame.sprite.Sprite):
#    def __init__(self):
#        super(Player, self).__init__()
#        #convert optimizes, set color key determines which color code to make transparent
#        self.surf = pygame.image.load('Assets/player_ship.gif').convert()
#        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
#        self.rect = self.surf.get_rect()

# class Block(pygame.sprite.Sprite):

#     # Constructor. Pass in the color of the block,
#     # and its x and y position
#     def __init__(self, color, width, height):
#        # Call the parent class (Sprite) constructor
#        pygame.sprite.Sprite.__init__(self)

#        # Create an image of the block, and fill it with a color.
#        # This could also be an image loaded from the disk.
#        self.image = pygame.Surface([width, height])
#        self.image.fill(color)

#        # Fetch the rectangle object that has the dimensions of the image
#        # Update the position of this object by setting the values of rect.x and rect.y
#        self.rect = self.image.get_rect()
