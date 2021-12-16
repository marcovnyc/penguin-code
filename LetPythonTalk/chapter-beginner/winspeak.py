import pyttsx3

def speak(text):
    engine = pyttsx3.init("espeak")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[3].id)
    engine.say(text)
    engine.runAndWait()

text = 'My name is Homer Simpson'
speak(text)