'''
Build a UI for cows and bulls
four squares that fill with cows and bulls
'''
import pygame as pg
import bull
from textwrap3 import wrap
import time

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
        #TODO: (H,M) refine the startup screen
        size = SCREEN_HEIGHT//10
        font = pg.font.Font(None, size)
        title = 'How to Play'
        text = font.render(title, True, (10, 10, 10))
        title_width = (font.size(title)[0])
        indent = (SCREEN_WIDTH - title_width)//2

        text_pos = (indent,0)
        screen.blit(text, text_pos)
        pg.display.flip()

class Explanation:
    def explanation_screen(self):
        size = SCREEN_HEIGHT//40
        font = pg.font.Font(None, size)
        explain = 'You will guess a four digit number. I will give you a response of either cows or bulls. A cow means a correct number and correct place. A bull is a correct guess in the wrong place.'
        x = wrap(explain, 30)
        tally = 0
        for i in range(len(x)):
            text = font.render(x[i], True, (10, 10, 10))
            line_width = (font.size(i)[0])
            text_y =100+(tally*(font.size(i)[1]))
            text_x = (SCREEN_WIDTH-line_width)//2
            text_pos = (text_x,text_y)
            screen.blit(text,text_pos)
            tally+=1
        pg.display.flip()

class Victory:
    def victory_screen(self, tally):
        size = SCREEN_HEIGHT//5
        font = pg.font.Font(None, size)
        end = 'YOU WIN'


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

# class Result:

    


def c_and_b_result(cowsandbulls):
    pg.draw.rect(screen, (255, 255, 255), (100, 200+rect_side, rect_side, rect_side), 4)
    pg.draw.rect(screen, (255, 255, 255), (400, 200+rect_side, rect_side, rect_side), 4)
    pg.draw.rect(screen, (255, 255, 255), (700, 200+rect_side, rect_side, rect_side), 4)
    pg.draw.rect(screen, (255, 255, 255), (1000, 200+rect_side, rect_side, rect_side), 4)
    pg.display.flip()
    time.sleep(0.5)

    #TODO: (vL,H) replace with sprites of cows and bulls that settle in the center 
    #for x in cowsandbulls:
        # if x == 'cow':
        #     pass
        # elif x == 'bull':
        #     pass


    list = enumerate(cowsandbulls)
    font = pg.font.Font(None, rect_side//2)
    for position, word in list:

        text = font.render(word, True, (10, 10, 10))

        #transform font by half of its size from the midpoint of the rect
        
        x_border = 100
        y_border = 200+rect_side
        square_midpoint_width = (rect_side // 2)
        shift_x = position*300
        word_width = (font.size(word)[0])
        word_height = (font.size(str(word))[1])

        textpos_x =shift_x + x_border + square_midpoint_width - word_width // 2
        textpos_y = y_border + square_midpoint_width - word_height//2

        textpos = textpos_x, textpos_y
        

        screen.blit(text, textpos)
        time.sleep(0.3)
        pg.display.flip()


def main():
    # set up a dark green screen with caption
    pg.init()
    pg.display.set_caption("Cows & Bulls")
    screen.fill((126, 200, 80))
    Startup().startup_screen()

    #TODO: (M,H) figure out how wrap works to run the explanation
    #Explanation().explanation_screen()
    input = Input()


    run = True
    while run:
        clock.tick(60)
        tally = 0
        gen_num = [1,2,3,4]

        if len(user_input) == 4:
            result = bull.get_cowandbull(gen_num, user_input)
            c_and_b_result(result)
            tally+=1
            bovine = bull.moo_count(result)

            if len(bovine[0]) == 4:
                #TODO: (H,M) victory screen, give option to quit or reset loop
                print(f'All cows, you win! You guessed {tally} times')
                break
            else:
                print('Try again!')

            user_input.clear()
            time.sleep(2)

        for event in pg.event.get():
            if event.type != pg.KEYDOWN:
                continue

            if event.key == pg.K_ESCAPE:
                run = False
                continue
            elif event.key == pg.K_BACKSPACE:
                del user_input[-1]
                input.center_num()
                continue
            
            #TODO (M,H) wrong input alert, window that moves in with warning
            digit = keyDict.get(event.key, 'X')
            user_input.append(digit)
            input.center_num()


if "__main__" == __name__:
    main()
