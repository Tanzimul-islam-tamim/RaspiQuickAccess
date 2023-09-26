from guizero import App, PushButton, Window, TextBox, Text, Picture
#from gpiozero import LED
#import sys
#import os
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

rulebook = Window(app, title="Rules", height=500, width= 900)
rulebook.hide()

#facerecwindow = Window(app, title="Close",height= 500, width=900)
#facerecwindow.hide()

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
def ruleb():
    rulebook.show()
def rulebclose():
    rulebook.hide()

def langtransshow():
    languagetrans.show()
#    os.system("espeak 'Live Language Translation Mode Activated. Please Speak close to the microphone.'")
    time.sleep(1)

def langtranshide():
    languagetrans.hide()
def Reader():
    #os.system("espeak 'The IOC has the final authority in selecting the host nation. Competitors, team personnel, and officials all must comply with the Olympic Charter and World Anti-Doping Code. Competing nations must be invited by the IOC. Athletes must be allowed to compete without any form of discrimination, with fair and equal gender representation. There is no general age limit for the Olympics, but IFs may establish age restrictions for certain sports with the IOC’s approval. Athletes must not participate in doping or any other manipulation of fair competition.'")
    pass
def translating():
    rules = Text(rulebook, text= "আয়োজক দেশ নির্বাচনের চূড়ান্ত কর্তৃত্ব আইওসি-এর। \n প্রতিযোগী, দলের কর্মী এবং কর্মকর্তাদের অবশ্যই অলিম্পিক চার্টার \n এবং ওয়ার্ল্ড অ্যান্টি-ডোপিং কোড মেনে চলতে হবে। \nপ্রতিযোগী দেশগুলিকে অবশ্যই আইওসি দ্বারা আমন্ত্রণ জানাতে হবে।\n ক্রীড়াবিদদের অবশ্যই ন্যায্য এবং সমান লিঙ্গ প্রতিনিধিত্ব সহ কোন\n প্রকার বৈষম্য ছাড়াই প্রতিযোগিতা করার অনুমতি দিতে হবে।অলিম্পিকের জন্য কোন সাধারণ বয়সের সীমা নেই, \nকিন্তু IFs IOC-এর অনুমোদনের সাথে কিছু খেলার জন্য বয়সের সীমাবদ্ধতা স্থাপন করতে পারে। \n ক্রীড়াবিদদের অবশ্যই ডোপিং বা ন্যায্য প্রতিযোগিতার অন্য কোনো কারসাজিতে অংশগ্রহণ করতে হবে না।", size=11)


### Cv -0


def VideoOn():
    # Get a reference to webcam #0 (the default one)
    #facerecwindow.show()
    #time.sleep(2)
    control = True
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
        "Phelps",
        "Bolt"
    ]

    while control:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        #rgb_frame = frame[:, :, ::-1]
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
                if (name == "Phelps"):
                    print("Good day! Mr. Michael Phelps.You are looking as powerful as ever, sir. Your olympic event is scheduled for today 1400 hours in Saint Denis Aquatic Centre. Please Follow Me, sir.")
                    control = False
                elif (name == "Bolt"):
                    print("Good day! Mr. Ussain Bolt.You are looking very handsome, sir. Your dedicated spot in the olympic village is in Road 5 Block D Apartment 27. Please follow me, sir.")
                    control = False

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'): #and cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) <1: this was for exiting the video by exiting the window
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

####Cv -1

#def loopbreaker():
 #   breaker = 1









##Main Window 4 buttons
FaceRecButt = PushButton(app,VideoOn,text="Face Recogntion",height = "3", width = "17", grid=[1,0])
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


RuleBook = PushButton(app,ruleb,text="Rule Book",height = "3", width = "17", grid=[2,1])
RuleBook.text_size = 34
RuleBook.bg = "cyan"

### The Info Window Codings -0
infoMotivation = Text(infowindow,text="Opportunities don't happen, you create them.",font="Helvetica", size= 30,align= "bottom", color= "blue" )

InfoExit1 = PushButton(infowindow,infowindowhide,text="Exit",height = "2", width = "10", align= "bottom")
InfoExit1.text_size = 34
InfoExit1.bg = "red"
InfoExit1.text_color = "white"
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

RuleRead = PushButton(rulebook,Reader,text="Read",height = "fill", width = 4, align= "right")
RuleRead.text_size = 34
RuleRead.bg = "violet"
InfoEnter = PushButton(rulebook,rulebclose,text="Exit",height = "fill", width = 4, align= "left")
InfoEnter.text_size = 34
InfoEnter.bg = "black"
InfoEnter.text_color = "white"
RuleTrans = PushButton(rulebook,translating,text="Translate",height = 1, width ="fill", align= "bottom")
RuleTrans.text_size = 34
RuleTrans.bg = "brown"

rules = Text(rulebook, text="""The IOC has the final authority in selecting the host nation. \n Competitors, team personnel, and officials all must comply with the Olympic Charter and World Anti-Doping Code. \nCompeting nations must be invited by the IOC. \n Athletes must be allowed to compete without any form of discrimination, with fair and equal gender representation.\n    There is no general age limit for the Olympics, \nbut IFs may establish age restrictions for certain sports with the IOC’s approval. \n Athletes must not participate in doping or any other manipulation of fair competition. """, size=10)


app.display()

