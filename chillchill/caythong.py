import turtle as t
import random as r

n = 100.0
t.speed("fastest")
t.screensize(bg='black')
t.left(90)
t.forward(3 * n)
t.color("orange", "yellow")
t.begin_fill()
t.left(126)

for _ in range(5):
    t.forward(n / 5)
    t.right(144)
    t.forward(n / 5)
    t.left(72)
t.end_fill()
t.right(126)

def draw_light():
    rand_num = r.randint(0, 30)
    if rand_num == 0:
        t.color('tomato')
        t.circle(6)
    elif rand_num == 1:
        t.color('orange')
        t.circle(3)
    else:
        t.color('dark green')

t.color("dark green")
t.backward(n * 4.8)

def tree(d, s):
    if d <= 0:
        return
    t.forward(s)
    tree(d - 1, s * .8)
    t.right(120)
    tree(d - 3, s * .5)
    draw_light()
    t.right(120)
    tree(d - 3, s * .5)
    t.right(120)
    t.backward(s)

tree(15, n)
t.backward(n / 2)

for _ in range(200):
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    t.up()
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.down()
    if r.randint(0, 1) == 0:
        t.color('tomato')
    else:
        t.color('wheat')
    t.circle(2)
    t.up()
    t.backward(a)
    t.right(90)
    t.backward(b)
    
t.title("cây thông promax =))")
t.color("dark red", "red")
t.write("Merry Christmas 2023", align="center", font=("Comic Sans MS", 40, "bold"))

def draw_snow():
    t.ht()
    t.pensize(2)
    for _ in range(200):
        t.pencolor("white")
        t.pu()
        t.setx(r.randint(-350, 350))
        t.sety(r.randint(-100, 350))
        t.pd()
        dens = 6
        snowsize = r.randint(1, 10)
        for _ in range(dens):
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            t.right(int(360 / dens))

draw_snow()

t.done()
