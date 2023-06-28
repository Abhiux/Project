from gtts import gTTS  #imported this module for text to speech conversion
import os

abc=open('sample.txt')
text=abc.read() #text that you want to convert

language='en' #en is for english language

obj=gTTS(text=text,lang=language,slow=False)
#used slow = False because our converted video will have a high speed
obj.save("sample.mp3")

#to open the video file automatically we have to import os
os.system("sample.mp3")