import turtle
import os
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Strategy")
#field
border_pen = turtle.Turtle() 
border_pen.speed(0) 
border_pen.color("white") 
border_pen.penup() 
border_pen.setposition(-300, -300) 
border_pen.pendown() 
border_pen.pensize(3) 
for side in range(4): 
	border_pen.fd(600) 
	border_pen.lt(90) 
	border_pen.hideturtle() 
#player
player = turtle.Turtle()
player.color("blue") 
player.shape("triangle") 
player.penup() 
player.speed(0) 
player.setposition(0, -250) 
player.setheading(90) 
#Move
playerspeed = 15 
#leftright
def move_left(event): 
	x = player.xcor() 
	x -= playerspeed 
	if x < -280: 
		x = -280 
	player.setx(x) 
def move_right(event): 
	x = player.xcor() 
	x += playerspeed 
	if x > 280: 
		x = 280 
	player.setx(x) 
#Keybinding 
turtle.listen() 
turtle.getcanvas().bind("<Left>", move_left) 
turtle.getcanvas().bind("<Right>", move_right) 
turtle.mainloop()