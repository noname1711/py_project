import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import pyperclip

def download_video():
    url = entry_url.get()
    youtube_video = YouTube(url)
    video_stream = youtube_video.streams.filter(progressive=True, file_extension="mp4").first()
    video_stream.download()
    status_label.config(text="down xong video !!!!")

def paste_from_clipboard():
    url = pyperclip.paste()
    entry_url.delete(0, 'end')
    entry_url.insert(0, url)

app = tk.Tk()
app.title("app down video youtube")

frame = ttk.Frame(app)
frame.grid(column=0, row=0, padx=10, pady=10)

label = ttk.Label(frame, text="Nhập URL ở đây:")
label.grid(column=0, row=0)

entry_url = ttk.Entry(frame, width=40)
entry_url.grid(column=1, row=0)

download_button = ttk.Button(frame, text="Download", command=download_video)
download_button.grid(column=2, row=0)

paste_button = ttk.Button(frame, text="paste đường link", command=paste_from_clipboard)
paste_button.grid(column=0, row=1, columnspan=3)

status_label = ttk.Label(frame, text="")
status_label.grid(column=0, row=2, columnspan=3)

app.mainloop()
