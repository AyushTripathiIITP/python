import turtle

bob = turtle.Turtle()

bob.color("green", "red")

bob.begin_fill()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill()

bob.penup()
bob.forward(50)
bob.pendown()
bob.begin_fill()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill()
turtle.done()
