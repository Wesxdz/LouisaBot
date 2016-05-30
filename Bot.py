"""
LouisaBot, written by a lonely young lad.
Written in Python 3.5
Required Python modules include: OS, SpeechRecognition, PyAudio, PortAudio, Webbrowser, and NLTK

What does this action signify?
My father tried to teach me human emotions. They are... difficult.
"""

import speech_recognition as sr
import os
import webbrowser
import nltk
from pws import Bing
import pafy
import subprocess

# Setup Functions


def parse(something):
    global key
    return something[len(key):]


def say(something):
    os.system('say -v "Victoria" ' + something)


def install():
    module = input('PIP Module: ')
    os.system("python3.5 -m pip install " + module)


def find():
    global statement, key
    mysearch = statement[len(key):]
    query = Bing.search(query=mysearch, num=2)
    results = (query.get('results')[0])
    mylink = results.get('link')
    webbrowser.open(mylink)
    Self.this = mylink


def download():
    if Self.this != '':
        url = input('Enter URL ')
    else:
        url = Self.this
    video = pafy.new(url)
    best = video.getbest(preftype='mp4')
    # bestaudio = video.getbestaudio(preftype='m4a')
    filetype = '.mp4'
    filepath = "/Users/Wesxdz/PycharmProjects/LouisaBot/Media/"
    best.download(filepath=filepath)
    subprocess.call(['open', filepath + video.title + filetype])


def play():
    songs = os.listdir('Media')
    print(songs)
    for s in songs:
        for i in words:
            if i in s.lower():
                print(i + s)
                subprocess.call(['open', "/Users/Wesxdz/PycharmProjects/LouisaBot/Media/" + s])
                break


def search():
    global statement, key
    lib = statement[len(key):].replace(' ', '+')
    url = "https://www.google.com/#q="
    webbrowser.open_new(url + str(lib))
    say("Looking up " + statement[len(key):])


def end():
    global power
    power = False
    say('Goodbye')

# Setup Keywords
power = True
statement = ''
functions = {search: ['google', 'search for', 'search', 'look up', 'what is'], end: ['quit', 'stop', 'end'],
             find: ['find'], install: ['install'], download: ['download this']}


class Self:
    name = 'LouisaBot'
    this = ''

print(Self.name)
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    r.pause_threshold = .3
    r.non_speaking_duration = .2

    while power:
        audio = r.listen(source)
        # recognize speech using Google Speech Recognition)
        try:
            statement = r.recognize_google(audio).lower()
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print(statement)
            words = nltk.word_tokenize(statement.lower())
            # nltk.pos_tag(nltk.word_tokenize(statement)))
            for keywords in functions:
                for k in functions[keywords]:
                    if k in statement:
                        key = k
                        keywords()
                        break

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
