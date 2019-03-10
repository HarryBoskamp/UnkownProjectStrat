from turtle import *
bgcolor("black")
pencolor("white")
title("M")
setup(600,600)
hideturtle()
speed(10)
up()
pensize(10)

goto(-300,100)
down()
forward(600)
up()
goto(-300,-100)
down()
forward(600)
up()

goto(-100,300)
setheading(-90)
down()
forward(600)
up()
goto(100,300)
down()
forward(600)
up()
pencolor("grey")

def cross(x,y):
	up()
	goto(x+20,y-20)
	setheading(-45)
	down()
	forward(226)
	up()

def nought(x,y):
	up()
	goto(x+100,y-180)
	setheading(-0)
	down()
	circle(80)
	up()

pieces = ["X","O","X","","O","","X","O",""]
x  = -300
y = 300
for piece in pieces:
	if piece == "x":
		cross(x,y)
	elif piece == "O":
		nought(x,y)
	x = x + 200
	if x > 100:
		x = -300
		y = y - 200