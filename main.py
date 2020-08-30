import tkinter as tk
import cv2  #opencv-python
import PIL.Image, PIL.ImageTk #pillow
from functools import partial
import threading
import imutils
import time


# width and height of screen
SET_WIDTH = 855
SET_HEIGHT = 517
stream = cv2.VideoCapture("clip.mp4")
blink = True # fro blinking the pending text

def play(speed):
    global stream
    global blink

    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed,frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0,0, image=frame, anchor=tk.NW)
    if blink:
        canvas.create_text(150,30, fill="red", font="Times 30 bold", text="Decision panding")
    blink = not blink
    print(f"play with {num}")


def pending(decision):
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tk.NW)
    time.sleep(1)

    frame = cv2.cvtColor(cv2.imread("sponser.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tk.NW)
    time.sleep(2)
    if decision == 'out':
        decisionImg = "out.png"
    else:
        decisionImg = "notout.png"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tk.NW)




def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("out")

def not_out():
    thread = threading.Thread(target=pending, args=("notout",))
    thread.daemon = 1
    thread.start()
    print("not out")


root = tk.Tk()
root.title("Sonu's Third Umpire Decision Program")

cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tk.Canvas(root, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, ancho=tk.NW, image=photo)
canvas.pack()


btn = tk.Button(root, text="<< Previous (fast)", width=50, command=partial(play, 25))
btn.pack()

btn = tk.Button(root, text="<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tk.Button(root, text="Next (slow) >>", width=50, command=partial(play, 2))
btn.pack()

btn = tk.Button(root, text="Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tk.Button(root, text="OUT", width=50, command=out)
btn.pack()

btn = tk.Button(root, text="NOT OUT", width=50, command=not_out)
btn.pack()

root.mainloop()