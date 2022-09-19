import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()  # Speech recognition object
engine = pyttsx3.init()     # TTS engine object

voices = engine.getProperty('voices')   # Set voice to female
engine.setProperty('voice', voices[1].id)


# Text to speech command
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                return command
    except:
        return ''


def run_alexa():
    command = take_command()
    print(command)
    if 'say hi to' in command:
        name = command.replace('say hi to', '')
        talk('Hi,' + name + 'nice to meet you')
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)    # Play song on yt
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)     # Get one
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


if __name__ == '__main__':
    while True:
        run_alexa()
