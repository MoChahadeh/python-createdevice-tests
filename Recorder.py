# May 3rd, 2023
# Author: Mohamad Chahadeh
# Github: MoChahadeh
# Website: https://mochahadeh.com
# License: MIT License
# Assigning credit is not required, but is greatly appreciated.
# Description: This file contains functions that can be used to play musical notes and create songs using the notes.


import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from time import sleep
import math

fs = 44100

def time(seconds):
    return np.arange(0, seconds, 1/fs)


duration = 10

sound_in = np.array([], dtype=np.float32)

def in_callback(indata, frames, time, status):
    global sound_in
    sound_in = np.append(sound_in, indata)

print("READY")
sleep(1)
with sd.InputStream(samplerate=fs, channels=1,callback=in_callback, dtype=np.float32) as stream:
    print("RECORDING")
    while True:
        print(stream.time)
        sleep(1)
        if len(sound_in) > duration * fs:
            break


playback_speed = 0.5
volume_multiplier = 2
with sd.OutputStream(samplerate=fs*playback_speed, channels=1, dtype=np.float32) as stream:
    write("recording.wav", int(fs*playback_speed), volume_multiplier*sound_in)
    stream.write(volume_multiplier*sound_in)