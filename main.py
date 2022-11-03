import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]


tim.pensize(10)

for _ in range(400):
  tim.pencolor(random.choice(colors))
  tim.shape("turtle")
  tim.setheading(random.choice(directions))
  tim.forward(20)
