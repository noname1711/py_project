import pygame
import time
from tkinter import Listbox
from tkinter import PhotoImage
import os
from tkinter.filedialog import *
from tkinter import Tk, Button
import sys

pygame.mixer.init()


par = 1
playlist = []

player = Tk()
player.title("Máy phát nhạc")
player.state("iconic")


def select_dir():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith("mp3"):
            playlist.append(files)

    for t in playlist:
        listbox.insert(0, t)


def play_music():
    b = listbox.curselection()[0]
    global i
    i = len(playlist) - b - 1
    global paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        stop_music()
        time.sleep(1)
        pygame.mixer.music.load(playlist[i])
        pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


paused = False


def pause_music():
    global paused
    paused = True
    pygame.mixer.music.pause()


def nxt():
    global i
    i -= 1
    pygame.mixer.pre_init(44100, -16, 2, 1024)
    pygame.mixer.init()
    pygame.mixer.music.load(playlist[i])
    pygame.mixer.music.play()


def prev():
    global i
    i += 1
    pygame.mixer.pre_init(44100, -16, 2, 1024)
    pygame.mixer.init()
    pygame.mixer.music.load(playlist[i])
    pygame.mixer.music.play()


playImage = PhotoImage(file="play.png")
nextImage = PhotoImage(file="next.png")
prevImage = PhotoImage(file="priv.png")
listImage = PhotoImage(file="list.png")
exitImage = PhotoImage(file="exit.png")
pauseImage = PhotoImage(file="pause.png")
stopImage = PhotoImage(file="stop.png")

pl = playImage.subsample(3, 3)
ps = pauseImage.subsample(3, 3)
nx = nextImage.subsample(3, 3)
prv = prevImage.subsample(3, 3)
lst = listImage.subsample(3, 3)
pwr = exitImage.subsample(3, 3)
st = stopImage.subsample(3, 3)

bt1 = Button(player, text="play", command=play_music, image=pl)
bt1.config(height=40, width=40)
bt2 = Button(player, text="pause", command=pause_music, image=ps)
bt2.config(height=40, width=40)
bt3 = Button(player, text="prev", image=prv, command=prev)
bt3.config(height=40, width=40)
bt4 = Button(player, text="next", image=nx, command=nxt)
bt4.config(height=40, width=40)
bt5 = Button(player, text="stop", image=st, command=stop_music)
bt5.config(height=40, width=40)
bt6 = Button(player, text="list", command=select_dir, image=lst)
bt6.config(height=40, width=40)
bt7 = Button(player, text="exit", image=pwr, command=sys.exit)
bt7.config(height=40, width=40)
bt1.grid(column=0, row=0, padx=2, pady=2)
bt2.grid(column=1, row=0, padx=2, pady=2)
bt3.grid(column=2, row=0, padx=2, pady=2)
bt4.grid(column=3, row=0, padx=2, pady=2)
bt5.grid(column=4, row=0, padx=2, pady=2)
bt6.grid(column=5, row=0, padx=2, pady=2)
bt7.grid(column=6, row=0, padx=2, pady=2)
listbox = Listbox(player, relief='sunken', width=30, height=20)
listbox.grid(row=1, columnspan=8)

player.mainloop()