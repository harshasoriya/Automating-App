import pyttsx3
import speech_recognition as sr

en = pyttsx3.init()
en.setProperty('rate', 190)
voices = en.getProperty('voices')
en.setProperty('voice', voices[1].id)
en.setProperty('volume', 1)


def speak(audio):
    en.say(audio)
    en.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('speak...')
        r.pause_threshold = 0.5
        v = r.listen(source)

    try:
        print('working on your command...')
        text = r.recognize_google(v, language="en-in")
        print("you said:", text)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "none"

    return text
