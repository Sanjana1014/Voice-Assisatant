import pyttsx3
import speech_recognition as sr
import datetime
from cv2 import cv2
import random
import wikipedia
import pychrome
import webbrowser
import os
import smtplib
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to wish according to time
def wishMe():
    
    hour = datetime.datetime.now().hour
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    if hour>=0 and hour<12:
        speak(f"Good Morning Master, it's {strTime}")
        print("Good Morning Master, it's")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Master, it's {strTime}")
        print("Good Afternoon Master, it's")
    else:
        speak(f"Good Evening Master, it's {strTime}")
        print("Good Evening Master, it's")
    print(strTime)

    speak("I am Jarvis Master, Please tell me how may I help you")
    print("I am Jarvis Master, Please tell me how may I help you")

#It takes Microphone input from the user and returns string output

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I am Listening Master")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=4)

    try:
        print("Recognizing...")
        speak("I am Recognizing your voice Master")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

#to send email

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rinkichaurasia1003@gmail.com', 'Sanjana@10')
    server.sendmail('rinkichaurasia1003@gmail.com', to, content)
    server.close()

#for executing different and enlisted tasks

def TaskExecution():  # sourcery skip: low-code-quality
    wishMe()
    while True:
        query = takeCommand().lower()

    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open pdf reader' in query:
            pdfpath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(pdfpath)

        elif 'open notepad' in query:
            npath = "C:\\Users\\91901\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.exe"
            os.startfile(npath)

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cap = cv2.imshow('webcam', img)
                k = cv2.waitKey(58)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'open cmd' in query:
            os.system("start cmd")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Sir, what should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'email to ashish' in query:
            try:
                speak("What should I say to him ?")
                content = takeCommand()
                to = "ashishgill12121999@gmail.com "
                sendEmail(to, content)
                speak("Email has been sent to Ashish!")
            except Exception as e:
                print(e)
                speak("Sorry Master your email is not sent to Ashish due to some issues.")

        elif 'email to shubham' in query:
            try:
                speak("What should I say to him ?")
                content = takeCommand()
                to = "shubhamtripathi655@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to Shubham!")
            except Exception as e:
                print(e)
                speak("Sorry Master your email is not sent to Shubham due to some issues.")

        elif 'email to sarthak' in query:
            try:
                speak("What should I say to him ?")
                content = takeCommand()
                to = "sharthak9@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to Sarthak!")
            except Exception as e:
                print(e)
                speak("Sorry Master your email is not sent to Sarthak due to some issues.")

        elif 'play music' in query:
            music_dir = 'F:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Master, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\91901\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open ipu' in query:
            webbrowser.open("ipu.ac.in")

        elif 'open web whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'no thanks' in query:
            speak("Thanks for using me Master, Have a good day")
            sys.exit()

        elif 'close notepad' in query:
            speak("Okay sir, Closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'close pdf reader' in query:
            speak("Okay sir, Closing PDF Reader")
            os.system("taskkill /f /im AcroRd32.exe")

        elif 'set alarm' in query:
            nn = datetime.datetime.now().hour
            if nn==8:
                music_dir = 'F:\\Songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")

        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'hello' in query or 'hey' in query:
            speak("Hello Master, may i help you with something.")

        elif 'how are you' in query:
            speak("I am fine Master, What about you.")

        elif 'also good' in query or 'fine' in query:
            speak("That's great to hear from you.")

        elif 'thank you' in query or 'thanks' in query:
            speak("It's my pleasure Master.")

        elif 'you can sleep' in query or 'sleep now' in query:
            speak("Okay Master, I am going to sleep now you can call me anytime.")
            break


if __name__ == '__main__':
    while True:
        permission = takeCommand()
        if 'wake up' in permission:
            TaskExecution()
        elif 'goodbye' in permission:
            speak("Thanks for using me Master, Have a good day")
            sys.exit()