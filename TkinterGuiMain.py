import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import cv2
import face_recognition
import glob
import os
import numpy as np
from time import strftime

names = []
images = []

myFont = ImageFont.truetype('FreeMono.ttf', 30)
path = "C:\Robotics\0PyCharm\facedata"
for file in glob.glob(path):
    image = cv2.imread(file)
    a = os.path.basename(file)
    b = os.path.splitext(a)[0]
    names.append(b)
    images.append(image)


def encoding1(images):
    encode = []

    for img in images:
        unk_encoding = face_recognition.face_encodings(img)[0]
        encode.append(unk_encoding)
    return encode


encodelist = encoding1(images)


# --- functions ---

def quitapp():
    button_play['state'] = 'normal'
    button_stop['state'] = 'normal'
    button_facedt['state'] = 'normal'
    button_facereco['state'] = 'normal'
    button_quit['state'] = 'disabled'


def datetime():
    #now.strftime("%a %m %y")
    pass

def facerecognition():
    global run_camera

    if not run_camera:
        run_camera = True

        button_play['state'] = 'normal'
        button_stop['state'] = 'normal'
        button_facedt['state'] = 'normal'
        button_facereco['state'] = 'disabled'
        button_quit['state'] = 'normal'
        update_image()


def facedetect():
    global run_camera

    if not run_camera:
        run_camera = True

        button_play['state'] = 'normal'
        button_stop['state'] = 'normal'
        button_facedt['state'] = 'disabled'
        button_facereco['state'] = 'normal'
        button_quit['state'] = 'normal'
        update_image()


def play():
    '''
    start stream (run_camera and update_image)
    and change state of buttons
    '''

    global run_camera

    if not run_camera:
        run_camera = True

        button_play['state'] = 'disabled'
        button_stop['state'] = 'normal'
        button_facedt['state'] = 'normal'
        button_facereco['state'] = 'normal'
        button_quit['state'] = 'normal'
        update_image()


def stop():
    '''
    stop stream (run_camera)
    and change state of buttons
    '''
    global run_camera

    if run_camera:
        run_camera = False

        button_play['state'] = 'normal'
        button_stop['state'] = 'disabled'
        button_facedt['state'] = 'normal'
        button_facereco['state'] = 'normal'
        button_quit['state'] = 'normal'


def update_image():
    '''executed frequencally, it updates frame/image on canvas'''

    # read one frame (and "return" status)
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame1 = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)

    if ret is None:
        print("Can't read from camera")
    else:
        image = Image.fromarray(frame)

        if button_facereco['state'] == 'disabled':
            face_locations = face_recognition.face_locations(frame)
            curframe_encoding = face_recognition.face_encodings(frame1, face_locations)

            for encodeface, facelocation in zip(curframe_encoding, face_locations):
                results = face_recognition.compare_faces(encodelist, encodeface)
                distance = face_recognition.face_distance(encodelist, encodeface)
                match_index = np.argmin(distance)
                name = names[match_index]
                top, right, bottom, left = facelocation

                draw = ImageDraw.Draw(image)
                draw.rectangle([left, top, right, bottom], outline="green")
                draw.text((left, top), name, font=myFont, fill=(255, 0, 0))
        if button_facedt['state'] == 'disabled':
            face_location = face_recognition.face_locations(frame)
            for face_locationn in face_location:
                top, right, bottom, left = face_locationn

                draw = ImageDraw.Draw(image)
                draw.rectangle([left, top, right, bottom], outline="red")

        photo.paste(image)

    if run_camera:
        root.after(10, update_image)


def clock():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, clock)


def quitapp():
    root.destroy()


# --- main ---

# open stream
cap = cv2.VideoCapture(0)  # local (built-in) camera

# check if opened
if not cap.isOpened():
    print("Can't open camera")
    cap.release()
    exit(1)

# get first frame
ret, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
if ret is None:
    print("Can't read from camera")
    cap.release()
    exit(1)

# ---

# control stream on canvas
run_camera = False

# ---

root = tk.Tk()
# name_var=tk.StringVar()
image = Image.fromarray(frame)
photo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=photo.width(), height=photo.height())
canvas.pack(fill='both', expand=True)

canvas.create_image((0, 0), image=photo, anchor='nw')

# ---
# label=tk.Label(root,fg="white", bg="black")

label = tk.Label(root, font="Calibri, 20")
label.pack(side='left')
buttons = tk.Frame(root)
buttons.pack(fill='x')

button_play = tk.Button(buttons, text="Play", command=play)
button_play.pack(side='left')

button_stop = tk.Button(buttons, text="Stop", command=stop, state='disabled')
button_stop.pack(side='left')

button_facedt = tk.Button(buttons, text="Facedetect", command=facedetect)
button_facedt.pack(side='left')

button_facereco = tk.Button(buttons, text="Facereco", command=facerecognition)
button_facereco.pack(side='left')

button_quit = tk.Button(buttons, text="Quit", command=quitapp)
button_quit.pack(side='left')

clock()
root.mainloop()

# ---

# close stream
cap.release()