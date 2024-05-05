import speech_recognition as sr
import keyboard
import threading
import pyttsx3
import subprocess
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
                    audio = recognizer.listen(source, timeout=0.2, phrase_time_limit=3) #
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
    if "play" in ftext and "game" not in ftext:
        from pywhatkit import playonyt
        song = ftext.replace("play","")
        try:
            playonyt(song)
            talk("Playing")
            talk(song)
        except ValueError:
            talk("Sorry but an error occured while trying to play "+ song + ". If possible can you be specific?")
    
    elif "search" in ftext:
        import pywhatkit
        search = ftext.replace("search","")
        pywhatkit.search(search)
        talk("Searching")
        talk(search)
    
    elif "screenshot" in ftext:
        from pyautogui import press
        press("printscreen")
        talk("Done sir")
    
    elif "whether" in ftext or "weather" in ftext:
        from weather import weather_report as wtr
        sent = wtr()
        talk(sent)            

    elif "open" in ftext:
        from application import open_app
        app = open_app(ftext)
        talk(app)
        
    elif "close" in ftext:
        from application import close_app
        app = close_app(ftext)
        talk(app)        
    
    elif "who is" in ftext:
        from wikipedia import summary
        person = ftext.replace("who is","")
        info = summary(person,1)
        talk(info)

    elif "game" in ftext:
        from game import find_game_link 
        sent = find_game_link(ftext)
        talk(sent)

    elif "download" in ftext:
        from yt import yt_download
        sent = yt_download()
        talk(sent)
        
    elif "add" in ftext:
        from whatsapp import add_number,save_data
        talk("please enter the number in the below popup with the name.")
        add_number()
    elif "pause" in ftext:
        from pyautogui import press
        press("k")
        
    elif "continue" in ftext:
        from pyautogui import press
        press("k")
        
    elif "forward" in ftext:
        from pyautogui import press
        press("l")

    elif "backward" in ftext:
        from pyautogui import press
        press("j")


    elif "send" in ftext:
        import whatsapp2
        try:
            contacts = whatsapp2.load_contacts("data.json")
            whatsapp2.create_contact_list_gui(contacts)
        except FileNotFoundError:
            talk("Sorry! No number found in the contact list.")
            
    else:
        print("I dont get you sir!")
        talk("I dont get you sir!")
        
if __name__ == "__main__":
    recognition_active = False
    keyboard.hook(on_key_event) 
    thread = threading.Thread(target=mic_to_text)
    thread.start()
    subprocess.Popen(["python", "p.py"])

    keyboard.wait('esc')
    recognition_active = False
    thread.join()