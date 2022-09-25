import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from pytube import YouTube


# Downloader Function
def download_mp4_videos(url: str, quality: str):
    try:
        youtube = YouTube(url)
        youtube.streams.filter(file_extension="mp4").get_by_resolution(quality).download()
        tkinter.messagebox.showinfo(title="Download Successful!", message="Video downloaded!!!")

    except Exception:
        tkinter.messagebox.showerror(title="ERROR", message="Check the url!!!")


# Create Window
root = Tk()
root.title("Youtube Video Downloader ©FK")
root.iconbitmap("youtube.ico")
root.config(bg="#ffeeee")
root.geometry("600x200")

# Create Frame include Label Text and Button Widgets
frm = Frame(root)
frm.config(bg="#ffeeee")
frm.grid(padx=30, pady=30)

# Label Widget
Label(frm, text="URL", bg="#ffeeee").grid(column=1, row=0)

# Text Widget
txt = Text(frm, height=2, width=60, bg="#fffaee")
txt.grid(column=0, row=1, columnspan=3)

# Change combobox background color
combo_style = ttk.Style()
combo_style.theme_create('combostyle', parent='alt',
                         settings={'TCombobox':
                                       {'configure':
                                            {'selectbackground': '#fffaee',
                                             'fieldbackground': '#fffaee',
                                             'background': '#fffaee'
                                             }}}
                         )
combo_style.theme_use('combostyle')

# Combobox Widget
qualities = ttk.Combobox(root, state="readonly")
qualities["values"] = ("144p",
                       "240p",
                       "360p",
                       "480p",
                       "720p",
                       "1080p")

qualities.grid(column=0, row=1)
qualities.current(4)

# Button Widget
btn = Button(frm, text="Submit", bg="#fffaee",
             command=lambda: download_mp4_videos(txt.get("1.0", "end-1c"), qualities.get()),
             height=2).grid(column=4, row=1, padx=10)

root.resizable(False, False)
root.mainloop()

