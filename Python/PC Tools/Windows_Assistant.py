"""
How to use this tool ?

1. Install all requirementes and run program.
2. When Listening... program, you can say bellow querys.
    a) According to wikipedia ...
    b) open youtube
    c) open google
    d) open facebook
    e) open stackoverflow
    f) play music
    g) the time now
    h) email to ...

"""


import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            # webbrowser.open("youtube.com")
            path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open("youtube.com")
            speak("Please Wait...")
            speak("Opening Youtube ...")
            break

        elif 'open google' in query:
            # webbrowser.open("google.com")
            path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open("google.com")
            speak("Please Wait...")
            speak("Opening Google ...")
            break

        elif 'open facebook' in query:
            # webbrowser.open("facebook.com")
            path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open("facbook.com")
            speak("Please Wait...")
            speak("Opening Facebook ...")
            break

        elif 'open stackoverflow' in query:
            # webbrowser.open("stackoverflow.com")
            path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open("stackoverflow.com")
            speak("Please Wait...")
            speak("Opening stackoverflow ...")
            break


        elif 'play music' in query:
            music_dir = 'D:\\OLD SONGH'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[50]))
            speak("Please Wait...")
            speak("Playing Song ...")
            break

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            break

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                print(content)
                to = input('Enter Email id - ')
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")
            break