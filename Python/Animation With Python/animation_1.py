import turtle
amy = turtle.Turtle()
amy.color("cyan")
amy.speed(0)
def drow_square(length):
	for side in range(4):
		amy.forward(length)
		amy.right(90)
		for side in range(4):
			amy.forward(50)
			amy.right(90)

amy.penup()
amy.back(20)
amy.pendown()

for square in range(80):
	drow_square(5)
	amy.forward(5)
	amy.right(5)

amy.hideturtle()