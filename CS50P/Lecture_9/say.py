import cowsay
import pyttsx3

engine = pyttsx3.init()
this:str = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
