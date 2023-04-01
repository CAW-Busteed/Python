'''
Build a UI for cows and bulls
four squares that fill with cows and bulls
'''
import pygame as pg
import bull
import time

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

def main():
    def center_num(input, length, tally):
        if pg.font:
            font = pg.font.Font(None, length)
            text = font.render(input, True, (10, 10, 10))
            #transform font by half of its size from the midpoint of the rect
            #TODO: make the rest of the numbers in squares, maybe as a function
            textpos = ((tally*300)+100)+ (length//2) -(font.size(input)[0]//2), (100+ (length//2) -(font.size(input)[1]//2)) 
            #, (400,100), (700,100), (1000,100)
            #text.get_rect(centerx=screen.get_width() / 2, y=10)
            screen.blit(text, textpos)
            pg.display.flip()

    def init_num(digit):
        center_num(digit, rect_side, count)
        count+=1
        user_input.append(digit)    

    pg.init()
    # set up a dark green screen with caption
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((126,200,80))
    pg.display.set_caption("Cows & Bulls")
    rect_side = (SCREEN_HEIGHT //3 )
    clock = pg.time.Clock()
    
    #make 4 squares in a row 
    #draw rect  on screen   black   location        size        border size
    pg.draw.rect(screen, (0,0,0), (100, 100, rect_side, rect_side), 4)
    pg.draw.rect(screen, (0,0,0), (400, 100, rect_side, rect_side), 4)
    pg.draw.rect(screen, (0,0,0), (700, 100, rect_side, rect_side), 4)
    pg.draw.rect(screen, (0,0,0), (1000, 100, rect_side, rect_side), 4)

    #updates screen
    pg.display.flip()
    

    #TODO:collate the bulls program to connect results to 4 squares
    run = True
    input = None
    count = 0
    user_input = []
    
    while run:
        clock.tick(60)


        for event in pg.event.get():
            if count == 4:
                if event.type == pg.QUIT:
                    run = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    run = False
                #TODO: this is where we add in the bull.py
                #TODO: find out why there's a latency, and why adding an update to the screen 
                # after each key doesn't allow it to move to the next box
                time.sleep(5)
                run=False
            elif event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                run = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_0:
                init_num(0)
            elif event.type == pg.KEYDOWN and event.key == pg.K_1:
                init_num(1)
            elif event.type == pg.KEYDOWN and event.key == pg.K_2:
                init_num(2)
            elif event.type == pg.KEYDOWN and event.key == pg.K_3:
                init_num(3)
            elif event.type == pg.KEYDOWN and event.key == pg.K_4:
                init_num(4)
            elif event.type == pg.KEYDOWN and event.key == pg.K_5:
                init_num(5)
            elif event.type == pg.KEYDOWN and event.key == pg.K_6:
                init_num(6)
            elif event.type == pg.KEYDOWN and event.key == pg.K_7:
                init_num(7)
            elif event.type == pg.KEYDOWN and event.key == pg.K_8:
                init_num(8)
            elif event.type == pg.KEYDOWN and event.key == pg.K_9:
                init_num(9)
            elif event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
                pass

        #this is the reason for latency, but without it, it just overwrites
        #TODO: find a solution to allow user pauses to type
        
        
        
        
            

if __name__ == "__main__":
    main()