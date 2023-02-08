import pygame
from sys import exit


#starting variables
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

#variable surfaces?
map_surface = pygame.image.load('Assets/snowy_test_map.jpg')
left_surface = pygame.image.load('Assets/gen_mountain.jpg')
text_surface = test_font.render('Scary things', True, 'Purple')

ghoul_surface = pygame.image.load('Assets/ghoul.jpeg')
#Note the origin point is in top left.
#changes on y axis are +added to go down

ghoul_x_pos = 600
ghoul_y_pos = 250
#The following up to 'clock.tick' limits speed of the game to 60 times per second
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #blit means BLock Image Transfer
    #layers go from lowest>highest
    screen.blit(map_surface,(0,0))
    screen.blit(left_surface, (600,-100))
    screen.blit(text_surface, (300,50))
    ghoul_x_pos -= 1
    screen.blit(ghoul_surface,(ghoul_x_pos, ghoul_y_pos))
    #updates whole thing
    pygame.display.update()
    clock.tick(60)

