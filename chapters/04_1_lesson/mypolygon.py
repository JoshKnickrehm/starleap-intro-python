import time
import turtle
bob = turtle.Turtle()
james = turtle.Turtle()
##########################67
# bob.pensize(10)
# bob.speed(1000000)
# for i in range(160):
#     bob.fd(1)
#     bob.rt(2)
# bob.fd(70)
# bob.rt(40)
# bob.pu()
# bob.fd(30)
# bob.pd()
# bob.fd(width)
# bob.rt(110)
# bob.fd(110)

####################Cube
def rgb_to_hex(r,g,b):
    return f"#{r:02x}{g:02x}{b:02x}"

width = 10
james.goto(100,100)
s = turtle.Screen()
s.tracer(0,0)
james.pensize(5)
bob.pensize(5)
for i in range(100):
    width = 10 + i*10 % 100
    james.pencolor(rgb_to_hex(i*10 % 200,100,200))
    bob.pd()
    bob.rt(36)

    for i in range(4):
        bob.fd(width)
        bob.lt(90)
    bob.fd(width)
    bob.lt(45)
    bob.fd(35)
    bob.lt(45)
    bob.fd(width)
    bob.lt(135)
    bob.fd(35)
    bob.rt(45)
    bob.fd(width)
    bob.rt(135)
    bob.fd(35)
    bob.rt(45)
    bob.fd(width)
    bob.pu()
    bob.goto(0,0)
    james.pd()
    james.rt(36)

    for i in range(4):
        james.fd(width)
        james.lt(90)
    james.fd(width)
    james.lt(45)
    james.fd(35)
    james.lt(45)
    james.fd(width)
    james.lt(135)
    james.fd(35)
    james.rt(45)
    james.fd(width)
    james.rt(135)
    james.fd(35)
    james.rt(45)
    james.fd(width)
    james.pu()
    james.goto(100,100)
    s.update()
    time.sleep(1/10)
    james.clear()
    bob.clear()


turtle.exitonclick()