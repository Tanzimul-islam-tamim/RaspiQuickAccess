from guizero import App, PushButton, Window
from gpiozero import LED
import sys
import os
import time


app = App('Leed', height = 500, width = 900)
infowindow = Window(app, title = "Input Name",height = 500, width = 900)
infowindow.hide()

def FaceRecogButton():
    os.system("espeak 'Facial Recogntion Mode Activated'")
    time.sleep(3)

def infowindowshow():
    infowindow.show()
def infowindowhide():
    infowindow.hide()
"""
CheerMe = PushButton(app,#####,text="Cheer Mode", padx = 100, pady = 100,height = "fill", width = "fill")
InfoMe.text_size = 34
InfoMe.bg = "green"
    """
FaceRecButt = PushButton(app,FaceRecogButton,text="Face Recogntion", padx = 100, pady = 100,height = "fill", width = "fill")
FaceRecButt.text_size = 34
FaceRecButt.bg = "yellow"

InfoMe = PushButton(app,infowindowshow,text="Info", padx = 100, pady = 100,height = "fill", width = "fill")
InfoMe.text_size = 34
InfoMe.bg = "green"

InfoMe = PushButton(infowindow,infowindowhide,text="Face Recogntion", padx = 100, pady = 100,height = "fill", width = "fill")
InfoMe.text_size = 34
InfoMe.bg = "green"
app.display()