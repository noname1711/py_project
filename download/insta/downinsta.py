import tkinter as tk
from tkinter import ttk
import requests
import os
from bs4 import BeautifulSoup
import pyperclip

def download_video():
    url = entry_url.get()
    if not url.startswith("https://www.instagram.com/"):
        status_label.config(text="Invalid Instagram URL")
        return

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    video_url = soup.find("meta", property="og:video")["content"]
    
    download_path = entry_path.get()  # Lấy đường dẫn từ ô nhập
    video_data = requests.get(video_url).content
    video_filename = os.path.join(download_path, "instagram_video.mp4")
    
    with open(video_filename, "wb") as video_file:
        video_file.write(video_data)

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

