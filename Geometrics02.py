import turtle

turtle.setup(width=800, height=800)
turtle.bgcolor('black')
turtle.hideturtle()
turtle.pensize(1)
turtle.speed(0)

#drawing inner sphere
for i1 in range(15):
    for j1 in [(1.00, 0.10, 0.00), (1.00, 0.30, 0.00), (1.00, 0.50, 0.00), (1.00, 0.70, 0.00), (1.00, 1.00, 0.00)]:

        turtle.circle(100)
        turtle.color(j1)
        turtle.left(5)

#drawing outer sphere
for i2 in range(10):
    for j2 in [(0.00, 1.00, 0.00), (1.00, 0.90, 0.00), (1.00, 0.80, 0.00), (1.00, 0.70, 0.00), (1.00, 0.60, 0.00)]:

        turtle.circle(150)
        turtle.color(j2)
        turtle.left(10)

turtle.done()
