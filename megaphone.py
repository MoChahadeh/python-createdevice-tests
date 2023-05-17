# May 3rd, 2023
# Author: Mohamad Chahadeh
# Github: MoChahadeh
# Website: https://mochahadeh.com
# License: MIT License
# Assigning credit is not required, but is greatly appreciated.
# Description: Attempting to create a megaphone like behaviour using audiodevice library.


import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from time import sleep
import math
from threading import Thread

fs = 88200

def time(seconds):
    return np.arange(0, seconds, 1/fs)


duration = 10

recording_period = 0.05
sound_in = np.array([], dtype=np.float32)

def in_callback(indata, frames, time, status):
    global sound_in
    sound_in = np.append(sound_in, indata)

print("READY")
sleep(1)

def in_():
    global sound_in
    with sd.InputStream(samplerate=fs, channels=1,callback=in_callback, dtype=np.float32) as stream:
        print("RECORDING")
        while True:
            print(stream.time)
            sleep(recording_period)

def out_():
    volume_multiplier = 4
    with sd.OutputStream(samplerate=fs, channels=1, dtype=np.float32) as stream:
        print("PLAYING")
        while(True):
            stream.write(volume_multiplier*sound_in[-int(fs*recording_period):])
            print("playing")
            sleep(recording_period)

def save_recording():
    
    while True:
        input("Press Enter to save the recording..")
        write("recording.wav", fs, sound_in)



try:
    in_thread   = Thread( target=in_ )
    out_thread  = Thread( target=out_ )
    save_thread = Thread( target=save_recording )

    in_thread.start()
    out_thread.start()
    save_thread.start()
except:
   print("Error: unable to start thread")
   exit(1)
