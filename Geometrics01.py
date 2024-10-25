import turtle

turtle.reset
turtle.bgcolor('black')
turtle.setup(width=900, height=900)
turtle.title("Geometrical Wormhole")

colors = ((1.00, 0.10, 0.00), (1.00, 0.30, 0.00), (1.00, 0.50, 0.00), (1.00, 0.70, 0.00), (1.00, 1.00, 0.00))

geo = turtle.Turtle()
geo.hideturtle()
geo.pensize(1)
geo.speed(0)

p = 300
c = 0

#drawing squares
for i in range(181):
    for j in range(4):
        geo.forward(p)
        geo.right(90)
        geo.pencolor(colors[c])
        
    i +=1

    if i > 36:
        p = 211
        c = 1

    if i > 72:
        p = 147
        c = 2

    if i > 108:
        p = 102
        c = 3

    if i > 144:
        p = 69
        c = 4

    geo.right(10)

#drawing circle
geo.penup()
geo.pencolor('red')
geo.goto(-76,-423)
geo.pendown()
geo.circle(428)

turtle.done()

