import turtle

turtle.title("Mangekyou Sharingan")
turtle.setup(width=800, height=800)
turtle.bgcolor('dark red')
turtle.pensize(3)
turtle.speed(5)

#drawing black circle
def circle():
    
    turtle.color('black')
    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()

    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()

#drawing symbols within black circle
def curve(pos, ang):
    turtle.color('dark red')

    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.seth(ang)
    turtle.begin_fill()
    turtle.circle(-380,60)
    turtle.right(120)
    turtle.circle(-380,60)
    turtle.end_fill()

#drawing borderlines for symbols
def curvelines(pos, ang):
    turtle.color('black')
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.seth(ang)
    turtle.circle(-380,60)
    turtle.right(120)
    turtle.circle(-380,60)

#drawing inner black circle
def innercircle(pos):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


#output the sharingan
circle()
curve((0,190), -60)
curve((-164.5,95), 0)
curve((170.5,100), -118)
curvelines((0,190), -60)
curvelines((-164.5,95), 0)
curvelines((170.5,100), -118)
innercircle((5.0,-18.0))

turtle.hideturtle()
turtle.done()