#MODULES

import speech_recognition as sr
from GoogleNews import GoogleNews
import pyttsx3

#initialization

googlenews = GoogleNews()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
recognizer = sr.Recognizer()

#COMMA

def cmd():
    with sr.Microphone() as Source:
        print('Clearing the background noices...')
        recognizer.adjust_for_ambient_noice(Source , duration = 0.5)
        print('Ask me anything...')
        recordaudio = recognizer.listen(Source , timeout = 1)
        print('Done recording.')
    try:
        text = recognizer.recognize_google(recordaudio , language = 'en-US')
        text = text.lower()
        print('Your message :' , format(text))

    except Exception as ex:
        print(ex)

    if 'headlines' in text:
        engine.say('Getting news for you')
        engine.runAndWait()
        googlenews.get_news('Today news')
        a = googlenews.gettext()
        print(*a[1:5] , sep = ',')

    if 'tech' in text:
        engine.say('Getting news for you')
        engine.runAndWait()
        googlenews.get_news('tech')
        a = googlenews.gettext()
        print(*a[1:5] , sep = ',')

    if 'politics' in text:
        engine.say('Getting news for you')
        engine.runAndWait()
        googlenews.get_news('politics')
        a = googlenews.gettext()
        print(*a[1:5] , sep = ',')

    if 'sports' in text:
        engine.say('Getting news for you')
        engine.runAndWait()
        googlenews.get_news('sports')
        a = googlenews.gettext()
        print(*a[1:5] , sep = ',')

    if 'cricket' in text:
        engine.say('Getting news for you')
        engine.runAndWait()
        googlenews.get_news('cricket')
        a = googlenews.gettext()
        print(*a[1:5] , sep = ',')
