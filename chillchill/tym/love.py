import turtle
import time
from pygame import mixer

# Adding music is optional as per your choice.
# Initialize pygame mixer
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("cute.mp3")# Add music

# importing turtle
t = turtle.Turtle()


def curve():
    t.pen(pencolor="white", pensize=3, speed=5)
    for i in range(200):
        t.rt(1)
        t.fd(1)

def love_sign():
    t.pen(pencolor="white",fillcolor="hot pink", pensize=3, speed=5)
    t.shape("turtle")
    t.shapesize(1,1,1)
    t.begin_fill()
    t.lt(50)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

    t.hideturtle()


window = turtle.Screen()
window.title("Tặng bé con của a =))")
window.bgcolor('black')
window.screensize(800, 700)
window.setup(width=1.0, height=1.0, startx=None, starty=None)

# Play Music
mixer.music.play()

t.penup()
t.goto(-80,300)
time.sleep(1)
t.pendown()
t.shapesize(1,2,1)

# ==============="I"==================
t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)

t.begin_fill()

t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)
# ===========Height of the 'I'=========
t.fd(140)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(140)
t.left(90)
t.fd(60)
t.rt(90)
t.fd(25)

t.end_fill()

# =========================================


t.penup()
t.goto(-550,-20)
t.pendown()


# ===============Love Part=================
# ================="L"=====================
t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.rt(90)
t.fd(25)
t.rt(90)
t.fd(165)
t.lt(90)
t.fd(115)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(140)
t.rt(90)
t.fd(190)
t.rt(90)

t.end_fill()
# ======================================

t.penup()
t.fd(140)

#Gap between "L" and "O"
t.fd(70)

# ================="O"=================
t.pen(pencolor="white",fillcolor="cyan", pensize=3, speed=8)
t.begin_fill()

t.rt(90)
t.fd(190)
t.lt(90)
t.pendown()
t.circle(60)
t.lt(90)
t.penup()
t.fd(20)
t.rt(90)
t.pendown()
t.circle(40)
t.rt(90)
t.penup()
t.fd(20)
t.lt(90)

t.end_fill()
# =======================================

#Gap between "O" and "V"
t.fd(100)
t.pendown()

# ================"V" part==============
t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.lt(100)
t.fd(120)
t.rt(100)
t.fd(20)
t.rt(80)
t.fd(100)
t.lt(80)
t.fd(20)
t.lt(80)
t.fd(100)
t.rt(80)
t.fd(20)
t.rt(100)
t.fd(120)
t.rt(80)
t.fd(50)
t.lt(180)

t.end_fill()
# ======================================

t.penup()
t.fd(100)
t.pendown()

# ================="E"=================

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.lt(90)
t.fd(120)
t.rt(90)
t.fd(80)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(80)

t.end_fill()
# =====================================

t.penup()
t.rt(180)
#Gap between "V" and "E"
t.fd(200)
t.pendown()

# ==================Y letter=================

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.lt(90)
t.fd(50)
t.lt(30)
t.fd(80)
t.rt(120)
t.fd(20)
t.rt(60)
t.fd(60)
t.lt(180)
t.rt(60)
t.fd(60)
t.rt(60)
t.fd(20)
t.rt(120)
t.fd(80)
t.lt(30)
t.fd(50)
t.rt(90)
t.fd(20)
t.rt(180)

t.end_fill()
# ========================================

t.penup()
t.fd(120)
t.pendown()

# ================"O"==================

t.pen(pencolor="white",fillcolor="cyan", pensize=3, speed=8)
t.begin_fill()

t.circle(60)
t.lt(90)
t.penup()
t.fd(20)
t.pendown()
t.rt(90)
t.circle(40)
t.rt(90)
t.penup()
t.fd(20)
t.lt(90)

t.end_fill()
# ====================================

# Gap between "O" and "U"
t.fd(100)
t.circle(60, extent=60)
t.pendown()

# ===============U part==============

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.lt(30)
# Height of "U"
t.fd(85)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(70)
t.circle(-20, extent=180)
t.fd(70)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(85)
t.circle(40, extent=180)

t.end_fill()
#  ==================================

t.penup()
# t.goto(300,130)
t.rt(180)
t.fd(35)
t.lt(90)
t.fd(140)
t.lt(90)
t.pendown()

# Calling the function for Love Sign
love_sign()

time.sleep(5)