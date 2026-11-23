import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Blue Robotic Cat")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)          # Drawing speed (1 = slowest, 10 = fastest, 0 = instant)
t.pensize(2)

def draw_circle(x, y, r, color):
    t.penup()
    t.goto(x, y - r)
    t.setheading(0)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# -----------------------
# Head
# -----------------------
draw_circle(0, 120, 120, "#29A8E0")

# Face
draw_circle(0, 90, 95, "white")

# Eyes
draw_circle(-28, 170, 22, "white")
draw_circle(28, 170, 22, "white")

# Pupils
draw_circle(-20, 165, 6, "black")
draw_circle(20, 165, 6, "black")

# Nose
draw_circle(0, 135, 10, "red")

# Nose line
t.penup()
t.goto(0, 125)
t.pendown()
t.goto(0, 55)

# Smile
t.penup()
t.goto(-55, 70)
t.setheading(-60)
t.pendown()
t.circle(65, 120)

# Whiskers
for y in [110, 90, 70]:
    # Left
    t.penup()
    t.goto(-10, y)
    t.pendown()
    t.goto(-95, y + 10)

    # Right
    t.penup()
    t.goto(10, y)
    t.pendown()
    t.goto(95, y + 10)

# -----------------------
# Collar
# -----------------------
t.penup()
t.goto(-90, 10)
t.pendown()
t.pensize(8)
t.pencolor("red")
t.goto(90, 10)

# Bell
t.pensize(2)
draw_circle(0, -5, 18, "gold")

t.penup()
t.goto(0, -5)
t.pendown()
t.circle(5)

t.penup()
t.goto(-8, -10)
t.pendown()
t.goto(8, -10)

# -----------------------
# Body
# -----------------------
t.penup()
t.goto(-85, 0)
t.pendown()
t.color("black", "#29A8E0")
t.begin_fill()

t.goto(-100, -150)
t.goto(100, -150)
t.goto(85, 0)
t.goto(-85, 0)

t.end_fill()

# Belly
draw_circle(0, -60, 70, "white")

# -----------------------
# Pocket (Fixed Position)
# -----------------------
t.color("black")
t.pensize(2)

t.penup()
t.goto(-45, -40)
t.setheading(0)
t.pendown()

t.circle(45, 180)

t.penup()
t.goto(-45, -40)
t.pendown()
t.goto(45, -40)

# -----------------------
# Left Hand
# -----------------------
t.penup()
t.goto(-85, -10)
t.pendown()
t.goto(-135, -60)
draw_circle(-145, -70, 15, "white")

# Right Hand
t.penup()
t.goto(85, -10)
t.pendown()
t.goto(135, -60)
draw_circle(145, -70, 15, "white")

# -----------------------
# Left Leg
# -----------------------
t.penup()
t.goto(-45, -150)
t.pendown()
t.goto(-45, -200)
draw_circle(-65, -210, 20, "white")

# Right Leg
t.penup()
t.goto(45, -150)
t.pendown()
t.goto(45, -200)
draw_circle(65, -210, 20, "white")

# Tail
t.penup()
t.goto(100, -120)
t.setheading(-30)
t.pendown()
t.forward(40)

t.hideturtle()
turtle.done()