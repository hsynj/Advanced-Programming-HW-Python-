import turtle

pen = turtle.Turtle()
turtle.bgcolor("lightblue")
pen.color("black", "white")

pen.begin_fill()

pen.right(45)

for x in range(4):
    pen.forward(100)
    pen.right(90)

pen.forward(200)
pen.left(90)

for x in range(3):
    pen.forward(100)
    pen.left(90)
    
pen.end_fill()

turtle.done()
