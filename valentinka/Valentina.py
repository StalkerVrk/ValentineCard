import math
import turtle


logo = r'''
(c)StalkerVrk
'''
print(logo)

def forHor(t):
    return 16 * math.sin(t) ** 3

def forVert(t):
    return 13 * math.cos(t) - 5 * \
        math.cos(2 * t) - 2 * \
        math.cos(3 * t) - \
        math.cos( 4 * t)

try:
    t = turtle.Turtle()
    t.speed(5000)
    turtle.colormode(255)
    turtle.Screen().bgcolor(0, 0, 0)
    for i in range(2550):
        t.goto((forHor(i) * 20, forVert(i) * 20))
        t.pencolor((255 - 1) % 255, 1 % 255, (255 + 1) % 255)
        t.goto(0, 0)

    t.hideturtle()
    turtle.update()
    turtle.mainloop() 
except BaseException:
    print("С 14 февреля. Пока-пока.")