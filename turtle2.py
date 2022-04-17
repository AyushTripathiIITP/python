import turtle

a = turtle.Turtle()
a.speed(10)
a.getscreen().bgcolor("#E8630A")

a.color("#001E6C" , "#FCD900")

a.begin_fill()
while( 1 > 0 ):
    a.forward(500)
    a.left(168.365)
    if abs(a.pos()) < 1 :
        break

a.end_fill()
turtle.done()