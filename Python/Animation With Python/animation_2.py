import turtle
amy = turtle.Turtle()
amy.color("cyan")
amy.speed(0)
colors = ["green","black","orange","navy","lightblue","purple","#d3f122","darkblue"]
def drow_square(color):
	for side in range(4):
		amy.forward(100)
		amy.right(90)
		for side in range(4):
			amy.forward(50)
			amy.right(90)

amy.penup()
amy.back(40)
amy.pendown()

for color in colors:
	amy.color(color)
	drow_square(color)
	amy.forward(50)
	amy.left(45)

amy.hideturtle()