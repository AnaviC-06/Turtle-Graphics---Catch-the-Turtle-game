#Anavi Chahal
#20/11/2023
#Purpose - To modify catch the turtle by adding a start screen

import turtle
import random

screen = turtle.Screen()
screen.setup(500,500)
screen.title("Catch the turtle")
screen.bgcolor("lightblue")

#for start screen
start = turtle.Turtle()
#add the pic to the screen
screen.addshape("start.gif")
start.shape("start.gif")

game = False

player = turtle.Turtle()
player.shape("arrow")
player.color("teal")
player.penup()
player.hideturtle()

target = turtle.Turtle()
target.shape("turtle")
target.color("red")
target.penup()
target.hideturtle()

def left():
  player.left(30)
def right():
  player.right(30)

screen.listen()
screen.onkey(left,"Left")
screen.onkey(right,"Right")

counter = 0
score = turtle.Turtle()
score.color("purple")
score.penup()
score.goto(200,200)
score.hideturtle()

def draw_on_click(x,y):
  global game #this statement tells us that the variable outside the function is being used
  game = True
  start.hideturtle()
  player.showturtle()
  target.goto(random.randint(-300,300),random.randint(-300,300))
  target.showturtle()
  score.showturtle()
  score.write("Score: {}".format(counter),align = "center",font=("courier",12,"normal"))
  gameloop()

start.onclick(draw_on_click)
def gameloop():
  global counter
  while game==True:
    player.forward(1)
    if player.distance(target)<20:
     target.goto(random.randint(-300,300),random.randint(-300,300))
     counter += 1
     score.clear()
     score.write("Score: {}".format(counter),align = "center",font=("courier",12,"normal"))
    screen.update()
screen.mainloop()