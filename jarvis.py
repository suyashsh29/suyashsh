import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r =sr.Recognizer()
    with sr.Microphone(device_index=None, sample_rate=None, chunk_size=1024) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source,Timeout)
    try:
        print("Recognizing...")
        query = r.recognize_google_cloud()
        print("recognize_google")
        print(f"user said:{query}\n")
    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query
    
if _name_ == "_main_":
    while True:
        query=takeCommand().lower()
        if 'xyz' in query:
            print("yes sir")
            speak("yes sir")