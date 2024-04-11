import pyttsx3

def talk(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()