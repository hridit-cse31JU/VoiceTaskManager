import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio input and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Speech Recognition
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command
        except Exception as e:
            print(f"Error: {e}")
            return None
