import speech_recognition as sr
import pyttsx3
import webbrowser
import sys
import pyaudio

def talk(words):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 155)
    engine.say(words)
    engine.runAndWait()
talk("Hi, how can I help you?")


def command():
    object = sr.Recognizer()

    with sr.Microphone() as source:
        print("speak")
        object.adjust_for_ambient_noise(source, duration=1)
        audio = object.listen(source)

    try:
        task = object.recognize_google(audio).lower()
        print("You have just said: " + task)

    except sr.UnknownValueError:
        talk("I do not understand you")
        task = command()

    return task

def makesomething(task):
    if "open facebook" in task:
        talk("give me a second")
        url = "https://www.facebook.com/"
        webbrowser.open(url)
    elif "your name" in task:
        talk("My name is Assistance")
    elif "stop" in task:
        talk("Have a nice day")
        sys.exit()

while True:
    makesomething(command())