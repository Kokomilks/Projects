import turtle, random

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw donut
t.penup()
t.goto(0, -100)
t.pendown()
t.color("peru")
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw hole
t.penup()
t.goto(0, -50)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw sprinkles
colors = ["red", "blue", "green", "yellow", "purple", "pink"]
for _ in range(15):
    while True:
        x, y = random.randint(-100, 100), random.randint(-100, 100)
        if 50 < (x**2 + y**2) ** 0.5 < 100:  # Ensures sprinkle is in the ring
            break
    t.penup()
    t.goto(x, y)
    t.dot(5, random.choice(colors))

turtle.done()
