import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good After Noon!")
    
    else:
        speak("Good Evening!")

    speak("Hai I am Jarvis. Sir. Please tell me How may I help you. sir")



def takeCommand():
    # It take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('raghavagrawal987078@gmail.com','9870785925')
    server.sendmail('raghavagrawal987078@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

         # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play' in query:
            song = query.replace("play", "")
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
       
        elif 'stop song' in query or 'close song' in query:
            os.system("taskkill /im chrome.exe /f")  # Agar tum Chrome use karte ho
            os.system("taskkill /im msedge.exe /f")  # Agar tum Edge use karte ho
            speak("Song has been stopped sir.")

        elif 'chat gpt' in query:
            speak("Opening Chat GPT")
            webbrowser.open("https://chat.openai.com")
        
        elif 'search' in query:
            search_query = query.replace("search", "").strip()
            speak(f"Searching {search_query} on Google")
            pywhatkit.search(search_query)


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("strTime")
            speak(f"sir. The time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\HP\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'open word' in query:
            Word = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(Word)
        
        elif 'email to Raghav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "raghavagrawal987078@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e: 
                print(e)
                speak("sorry my friend Raghav bhai. I am not able to send this email")