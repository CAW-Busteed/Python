'''
Build a UI for cows and bulls
four squares that fill with cows and bulls
'''
import pygame as pg
# import bull
# import time

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
rect_side = (SCREEN_HEIGHT // 3)
clock = pg.time.Clock()

input = None
user_input = []

keyDict = {
    pg.K_0: 0,
    pg.K_1: 1,
    pg.K_2: 2,
    pg.K_3: 3,
    pg.K_4: 4,
    pg.K_5: 5,
    pg.K_6: 6,
    pg.K_7: 7,
    pg.K_8: 8,
    pg.K_9: 9,
}


class Startup:
    def startup_screen(self):
        #TODO: refine the startup screen
        size = 30
        font = pg.font.Font(None, size)
        text = font.render('How to play:', True, (10, 10, 10))
        text_pos = (0,0)
        screen.blit(text, text_pos)
        pg.display.flip()

class Input:
    pass

    def screen_reset(self, screen, rect_side):
        screen.fill((126, 200, 80))  # fill entire screen with green

        # draw each box
        pg.draw.rect(screen, (0, 0, 0), (100, 100, rect_side, rect_side), 4)
        pg.draw.rect(screen, (0, 0, 0), (400, 100, rect_side, rect_side), 4)
        pg.draw.rect(screen, (0, 0, 0), (700, 100, rect_side, rect_side), 4)
        pg.draw.rect(screen, (0, 0, 0), (1000, 100, rect_side, rect_side), 4)

        pg.display.flip()  # updates screen


    def center_num(self):
        self.screen_reset(screen, rect_side)
        response = enumerate(user_input)
        font = pg.font.Font(None, rect_side)
        for position, integer in response:

            text = font.render(str(integer), True, (10, 10, 10))

            #transform font by half of its size from the midpoint of the rect
            
            border = 100
            square_midpoint_width = (rect_side // 2)
            shift_x = position*300
            digit_width = (font.size(str(integer))[0])
            digit_height = (font.size(str(integer))[1])

            textpos_x =shift_x + border + square_midpoint_width - digit_width // 2
            textpos_y = border + square_midpoint_width - digit_height//2

            textpos = textpos_x, textpos_y
            

            screen.blit(text, textpos)
            pg.display.flip()


def main():
    # set up a dark green screen with caption
    pg.init()
    pg.display.set_caption("Cows & Bulls")
    screen.fill((126, 200, 80))
    Startup().startup_screen()
    input = Input()

    # #make 4 squares in a row
    # #draw rect  on screen   black   location        size        border size
    # pg.draw.rect(screen, (0, 0, 0), (100, 100, rect_side, rect_side), 4)
    # pg.draw.rect(screen, (0, 0, 0), (400, 100, rect_side, rect_side), 4)
    # pg.draw.rect(screen, (0, 0, 0), (700, 100, rect_side, rect_side), 4)
    # pg.draw.rect(screen, (0, 0, 0), (1000, 100, rect_side, rect_side), 4)

    # #updates screen, do this for title screen or instructions
    # pg.display.flip()

    #TODO:collate the bulls program to connect results to 4 squares

    run = True
    while run:
        clock.tick(60)

        for event in pg.event.get():
            if event.type != pg.KEYDOWN:
                continue

            # if len(user_input) == 4:
            #     # if event.type == pg.QUIT:
            #     #     run = False
            #     if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            #         run = False
            #         #TODO: this is where we add in the bull.py
            #     continue
            # elif event.type == pg.QUIT:
            #     run = False
            #     continue

            if event.key == pg.K_ESCAPE:
                run = False
                continue
            elif event.key == pg.K_BACKSPACE:
                del user_input[-1]
                input.center_num()
                continue

            digit = keyDict.get(event.key, -1)
            user_input.append(digit)
            input.center_num()


if "__main__" == __name__:
    main()
