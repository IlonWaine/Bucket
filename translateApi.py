# import pyttsx3
import threading
# from plyer import tts
from plyer import tts

        # Use the Plyer TTS API for Android TTS
#driverName='espeak'
# engine = pyttsx3.init()
# engine.setProperty("rate", 120) 
# def speak(word):
#     # engine.setProperty("rate", rate)
#     engine.say(word)
#     engine.runAndWait()
  
# word = input('write word: ')
# # rate = input('write word: ')
# while word!='0':
#     speak(word)
#     word = input('write word: ')
#     # rate = input('write word: ')

def speak(word):
    tts.speak(word)
    # engine.say(word)
    # engine.runAndWait()

# def closePyttsx3():
#     pyttsx3.
#     print('close audio engine')


def giveSound(word):    
    speech_thread = threading.Thread(target=speak, args=(word,))
    # Start the text-to-speech thread
    speech_thread.start()
















# pip install gTTS
# pip install pygame


 
# import pygame.mixer


            # from gtts import gTTS
            # import sounddevice as sd
            # from io import BytesIO
            # from googletrans import Translator

            # import numpy as np
            # import wave


# text = 'hello'
# tts = gTTS(text)

# translator = Translator()
# tr=translator.translate('lest',dest='uk',src='en')
# print(tr.text)

# audio_data = BytesIO(tts.save(text))


# # Rewind the stream to the beginning

# audio_data = wave.open(audio_data)
# audio_data = audio_data.readframes(-1)
# audio_data = np.frombuffer(audio_data, dtype="int16")

# sd.play(audio_data, audio_data.dtype)
# sd.wait()