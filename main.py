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
# for streaming video 
stream = cv2.VideoCapture("clip.mp4")
blink = True # fro blinking the pending text

def play(speed):
    global stream
    global blink
    # getting the current frame of video 
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    #  setting the new modified frame for video according to input 
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    # reading the new frame and it will return 1st boolian value and 2nd frame 
    grabbed,frame = stream.read()
    if not grabbed:
        exit()
    # resizing the frame into default height and width 
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0,0, image=frame, anchor=tk.NW)
    # this is for blinking text 
    if blink:
        canvas.create_text(150,30, fill="red", font="Times 30 bold", text="Decision panding")
    blink = not blink
    print(f"play with {num}")


def pending(decision):
    # getting image and displaying after processing it 
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tk.NW)
    #  to wait some time 
    time.sleep(1)
         # getting image and displaying after processing it 
    frame = cv2.cvtColor(cv2.imread("sponser.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tk.NW)
    time.sleep(2)
    #   condition for displaying a specific image 
    if decision == 'out':
        decisionImg = "out.png"
    else:
        decisionImg = "notout.png"
         # getting image and displaying after processing it 
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tk.NW)




def out():
    # creating thread for run function while running mainscreen loop ,function name at target and all arguments at args
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("out")

def not_out():
    # creating thread for run function while running mainscreen loop ,function name at target and all arguments at args
    thread = threading.Thread(target=pending, args=("notout",))
    thread.daemon = 1
    thread.start()
    print("not out")

#   making display
root = tk.Tk()
# setting title of app
root.title("Sonu's Third Umpire Decision Program")
  
#  displaying image after geting and changing height width and pil from array using canvas
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tk.Canvas(root, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, ancho=tk.NW, image=photo)
canvas.pack() #packing canvas to display

#    creating and displaying buttons on screen , command for running function on click
#  and using partial for passing arguments with function 
btn = tk.Button(root, text="<< Previous (fast)", width=50, command=partial(play, 25))
btn.pack()   # always pack after making and graphic changes

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

root.mainloop()  #runnning main window loop