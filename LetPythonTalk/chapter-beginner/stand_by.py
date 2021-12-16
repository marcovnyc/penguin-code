import speech_recognition as sr
speech = sr.Recognizer()
while True:
    print('Python is listening--')
    inp = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            inp = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    print('You just said {input}' .format(input=inp))
    if inp == "stop listening":
        print('Good bye')
        break