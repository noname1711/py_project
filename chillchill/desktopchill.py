from turtle import *
bgcolor("#000"), setup(500,500,900,90)
hideturtle(),tracer(0),penup()
getcanvas().winfo_toplevel().wm_attributes("-transparentcolor","#000")
getcanvas().winfo_toplevel().attributes('-fullscreen',True)
from math import sin,cos
from time import perf_counter
w=500
def draw():
    update(), clear()
    t=perf_counter()
    for i in range(1,250):
        u=t*99
        a=i+u-u%1
        X=sin(a)*w*59/(i*2-u%1)+(sin(a/w*3))*200
        Y=cos(a)*w*59/(i*2-u%1)+(sin(a/w*3))*100
        goto(X,Y)
        dot(w/i,(1,.5,0))
    ontimer(draw,0)
draw()
mainloop()