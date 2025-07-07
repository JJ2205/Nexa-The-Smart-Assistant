import pyttsx3


def text_to_speech(text):
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change voice (0 for male, 1 for female)
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()


