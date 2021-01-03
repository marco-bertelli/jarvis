import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

#listener in ascolto sulle nostre parole

listener = sr.Recognizer()
#inizializzo il motore, cioè quello che "capisce"
engine = pyttsx3.init()

def ia_talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        #quando cattura dei suoni in entrata li elabora con la libreria
        with sr.Microphone() as source:
            print("sto ascoltando...")
            voice = listener.listen(source)
            #interpreta il comando con una libreria google
            command = listener.recognize_google(voice)
            #per sicurezza metto tutto in minuscolo
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        print("non ho capito ")

    return command

#funzione principale, prende un comando vocale lo traduce e cerca di associarlo ad una funzione
def jarvis_run():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        ia_talk("ok avvio "+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        ia_talk('sono le'+time)
    elif 'who is' in command:
        person = command.replace('who is ', '')
        info=wikipedia.summary(person, 1)
        ia_talk(info)
    #funzioni divertenti
    elif 'bottana' in command:
        print("stai dicendo a tua madre per caso")
        ia_talk("stai dicendo a tua madre per caso")
    elif 'joke' in command:
        ia_talk(pyjokes.get_joke('it', 'neutral'))
    else:
        ia_talk("scusa non ho capito il comando")

while True:
    jarvis_run()