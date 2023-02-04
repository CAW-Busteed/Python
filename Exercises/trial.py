import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor('pink')
#player setup
player_one = turtle.Turtle()
player_one.color('green')
player_one.shape('turtle')

#I could copy-paste but let's experiment. Clone then differentiate 
#spacially and colorfully

player_two = player_one.clone()
player_two.color('yellow')
player_one.penup()
player_two.penup()
player_two.goto(-200,200)
player_one.goto(-200,-200)

#make a finish line
#tried with a thrid party, player one had to step up
player_one.goto(200,200)
player_one.right(90)
player_one.pendown()
player_one.color('black')
player_one.forward(400)
player_one.write('Finish Line',font=20)

#player one returns back to set up. 
# Why not just have him start making the finish line? 
# maybe in v2
player_one.color('green')
player_one.penup()
player_one.goto(-200,-200)
player_one.left(90)

#Finish line done, let's do inputs?
#tricky, start with easier stuff. Die rolling.
player_one.pendown()
player_two.pendown()
die = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(30):
    if player_one.pos() >= (200,-200):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (200,200):
        print("Player Two Wins!")
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(10 * die_roll)
        time.sleep(2)
        die_roll2 = random.choice(die)
        player_two.forward(10 * die_roll2)
        time.sleep(2)

 #this keeps the screen up
turtle.done()
    #this code doesn't work, dissect later
    #referee = player_one.clone
    #referee.color('purple')
    #referee.penup()
    #referee.goto(200,200)
    #referee.right(90)