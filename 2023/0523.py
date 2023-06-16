from turtle import *


print("python debug start")
print("python debug end")

def drawRectangle():
    width(4)

    forward(200)
    right(90)

    pencolor('red')
    forward(100)
    right(90)

    pencolor('green')
    forward(200)
    right(90)

    pencolor('blue')
    forward(100)
    right(90)

    done()

# drawRectange()


def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

def drawStars():
    for x in range(0, 250, 50):
        drawStar(x, 0)
    done()

drawStars()