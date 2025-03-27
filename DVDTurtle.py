import turtle
import random


my_turtle = turtle.Turtle()
screen = turtle.Screen()

screen.setup(1024, 768)

image_w = 640
image_h = 298
image = 'DVD.gif'
screen.addshape(image)
my_turtle.shape(image)
my_turtle.shapesize(image_w, image_h, 1)
my_turtle.speed(1)
my_turtle.penup()

def hit_wall(t:turtle.Turtle, s:turtle.Screen):
    hit_wall = False
    wall = ''
    if t.xcor() + (t.turtlesize()[0] / 2) >= (s.window_width() / 2):  # Hit right wall
        print("Hit right")
        hit_wall = True
        wall ='r'
    if t.xcor() - (t.turtlesize()[0] / 2) <= -(s.window_width() / 2): # Hit left wall
        print("Hit left")
        hit_wall = True
        wall = 'l'
    if t.ycor() + (t.turtlesize()[1] / 2) >= (s.window_height() / 2):  # Hit top wall
        print("Hit top")
        hit_wall = True
        wall = 't'
    if t.ycor() - (t.turtlesize()[1] / 2) <= -(s.window_height() / 2): # Hit bottom wall
        print("Hit bottom")
        hit_wall = True
        wall = 'b'
    return hit_wall, wall

def game_loop(t: turtle.Turtle, s: turtle.Screen):
    while True:
        t.forward(10)
        if hit_wall(t, s)[0]:
            t.left(random.randint(120, 241))

game_loop(my_turtle, screen)
#for i in range(1):
#    #print(my_turtle.xcor(), my_turtle.ycor())
#    print(my_turtle.turtlesize())
#    print(screen.window_height())
#
#    my_turtle.forward(192)
#    hit_wall(my_turtle, screen)
#    my_turtle.left(180)
#    my_turtle.forward(384)
#    hit_wall(my_turtle, screen)
#    my_turtle.left(180)
#    my_turtle.forward(168)
#    my_turtle.left(90)
#    my_turtle.forward(235)
#    hit_wall(my_turtle, screen)
#    my_turtle.left(180)
#    my_turtle.forward(470)
#    hit_wall(my_turtle, screen)

turtle.exitonclick()

