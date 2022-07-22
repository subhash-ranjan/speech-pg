import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voiceProperties = engine.getProperty('voices')
engine.setProperty('voice', voiceProperties[1].id)
engine.say('I am alexa. what i can do for you')
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language='en-US')
        print(command)
        command = command.lower()
        if 'alexa' in command.lower():
            print(command)
        else:
            print('alexa not in command')

except Exception as e:
    print(e)
    pass
