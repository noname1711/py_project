from turtle import *
from tkinter.ttk import *
from tkinter import *
import time

s=Screen()
s.setup(650,650)
s.bgcolor('black')
s.title("clock")
t3=Turtle()
t=Turtle()
t.pensize(7)
colormode(255)
color=['red','blue','green','cyan','yellow']
clock=Turtle()
clock.color('#4287f5')
clock.speed(10)
clock.pensize(5)
clock.up()
clock.goto(0,-250)
clock.down()
clock.circle(250)
clock.up()
clock.goto(0,0)


for i in range(12):
    clock.color("#29f25f")
    clock.left(30)
    clock.fd(200)
    clock.down()
    clock.bk(20)
    clock.up()
    clock.goto(0,0)


clock.color("#43b552")
clock.dot(10)
clock.up()
clock.goto(0,-255)
clock.down()
clock.color('white')
clock.circle(255)

clock.ht()

def write(message,pos):
    x,y=pos
    clock.up()
    clock.goto(x,y)
    clock.color('white')
    style=("Azeret Mono",18,"bold")
    clock.write(message,font=style)



write("1",(110,180))
write("2",(190,95))
write("3",(220,-15))
write("4",(190,-125))
write("5",(106,-210))
write("6",(-6,-240))
write("7",(-115,-210))
write("8",(-200,-125))
write("9",(-230,-15))
write("10",(-210,95))
write("11",(-130,176))
write("12",(-12,210))



t.begin_poly()
t.fd(150)
t.end_poly()
t2=t.get_poly()
addshape('f',t2)
t.reset()
t.ht()


kimgio=Turtle()
kimgio.shape('f')
kimgio.color('blue')
kimgio.shapesize(0.75,2,4)
kimgio.seth(180)

kimphut=Turtle()
kimphut.shape('f')
kimphut.color('yellow')
kimphut.shapesize(1,2,3)
kimphut.seth(180)

kimgiay=Turtle()
kimgiay.shape('f')
kimgiay.color('red')
kimgiay.shapesize(1,2,2)
kimgiay.seth(180)


clock2=Turtle()
clock2.ht()
def write(message,pos):
    x,y=pos
    clock2.up()
    clock2.goto(x,y)
    clock2.color('white')
    style=("Arial",18,"bold")
    clock2.write(message,font=style)

#tkinter
win = Tk()
win.geometry("650x300")
win.focus()
win.title("Input time")

lb1 = Label(win, text="Input Time", font=("Azeret Mono",20,"bold"),fg="FireBrick")
lb1.place(x=30,y=10)

hr = Label(win, text="Hours", font=("Azeret Mono",13,"bold"),fg="MidnightBlue")
hr.place(x=10,y=50)

mi = Label(win, text="Minutes", font=("Azeret Mono",13,"bold"),fg="DarkOrange")
mi.place(x=10,y=100)

se = Label(win, text="Seconds", font=("Azeret Mono",13,"bold"),fg="darkred")
se.place(x=10,y=150)


combobox1 = Combobox(win,font=("Azeret Mono",12),width=15)
combobox1.place(x=100,y=50)
combobox1['value']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
combobox1.current(0)


combobox2 = Combobox(win,font=("Azeret Mono",12),width=15)
combobox2.place(x=100,y=100)
combobox2['value']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24
                    ,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,
                    45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
combobox2.current(0)


combobox3 = Combobox(win,font=("Azeret Mono",12),width=15)
combobox3.place(x=100,y=150)
combobox3['value']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24
                    ,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,
                    45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
combobox3.current(0)



def getTime():
    clock2.clear()
    write(str(combobox1.get())+" hours",(-180,-285))	
    write(str(combobox2.get())+" minutes",(-70,-285))	
    write(str(combobox3.get())+" seconds",(70,-285))
   
    

but = Button(win, text="GET TIME",width=10,font=("Azeret Mono",13,"bold"),bg="RoyalBlue",fg="white",command=getTime)
but.place(x=10,y=200)


lbl2= Label(win, text="START OR EXIT",font=("Azeret Mono",14,"bold"),fg="maroon")
lbl2.place(x=400,y=50)

tong =0
def start():
    hours=int(combobox1.get())
    minutes=int(combobox2.get())
    seconds=int(combobox3.get())
    tong = int(hours*3600 + minutes*60 + seconds)
    i=0
    for i in range(tong):
        time.sleep(1)
        kimgiay.right(6)
        if i!=0 and i%60==0:
            kimphut.right(6)
            if i!=0 and i%3600==0:
                kimgio.right(30)
            
         
chooseStart = Button(win,text="START",width=10,bg="lime",fg="black",font=("Azeret Mono",13,"bold"),command=start)
chooseStart.place(x=335,y=100)

chooseNo = Button(win,text="EXIT",command=exit,bg="red",fg="black",width=10,font=("Azeret Mono",13,"bold"))
chooseNo.place(x=500,y=100)

def restart():
    kimgiay.seth(180)
    kimphut.seth(180)
    kimgio.seth(180)


chooseRestart = Button(win,text="RESTART",width=10,font=("Azeret Mono",13,"bold"),bg="MediumSeaGreen",fg="white",command=restart)
chooseRestart.place(x=150,y=200)


win.mainloop()
