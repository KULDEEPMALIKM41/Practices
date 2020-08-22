import turtle
import time
time.sleep(10)
romio = turtle.Turtle()
julit = turtle.Turtle()

romio.color("red")
romio.width(3)

julit.color("violet")
julit.width(3)

julit_last_name = "montague"

julit.left(40)
julit.forward(100)

for side in range(185):
	julit.forward(1)
	julit.left(1)
julit.hideturtle()

if julit_last_name == 'montague':
	romio.left(140)
	romio.forward(100)
	for side in range(185):
		romio.forward(1)
		romio.right(1) 
	time.sleep(5)
