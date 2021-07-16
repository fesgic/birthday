import tkinter as tk
from tkinter import LEFT, GROOVE

from PIL import ImageTk, Image
import os
import vlc

root = tk.Tk()

root.title("Special one's bash 🥳🥳🥳")
load = Image.open('photos/1.jpg')
render = ImageTk.PhotoImage(load)
root.iconphoto(False, render)
root.geometry("1366x768")
root.config(bg="blue4")
root.resizable(0,0)

def play():
    p = vlc.MediaPlayer('./music/anne-marie_birthday_official_video_mp3_67189-[AudioTrimmer.com].mp3')
    p.play()

def start():
    global i, show
    if i >= (len(images)-1):
        i = 0
        slide_image.config(image = images[i])
    else:
        i = i+1
        slide_image.configure(image = images[i])
    show = slide_image.after(1500, start)

def stop():
    global show
    # All done! Stop and quit the mixer.

def resume():
    start()

basepath = 'photos/'

photos = []
images = []
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        a = f"{basepath}{entry}"
        photos.append(a)

def processing(photos):
    global result
    for i in photos:
        result = Image.open(i)
        b = result.resize((370, 590), Image.ANTIALIAS)
        answer = ImageTk.PhotoImage(b)
        images.append(answer)

processing(photos)



#configure image to label
i = 0
slide_image = tk.Label(root, image=images[i], height=590, width=1366)
slide_image.pack(pady=5, anchor='center')

# create buttons
btn1 = tk.Button(root, text="Start", bg='black', fg='gold', width=6, font=('ariel 20 bold'), relief=GROOVE, command=lambda:[start(),play()])
btn1.pack(side=LEFT, padx=60, pady=50)

btn2 = tk.Button(root, text="Pause/Stop", bg='black', fg='gold', width=10, font=('ariel 20 bold'), relief=GROOVE, command=lambda:[stop()])
btn2.pack(side=LEFT, padx=60, pady=50)

btn3 = tk.Button(root, text="Resume", bg='black', fg='gold', width=8, font=('ariel 20 bold'), relief=GROOVE, command=lambda:[resume()])
btn3.pack(side=LEFT, padx=60, pady=50)

btn4 = tk.Button(root, text="Exit", bg='black', fg='gold', width=6, font=('ariel 20 bold'), relief=GROOVE, command=root.destroy)
btn4.pack(side=LEFT, padx=30, pady=50)

root.mainloop()