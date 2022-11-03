import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)

########### Challenge 4 - Random Walk ########
directions = [0, 90, 180, 270]

tim.speed("fast")
tim.pensize(10)

for _ in range(4000):

  rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  tim.pencolor(rgb)
  tim.shape("turtle")
  tim.setheading(random.choice(directions))
  tim.forward(20)
