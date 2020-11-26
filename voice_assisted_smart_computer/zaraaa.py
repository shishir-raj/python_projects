import pyttsx3
import pythoncom
import speech_recognition as sr
import datetime

engine = pyttsx3.init("sapi5")
voice = engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice', voice[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def takecmd():
    obj =sr.Recognizer() #obj is the working person.
    with sr.Microphone() as source:
        print('Listening ')
        speak('Hi, i am zara, Please speak ')
        obj.pause_threshold=1 #india english pause speed is assumed 1
        audio = obj.listen(source)
        print(audio)
    try:

        print("recognizing")
        speak("recognizing")
        understood_audio = obj.recognize_google(audio,language="en-in")
        print(f"you said {understood_audio} ")
        speak(f"you said {understood_audio} ")
    except Exception as e:
        print("Please say that again ")
        speak("please say that again, Improve your english")
        return "None"
    return understood_audio
import webbrowser
import wikipedia
import os
from random import *

music_keywords=["play some music","play music","play songs","play song", "play some songs"]
while(1):
    query= takecmd().lower()
    if "time" in query:
        timenow=datetime.datetime.now().strftime("%H:%M:%S")
        speak(timenow)
        print(timenow)
    elif "wikipedia" in query:
        query= query.replace("on wikipedia","")
        result= wikipedia.summary(query,sentences=3)
        print(result)
        speak(result)
    elif "bye" in query:
        exit()
    elif "open google" in query:
        webbrowser.open("google.com")
    elif "youtube" in query:
        webbrowser.open("youtube.com")

    elif "open microsoft word" in query:
        codepath=  r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
        os.startfile(codepath)
    elif "play some music" in query:
        codepath= r"C:\Users\shish\Desktop\songs"
        songs1 = os.listdir(codepath)  #gets all files in that directory
        print(songs1)
        os.startfile(os.path.join(codepath , songs1[randint(0,len(songs1)-1)]))









#speak(" ")
# var1 = datetime.datetime.now().strftime("%H:%M:%S")
# print(var1)
# speak(var1)
#
# var2= datetime.datetime.now().hour
# speak(var2)






