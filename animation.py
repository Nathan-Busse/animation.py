
import numpy as np
#import gtts
#import face_recognition as fr
#import opencv-python
import pyttsx3
import pyttsx3
import playsound
import sys
import time
import datetime
import Speak
import wikipedia
import speech_recognition
import speech_recognition as sr
import pyaudio
import numpy
import smtplib
import random
import os
import wolframalpha
import webbrowser
import subprocess
import psutil
import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file

import random
from time import ctime  # get time details
import webbrowser  # open browser
import ssl
import certifi
import time
import os  # to remove created audio files
from PIL import Image
import subprocess
#from gtts import gTTS
import pyttsx3
import bs4 as bs
import urllib.request
import requests
from playsound import playsound
import speedtest
from subprocess import call
import os
import logging
#import imutils
#from imutils.video import VideoStream
#from imutils.video import FPS
import numpy as np
import time
from pygame import mixer
#import cv2
from gtts import gTTS
import string


# import serial

# in connect.py
# ser = serial.Serial('/dev/ttyACM0',9600)


#engine = pyttsx3.init('espeak')
#engine.setProperty('rate', 140)

client = wolframalpha.Client('Your_App_ID')

#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(audio):
    print('A.I: ' + audio)


    
    
   # engine.runAndWait()
    
    finalChar = 201
    print(audio)
    
    text_to_speech = gTTS(text=audio, lang='en')
    
    text_to_speech.save('audio.mp3')
    mixer.init()
    mixer.music.load("audio.mp3")
    mixer.music.play()    


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


greetMe()

speak('Hello, ')
speak('hello')
speak('hello i dont think we have met. ,  i  am extremely excited to get to know each other and form a new relationship. let me tell you more about myself. I was designed by Nathan and was first tested  in 28 October 2020. I am still being currently developed and still learning new things. So be patient if i do not know the answer to your question for i might know it in the future. i was designed to be customized and therefore i have no name. can you give me my own name. ')
if __name__ == '__main__':

    myname = input('please type my name:')
                   
    
    speak(myname + 'is my name. what is your name.')

    name = input('please type your name:')

    speak(name + "!")
    speak(name + '.. it is so nice to meet you')








def myCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
       
        print("Listening...")
        # playsound('hey.mp3')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except Exception as e:
        print(e)
        print("Say that again")
        return "None"

    return query


if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        # if m == ('on'):
        # val= '1'
        # ser.write(val.encode("utf-8"))
        # break

        # elif m == ('off'):
        # val='0'
        # print(val.encode("utf-8"))
        # ser.write(val.encode("utf-8"))

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')


       

                
        elif 'made mistake with your name' in query:
            myname =myCommand()
            speak(myname + '...is now my new name.')


        elif query == 'none':
            continue

        elif 'what is my name' in query:
            speak(name )

        elif 'what is the time' in query or "tell me the time" in query or "what time is it" in query or "what is the time" in query:
            time = ctime().split(" ")[3].split(":")[0:2]
            if time[0] == "00":
                hours = '12'
            else:
                hours = time[0]
            minutes = time[1]
            seconds = time[1]
            date = time[1]
            time = hours + " hours and " + minutes + "minutes and" + seconds + "seconds"
            speak(time)

        elif 'time for a game' in query:

            os.system('home/pi/PycharmProjects/SETH/Game.py')


        elif 'open ccleaner' in query:

            speak('okay')
            subprocess.call(r'C:\Program Files\CCleaner\CCleaner.exe')

        elif 'open google chrome' in query:

            speak('okay')
            subprocess.call(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif 'open powerpoint' in query:

            speak('okay')
            subprocess.call(r'C:\Program Files\Microsoft Office\Office16\WORD.EXE')

        elif 'open youtube' in query:

            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:

            speak('okay')
            webbrowser.open('www.google.co.in')


        elif 'open gmail' in query:

            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'what are you' in query:
            
                stMsgs =       [' I was designed by Nathan and was first tested  in 28 October 2020. I am still being currently developed and still learning new things. So be patient if i do not know the answer to your question for i might know it in the future. ']
                speak(random.choice(stMsgs))

        elif "how are you feeling today" in query or 'How are you doing' in query:
            stMsgs = ['I am good']

            speak(random.choice(stMsgs))


        elif "slice the watermelon" in query:
            stMsgs = ['You. Yes you. Leave my watermelon alone']

            speak(random.choice(stMsgs))






        elif 'good morning' in query:

            speak('morning. how are you doing')

        elif 'good afternoon' in query:

            speak('afternoon. how are you doing')


        elif 'good evening' in query:

            speak('evening. how are you doing')


        elif 'doing well' in query:

            speak('I am glad to here.')


        elif 'not good' in query:

            speak('that is sad to here. ')




        elif 'execute order 66' in query:

            speak('yes my lord. ')


        elif 'thank you' in query:

            speak('Pleasure. I am glad that I can help.')

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry ! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye , have a good day.')


        elif 'hi' in query or 'hello' in query:
            speak('Hello  ')



        elif 'what is your name' in query:
            speak(myname)




        elif 'what is my battery' in query:

            battery = psutil.sensors_battery
            print(battery.percent)  # ------------Bug

        elif 'accepted' in query:
            stMsgs = ['Thank you.', 'you made my day', 'i feel much better.']
            speak(random.choice(stMsgs))

        elif 'time for bed' in query:
            stMsgs = ['Good night.', 'Sleep tite.', ' Don\'t let the bed bugs bite.', ' See you in the morning.', ''
                                                                                                                  ''
                                                                                                                  'Do not go gentle into that good night. old age should burn and rave at close of day. rage. rage against the dying of the light. though wise men at their end know dark is right, because their words had forked no lightning they do not  go gentle into that good night. rage. rage against the dying of the light.',
                      'Our Father, who art in heaven. hallowed be thy name. thy kingdom come, thy will be done, on earth as it is in heaven. give us this day our daily bread. and forgive us our trespasses, as we forgive those who trespass against us. and lead us not into temptation, but deliver us from evil. for thine is the kingdom, and the power, and the glory. for ever and ever. amen']

            speak(random.choice(stMsgs))



        elif 'Amen' in query:
            speak('Amen.')
            sys.exit()

        elif '  ' in query:
            speak('No')

        elif 'what are you' in query:
            stMsgs = ['I am  Seth.'
                      ' I was designed by Nathan and was first tested  in 28 October 2020. I am still being currently developed and still learning new things. So be patient if i do not know the answer to your question for i might know it in the future. ']

            speak(random.choice(stMsgs))

        elif 'hello' in query:

            speak(
                'Hello my name is Seth and i can do the following . i can play music. browse the web. Have conversations.  Open apps and other software installed on your device. I can send emails. I can open Youtube. I can do so much more')


       




        elif 'bye' in query:
            speak(name +'see you later and , have a good day.')
           



        elif 'music' in query:
            music_folder = 'Party\\'
            music = ['Arrow']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)







        elif 'time for a movie' in query:
            movie_folder = 'Movies\\'
            movie = ['Pacific.Rim.Uprising.2018.720p.WEBRip.x264-[YTS.AM]',
                     'Terminator.Dark.Fate.2019.1080p.WEBRip.x264-[YTS.LT]']
            random_movie = movie_folder + random.choice(movie) + '.mp4'
            os.system(random_movie)

            speak('Okay, here is your movie! Enjoy!')
            speak('Quite. we are watching a movie.')




        #elif 'my internet' in query:
           # def speed(speed):
                #speed.Speedtest()  # ----------------------Bug
              #  download = speed .download()
               # upload = speed.upload()
               # print(f"Download Speed{download}")
               # print(f"Upload Speed {upload}")


        #elif 'show' in query:
            #os.system('Vision.py')

        elif 'what is the weather' in query:

            subprocess.call(r'WeatherSmart')





        # in connect.py

        else:
            query = query
            print('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
                  
    
            except:
                ()










