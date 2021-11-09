
import speed_reading

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

import speech_recognition as s

from threading import *

sr = s.Recognizer()

freq = 44100
duration = 15
a = 'gajendra'

print('Start reading')


class Jan(Thread):
    def run(self):
        with s.Microphone() as m:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)


class Voice(Thread):
    def run(self):
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
        sd.wait()

        write("recording0.wav", freq, recording)

        # Convert the NumPy array to audio file
        wv.write("recording1.wav", recording, freq, sampwidth=2)


class Gaj(Thread):
    def run(self):
        print(speed_reading)


t1 = Jan()
t2 = Voice()
t3 = Gaj()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
