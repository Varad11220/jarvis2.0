import speech_recognition as sr
import keyboard
import threading
import pyttsx3
def on_key_event(e):
    global recognition_active
    if e.event_type == keyboard.KEY_DOWN and e.name == 'h':
        recognition_active = True
    elif e.event_type == keyboard.KEY_UP and e.name == 'h':
        print("Speech recognition deactivated.")
        recognition_active = False
        

def talk(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()

def mic_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            if recognition_active:
                try:
                    print("Listening")
                    audio = recognizer.listen(source, timeout=0.2, phrase_time_limit=5) #
                    print("Transcribing")
                    text = recognizer.recognize_google(audio)
                    ftext = format(text)
                    if_else(ftext)
                except sr.UnknownValueError:
                    pass  # Ignore errors for unknown values
                except sr.RequestError as e:
                    print("Error with the speech recognition service; {0}".format(e))
                except sr.WaitTimeoutError:
                    pass
                

def if_else(ftext):
    if "play" in ftext:
        from pywhatkit import playonyt
        song = ftext.replace("play","")
        try:
            talk("Playing")
            talk(song)
            playonyt(song)
        except ValueError:
            talk("Sorry but an error occured while trying to play "+ song + ". If possible can you be specific?")
    
    elif "search" in ftext:
        from pywhatkit import search
        search = ftext.replace("search","")
        talk("Searching")
        talk(search)
        search(search)
    
    elif "screenshot" in ftext:
        from pyautogui import press
        press("printscreen")
        talk("Done sir")
    
    elif "whether" or "weather" in ftext:
        from weather import weather_report as wtr
        sent = wtr()
        talk(sent)            

if __name__ == "__main__":
    recognition_active = False
    keyboard.hook(on_key_event) 
    thread = threading.Thread(target=mic_to_text)
    thread.start()
    keyboard.wait('esc')
    recognition_active = False
    thread.join()
   
    