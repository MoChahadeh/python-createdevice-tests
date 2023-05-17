import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from time import sleep
import math

fs = 22050

def time(seconds):
    return np.arange(0, seconds, 1/fs)


def play_note(note,octave, time, volume= 0.4):

    notes = {
        "C" : 16.35,
        "C#" : 17.32,
        "D" : 18.35,
        "D#" : 19.45,
        "E" : 20.60,
        "F" : 21.83,
        "F#" : 23.12,
        "G" : 24.50,
        "G#" : 25.96,
        "A" : 27.50,
        "A#" : 29.14,
        "B" : 30.87,
    }



    note_freq = notes[note] * 2 ** octave
    sound = np.sin(2 * np.pi * note_freq * time) * np.exp(-0.0004 * 2 * np.pi * note_freq * time) 
    
    sound += np.sin(2 * np.pi * 2 * note_freq * time) * np.exp(-0.0004 * 2 * np.pi * 2 * note_freq * time) /2
    sound += np.sin(2 * np.pi * 3 * note_freq * time) * np.exp(-0.0004 * 2 * np.pi * 3 * note_freq * time) /4
    sound += np.sin(2 * np.pi * 4 * note_freq * time) * np.exp(-0.0004 * 2 * np.pi * 4 * note_freq * time) /8
    sound += np.sin(2 * np.pi * 5 * note_freq * time) * np.exp(-0.0004 * 2 * np.pi * 5 * note_freq * time) /16
    sound += np.sin(2 * np.pi * 6 * note_freq * time) * np.exp(-0.0004 * 2 * np.pi * 6 * note_freq * time) /32
    sound += np.sin(2 * np.pi * 1/2 * note_freq * time) * np.exp(-0.0004 * 2 * np.pi * 7 * note_freq * time) /8
    sound += np.sin(2 * np.pi * 1/4 * note_freq * time) * np.exp(-0.0004 * 2 * np.pi * 8 * note_freq * time) /16
    sound += sound * sound * sound
    sound *= 1 + 16 * time * np.exp(-6 * time)

    sound /= np.max(sound)
    sound *= max(min(1, volume),0)

    return sound

sound = np.array([], dtype=np.float32)

sound = np.append(sound, play_note("C", 4, time(5)))
sound = np.append(sound, play_note("C", 3, time(5)))
sound = np.append(sound, play_note("C", 2, time(5)))
sound = np.append(sound, play_note("C", 1, time(5)))
sound = np.append(sound, play_note("C", 0, time(5)))


sd.play(sound, fs)

import matplotlib.pyplot as plt
plt.plot(time(25), sound, color = "blue")
plt.show()