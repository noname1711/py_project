import tkinter as tk
from tkinter import ttk
import pyperclip
from pyinstalive import Client
import os

def download_video():
    url = entry_url.get()
    if not url.startswith("https://www.instagram.com/p/"):
        status_label.config(text="Invalid Instagram URL")
        return

    with Client() as client:
        video = client.download(url)
        download_path = entry_path.get()
        video_filename = os.path.join(download_path, "instagram_video.mp4")
        video.save(video_filename)
        status_label.config(text="Video downloaded successfully!")

def paste_from_clipboard():
    url = pyperclip.paste()
    entry_url.delete(0, 'end')
    entry_url.insert(0, url)

app = tk.Tk()
app.title("Instagram Video Downloader")

frame = ttk.Frame(app)
frame.grid(column=0, row=0, padx=10, pady=10)

label = ttk.Label(frame, text="Enter Instagram URL:")
label.grid(column=0, row=0)

entry_url = ttk.Entry(frame, width=40)
entry_url.grid(column=1, row=0)

label_path = ttk.Label(frame, text="Download Path:")
label_path.grid(column=0, row=1)

entry_path = ttk.Entry(frame, width=40)
entry_path.grid(column=1, row=1)

download_button = ttk.Button(frame, text="Download", command=download_video)
download_button.grid(column=0, row=2, columnspan=2)

paste_button = ttk.Button(frame, text="Paste from Clipboard", command=paste_from_clipboard)
paste_button.grid(column=0, row=3, columnspan=2)

status_label = ttk.Label(frame, text="")
status_label.grid(column=0, row=4, columnspan=2)

app.mainloop()
