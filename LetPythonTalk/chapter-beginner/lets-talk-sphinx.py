import speech_recognition as sr
speech = sr.Recognizer()
print('Python is listening--')
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio = speech.listen(source)
    inp = speech.recognize_sphinx(audio)
print('You just said {input}' .format(input=inp))