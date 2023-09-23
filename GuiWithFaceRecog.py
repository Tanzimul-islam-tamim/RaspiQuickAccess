from guizero import App, PushButton, Window, TextBox, Text, Picture
#from gpiozero import LED
#import sys
import os
import time
import face_recognition
import cv2
import numpy as np
import pyttsx3
breaker = 0
app = App('COUBERTIN', height = 500, width = 900, layout="grid")
infowindow = Window(app, title = "Input Name",height = 500, width = 900)
infowindow.hide()
infogif = Window(infowindow, title="Destination", height=500, width= 900)
infogif.hide()

languagetrans = Window(app, title = "Language Translation", height=500, width= 900)
languagetrans.hide()

#facerecwindow = Window(app, title="Close",height= 500, width=900)
#facerecwindow.hide()

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


### Cv -0
def VideoOn():
    # Get a reference to webcam #0 (the default one)
    #facerecwindow.show()
    #time.sleep(2)
    video_capture = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("1.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # Load a second sample picture and learn how to recognize it.
    biden_image = face_recognition.load_image_file("afridi.jpg")
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        obama_face_encoding,
        biden_face_encoding
    ]
    known_face_names = [
        "VP Sir",
        "Mr.Afridi"
    ]

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        # rgb_frame = frame[:, :, ::-1]
        rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])

        # Find all the faces and face enqcodings in the frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                print("The afibaefuhbseuf")
                engine = pyttsx3.init()
                engine.say('Hello sir, how may I help you, sir.')
                engine.runAndWait()

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

####Cv -1

#def loopbreaker():
 #   breaker = 1









##Main Window 4 buttons
FaceRecButt = PushButton(app,VideoOn,text="Face Recogntion",height = 3, width = 17, grid=[1,0])
FaceRecButt.text_size = 34
FaceRecButt.bg = "magenta"

InfoMe = PushButton(app,infowindowshow,text="Info",height = 3, width = 17, grid=[1,1])
InfoMe.text_size = 34
InfoMe.bg = "green"

LanguageTrans = PushButton(app,langtransshow,text="Language Translation",height = 3, width = 17, grid=[2,0])
LanguageTrans.text_size = 34
LanguageTrans.bg = "orange"


CheerMe = PushButton(app,langtransshow,text="Cheer Mode",height = 3, width = 17, grid=[2,1])
CheerMe.text_size = 34
CheerMe.bg = "cyan"

### The Info Window Codings -0
infoMotivation = Text(infowindow,text="Opportunities don't happen, you create them.",font="Helvetica", size= 30,align= "bottom", color= "blue" )

InfoExit = PushButton(infowindow,infowindowhide,text="Exit",height = 2, width = 10, align= "bottom")
InfoExit.text_size = 34
InfoExit.bg = "red"

InfoEnter = PushButton(infowindow,infoenter,text="Enter",height = 2, width = 10, align= "bottom")
InfoEnter.text_size = 34
InfoEnter.bg = "green"

InfoText = TextBox(infowindow,text="Please Enter your Athlete ID: 2958 ",width= 100, align= "top")

InfoExit = PushButton(infogif,infoenterhide,text="Thank You",height = 2, width = 10, align= "bottom") #Info 3rd Window
InfoExit.text_size = 34
InfoExit.bg = "red"
InfoMapGif = Picture(infogif, image= "maps.gif")
### The Info WIndow Codings -1


##face rec button
#facerecbutton = PushButton(facerecwindow, loopbreaker, text="Close", height="2", width="10", align= "bottom")


app.display()

