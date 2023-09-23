from guizero import App, PushButton, Window, TextBox, Text, Picture
#from gpiozero import LED
#import sys
import os
import time


app = App('COUBERTIN', height = 500, width = 900, layout="grid")
infowindow = Window(app, title = "Input Name",height = 500, width = 900)
infowindow.hide()
infogif = Window(infowindow, title="Destination", height=500, width= 900)
infogif.hide()

languagetrans = Window(app, title = "Language Translation", height=500, width= 900)
languagetrans.hide()
def FaceRecogButton():
#    os.system("espeak 'Facial Recogntion Mode Activated'")
    time.sleep(3)


##Info Window-0
def infowindowshow():
    infowindow.show()
def infowindowhide():
    infowindow.hide()

def infoenter():
    infogif.show()
def infoenterhide():
    infogif.hide()
 ##Info Window-1


def langtransshow():
    languagetrans.show()
#    os.system("espeak 'Live Language Translation Mode Activated'")
    time.sleep(3)

def langtranshide():
    languagetrans.hide()


##Main Window 4 buttons
FaceRecButt = PushButton(app,FaceRecogButton,text="Face Recogntion",height = "3", width = "17", grid=[1,0])
FaceRecButt.text_size = 34
FaceRecButt.bg = "magenta"


HelpMe = PushButton(app,infowindowshow,text="Help",height = "3", width = "17", grid=[1,1])
HelpMe.text_size = 34
HelpMe.bg = "green"
"""
InfoMe = PushButton(app,infowindowshow,text="Info",height = "3", width = "17", grid=[1,1])
InfoMe.text_size = 34
InfoMe.bg = "green"
"""
LanguageTrans = PushButton(app,langtransshow,text="Language Translation",height = "3", width = "17", grid=[2,0])
LanguageTrans.text_size = 34
LanguageTrans.bg = "orange"


CheerMe = PushButton(app,langtransshow,text="Cheer Mode",height = "3", width = "17", grid=[2,1])
CheerMe.text_size = 34
CheerMe.bg = "cyan"

### The Info Window Codings -0
infoMotivation = Text(infowindow,text="Opportunities don't happen, you create them.",font="Helvetica", size= 30,align= "bottom", color= "blue" )

InfoExit = PushButton(infowindow,infowindowhide,text="Exit",height = "2", width = "10", align= "bottom")
InfoExit.text_size = 34
InfoExit.bg = "red"

InfoEnter = PushButton(infowindow,infoenter,text="Enter",height = "2", width = "10", align= "bottom")
InfoEnter.text_size = 34
InfoEnter.bg = "green"

InfoText = TextBox(infowindow,text="Please Enter your Athlete ID: 2958 ",width= 100, align= "top")
##0-9 Buttons -0
## Buttons -1
InfoExit = PushButton(infogif,infoenterhide,text="Thank You",height = "2", width = "10", align= "bottom") #Info 3rd Window
InfoExit.text_size = 34
InfoExit.bg = "red"
InfoMapGif = Picture(infogif, image= "maps.gif")
### The Info WIndow Codings -1



app.display()

