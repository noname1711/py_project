from tkinter import *
from PIL import Image 
import qrcode

def on_entry_click(event):
    if entry.get() == 'Nhập link: ':
        entry.delete(0, "end")
        entry.insert(0, '')
        entry.config(fg='red')

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0,'Nhập link: ')
        entry.config(fg="grey")

root =Tk()
root.title("APP chuyển về qr")
root.geometry("495x565")
label=Label(root, text="Link: ")
label.pack()
entry=Entry(root,bd=1)
entry.insert(0,'Nhập link: ')
entry.bind('<FocusIn>',on_entry_click)
entry.bind('<FocusOut>',on_focusout)
entry.config(fg='grey')
entry.pack()
# mã qr hiện ở C:\Users\Test
def myClick():
    data=entry.get()
    img= qrcode.make(data)
    img=img.resize((490,490),Image.HAMMING)
    img.save('qr.png')   #sau mỗi lần dùng nhớ đổi tên
    photo= PhotoImage(file="qr.png")  #sau mỗi lần dùng nhớ đổi tên
    imag=Label(root,image=photo)
    imag.pack()
    cv= Canvas(root,width=200,height=100)
    cv.pack(side='top',fill='both',expand='yes')
    cv.photo=PhotoImage(file="qr.png") #sau mỗi lần dùng nhớ đổi tên
    cv.create_image(0, 0, image=cv.photo, anchor="nw")
    cv.create_image(10,10, image=img, anchor='nw')

MyButton =Button(root, text="Generate", command=myClick)
MyButton.pack()

root.mainloop()
