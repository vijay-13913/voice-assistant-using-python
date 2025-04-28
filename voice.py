import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from playsound import playsound
import os

# Voice engine setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Contact list 
contacts = {
    "laddu": "919701749495",
    "santhosh": "919177452709"
}

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
            return query.lower()
        except:
            speak("Sorry, I didn't catch that.")
            return ""

def play_music():
    music_path = "G:\\Music\\fav_song.mp3"  
    if os.path.exists(music_path):
        speak("Playing music.")
        playsound(music_path)
    else:
        speak("Music file not found.")

def open_website(name):
    urls = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "spotify": "https://open.spotify.com",
        "amazon": "https://www.amazon.in",
        "flipkart": "https://www.flipkart.com",
        "rapido": "https://www.rapido.bike",
        "whatsapp": "https://web.whatsapp.com",
        "facebook": "https://www.facebook.com"
    }
    if name in urls:
        speak(f"Opening {name}")
        webbrowser.open(urls[name])
    else:
        speak("Website not recognized.")

def call_friend(name):
    if name in contacts:
        phone_number = contacts[name]
        url = f"https://wa.me/{phone_number}"
        speak(f"Calling {name} on WhatsApp.")
        webbrowser.open(url)
    else:
        speak(f"Sorry, I don't have contact info for {name}.")

def run_assistant():
    speak("How can I help you?")
    query = take_command()

    if 'play music' in query:
        play_music()

    elif 'open' in query:
        sites = ["google", "youtube", "spotify", "amazon", "flipkart", "rapido", "whatsapp", "facebook"]
        for site in sites:
            if site in query:
                open_website(site)
                break
        else:
            speak("I didn't understand which site to open.")

    elif 'call' in query:
        for name in contacts.keys():
            if name in query:
                call_friend(name)
                break
        else:
            speak("I didn’t catch who you want to call.")

    else:
        speak("Sorry, I can't help with that yet.")

    speak("Shutting down. Have a great day!")

# Start the assistant
if __name__ == "__main__":
    run_assistant()





