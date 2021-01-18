# Importing the modules
import pyttsx3                                                        # pip install pyttsx3
import speech_recognition as sr                                       # pip install speechRecognition
import datetime
import wikipedia                                                      # pip install wikipedia
import webbrowser
import os

# Creating the speech API
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# Creating the function for speaking
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# creating a function for wishing
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    elif hour>=18 and hour<20:
        speak("Good Evening sir!")  

    else:
        speak("Good Night sir!")  

    speak("I am Jarvis. Please tell me how may I help you") 

# Taking voice input from Microphone
def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("please speak ..")
        audio_data = r.record(source, duration = 7)
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio_data, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# Creating a Loop
if __name__ == "__main__":
    wishMe()
    while True:
    
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
            webbrowser.open("youtube.com")

        elif 'open Facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open Linkedin' in query:
            webbrowser.open("www.linkedin.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open Whatsapp' in query:
            webbrowser.open("www.web.whatsapp.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\shrim\\Videos'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            

        elif 'open code' in query:
            codePath = "C:\\Users\\shrim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome"
            os.startfile(codePath)
         
        
        elif 'Hello' in query:
            speak('hii')


        



