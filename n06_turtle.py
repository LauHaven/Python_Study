# 第一个抛砖引玉的程序，使用几句话绘图

import turtle as t
import math as m

pi = 3.1415926
cl = ("red", "green", "blue", "black", "orange", "gray", "pink")
# drawing 同心circle
t.clear()
t.speed(50)
t.width(2)
for i in range(0, 350, 5):
    t.penup()
    t.goto(0, -i)
    t.color(cl[(i // 5) % (len(cl))])
    t.pendown()
    t.circle(10 + i)

# drawing a rectangle
t.clear()
t.speed(50)
t.width(2)
t.penup()
t.goto(0, 0)
t.pendown()
for x in range(100):
    t.color(cl[(x // 5) % (len(cl))])
    t.forward(3 * x)
    t.right(90)


# drawing a triangle
t.clear()
t.speed(50)
t.width(2)
t.penup()
t.goto(0, 0)
t.pendown()
for x in range(120):
    t.color(cl[(x // 5) % (len(cl))])
    t.forward(5 * x)
    t.right(120)


# drawing x axis
t.clear()
t.speed(50)
t.width(2)
t.penup()
t.goto(-350, -100)
t.color('black')
t.width(2)
t.pendown()
t.goto(350, -100)
t.penup()
# drawing y axis
t.goto(-300, 100)
t.pendown()
t.goto(-300, -300)
t.penup()

# drawing sin formular
t.goto(-300, -100)
t.width(1)
t.color("red")
t.pendown()
for T in range(5):
    for x in range(200):
        X = (T * 2 * pi) + (2 * pi / 200) * x
        Y1 = m.sin(X) * 50
        t.goto(-300 + 20 * X, -100 + Y1)
t.penup()

t.goto(-300, -100)
t.color("green")
t.pendown()
for T in range(5):
    for x in range(200):
        X = (T * 2 * pi) + (2 * pi / 200) * x
        Y2 = m.sin(X + 2 * pi / 3) * 50
        t.goto(-300 + 20 * X, -100 + Y2)
t.penup()

t.goto(-300, -100)
t.color("blue")
t.pendown()
for T in range(5):
    for x in range(200):
        X = (T * 2 * pi) + (2 * pi / 200) * x
        Y3 = m.sin(X + 2 * pi * 2 / 3) * 50
        t.goto(-300 + 20 * X, -100 + Y3)
t.penup()

# drawing grid
t.clear()
t.width(2)
t.speed(50)
for i in range(-200, 220, 20):
    t.penup()
    t.goto(-200, i)
    t.color(cl[(i // 20) % len(cl)])
    t.pendown()
    t.goto(200, i)
for j in range(-200, +220, 20):
    t.penup()
    t.goto(j, -200)
    t.color(cl[(j // 20) % len(cl)])
    t.pendown()
    t.goto(j, 200)
t.done()
