from vosk import Model, KaldiRecognizer
import pyaudio



model = Model(r"C:\Robotics\0PyCharm\vosk-model-small-en-in-0.4 india\vosk-model-small-en-in-0.4") #the language model is to be kept here

recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16,channels=1,rate=16000, input=True,frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text)
