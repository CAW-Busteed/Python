'''
Build a UI for cows and bulls
four squares that fill with cows and bulls
'''
import pygame as pg
import bull
import time

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

input = None
user_input = []

def main():
    run = True

    def center_num(input):
        if pg.font:
            response = enumerate(input)
            font = pg.font.Font(None, rect_side)
            for position, integer in response:
                text = font.render(str(integer), True, (10, 10, 10))

                #transform font by half of its size from the midpoint of the rect
                textpos = ((position*300)+100)+ (rect_side//2) -((font.size(str(integer))[0])//2), (100+ (rect_side//2)) -((font.size(str(integer))[1])//2) 
            

            screen.blit(text, textpos)
            pg.display.flip()

    def init_num(digit):
        user_input.append(digit)  
        center_num(user_input)
          

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
    
    
    while run:
        clock.tick(60)


        for event in pg.event.get():
            if len(user_input) == 4:
                if event.type == pg.QUIT:
                    run = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    run = False
                #TODO: this is where we add in the bull.py
                
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
        
        
        
        
            

if __name__ == "__main__":
    main()