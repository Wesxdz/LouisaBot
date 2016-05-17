"""
LouisaBot, written by a lonely young lad.
Required Python modules include: OS, SpeechRecognition, PyAudio, PortAudio, Webbrowser, and NLTK

What does this action signify?
My father tried to teach me human emotions. They are... difficult.
"""

import speech_recognition as sr
import os
import webbrowser
import nltk

# Setup Keywords
browse = ['google', 'search for', 'search', 'look up', 'what is']
name = ['call me', 'my name is']

# Setup Functions


def search(statement):
    for i in browse:
        if i in statement:
            lib = statement[len(i):].replace(' ', '+')
            url = "https://www.google.com/#q="
            webbrowser.open_new(url + str(lib))
            os.system("say Looking up " + statement[len(i):])
            return True

# obtain audio from the microphone
print('Opening Ears...')
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    # r.energy_threshold += 100
    r.pause_threshold = .3
    r.non_speaking_duration = .2
    while True:
        print('Listening...')
        audio = r.listen(source)
        # recognize speech using Google Speech Recognition)
        try:
            said = r.recognize_google(audio)
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("I think you said '" + said + "'")
            words = nltk.word_tokenize(said.lower())
            # nltk.pos_tag(nltk.word_tokenize(said)))
            if 'quit' in words:
                os.system("say 'Fare thee well.'")
                break
            elif 'install' in words:
                mod = input('PIP Module: ')
                os.system("python3.5 -m pip install " + mod)
            elif 'genghis' in words:
                link = 'https://www.youtube.com/watch?v=P_SlAzsXa7E'
                webbrowser.open(link)
            elif search(said):
                print('It worked')
            elif 'mute' in words:
                os.system("osascript -e 'set volume output muted true'")
                r.adjust_for_ambient_noise(source)
            elif 'unmute' in words:
                os.system("osascript -e 'set volume output muted false'")
                r.adjust_for_ambient_noise(source)
            elif 'volume' in words:
                if 'increase' in words:
                    volume = os.system("osascript -e 'output volume of (get volume settings)'")
                    print(volume)
                else:
                    for w in words:
                        if w.isdigit():
                            os.system("osascript -e 'set volume output volume " + w + "'")
                            break
            elif 'hello' in said:
                print("Greetings")
                os.system("say 'Greetings'")
            elif 'thank you' in said:
                os.system("say You are welcome.")
            elif 'simon says ' in said:
                os.system("say " + said[11:])
            elif 'who are you' in said:
                print("I am programmed to be what you say I am.")
                os.system("say 'I am programmed to be what you say I am.'")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
