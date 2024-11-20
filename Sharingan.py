import turtle

turtle.title("Sharingan")
turtle.setup(width=800, height=800)
turtle.bgcolor('dark red')
turtle.pensize(3)
turtle.speed(5)

def outercircle():
    turtle.color('black')
    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()

    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()

def redcircle():
    turtle.color('dark red')
    turtle.penup()
    turtle.goto(0,-190)
    turtle.pendown()

    turtle.begin_fill()
    turtle.circle(190)
    turtle.end_fill()

def innercircle():
    turtle.color('black')
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.circle(100)

def blackcircle():
    turtle.color('black')
    turtle.penup()
    turtle.goto(0,-20)
    turtle.pendown()

    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

def circle():
    outercircle()
    redcircle()
    innercircle()
    blackcircle()

def curve01(a,d):
    for i in range(d):
        turtle.right(a)
        turtle.forward(1)

def curve02(a,d):
    for i in range(d):
        turtle.left(a)
        turtle.forward(1)

def tomoe(pos, ang):
    
    turtle.color('black')
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.seth(ang)
    turtle.begin_fill()
    curve02(2.3, 120)
    turtle.right(118)
    curve01(2, 50)
    turtle.left(165)
    curve02(1.42, 130)
    turtle.end_fill()


circle()

tomoe((-13,87), -60)
tomoe((-63,-57), 50)
tomoe((98,-12), 160)

turtle.hideturtle()
turtle.done()