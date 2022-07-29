from ast import For
import random
import string
import datetime
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from cgitb import text
import pyttsx3
import speech_recognition as sr #pip install speechRecognition
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[2].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


    




print(Fore.BLUE+Back.YELLOW+ "Hi  sir This is Nitro ,Made by Saptaparna" + Fore.YELLOW+ Back.BLUE+"How are u doing.")
print(Fore.RED + Back.GREEN+"Its nice to meet you.")
print(Fore.RED+Back.CYAN+"Welcome to Password Picker")
speak("Hi Sir ,  This is Nitro ,  made by Saptaparna , How are u doing , Welcome to Password Picker , Its nice to meet you.")
speak("What is you name sir kindly please write it down")
a=input("What is you name sir kindly please write it down :")
speak("Hi")
speak(a)


adjectives = ['Mota', 'Fat', 'Losser', 'Tommy', 'Hot',  'Cringe', 'Creep', 'Toxic', 'Adoreble', 'Lame', 'Cool', 'Tall', 'Hate']
nouns = ['joyda', 'sourav', 'tommyda', 'sapta', 'joyda', 'sourav', 'tommyda', 'sapta']

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 10)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print(Fore.BLUE+"You requierment is : %s" % password)
    speak("Your password is")
    speak(password)
    
    speak("Would you like another password sir?")
    response = input(Fore.GREEN+Back.YELLOW+"Would you like another password?"+Fore.BLUE+Back.CYAN+"Type"+Fore.WHITE+Back.GREEN+"Y"+Fore.WHITE+Back.GREEN+"N")
    if response == 'N':
        print("Thanks for using me!")
        speak("Thanks for using me ")
        print(Fore.BLUE+Back.YELLOW+"Have"+Fore.YELLOW+Back.CYAN+"A"+Fore.GREEN+Back.BLUE+"Nice"+Fore.GREEN+Back.YELLOW+"Day")
        speak("Have a nice day.")
        break 

