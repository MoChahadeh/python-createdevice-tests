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
output_fs = 44100


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

def delay(time):

    time = np.arange(0, time, 1/fs)

    return time * 0


def mozart_eine_kleine_nachtmusik(octave):
    base_octave = octave * int(fs/output_fs)

    # play Mozart's Eine Kleine Nachtmusik
    sound = np.array([], dtype=np.float32)
    sound = np.append(sound, play_note("G", base_octave, time(0.75)))
    sound = np.append(sound, play_note("D", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.75)))
    sound = np.append(sound, play_note("D", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))
    sound = np.append(sound, play_note("D", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))
    sound = np.append(sound, play_note("B", base_octave, time(0.25)))
    sound = np.append(sound, play_note("D", base_octave+1, time(1)))

    sound = np.append(sound, play_note("C", base_octave+1, time(0.75)))
    sound = np.append(sound, play_note("A", base_octave, time(0.25)))
    sound = np.append(sound, play_note("C", base_octave+1, time(0.75)))
    sound = np.append(sound, play_note("A", base_octave, time(0.25)))
    sound = np.append(sound, play_note("C", base_octave+1, time(0.25)))
    sound = np.append(sound, play_note("A", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))
    sound = np.append(sound, play_note("A", base_octave, time(0.25)))
    sound = np.append(sound, play_note("D", base_octave, time(1)))

    sound = np.append(sound, play_note("G", base_octave, time(0.5)))
    sound = np.append(sound, play_note("G", base_octave, time(0.75)))
    sound = np.append(sound, play_note("B", base_octave, time(0.25)))
    sound = np.append(sound, play_note("A", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))
    sound = np.append(sound, play_note("F#", base_octave, time(0.25)))
    sound = np.append(sound, play_note("F#", base_octave, time(0.75)))

    sound = np.append(sound, play_note("A", base_octave, time(0.25)))
    sound = np.append(sound, play_note("B", base_octave, time(0.25)))
    sound = np.append(sound, play_note("F#", base_octave, time(0.25)))
    sound = np.append(sound, play_note("A", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.75)))

    sound = np.append(sound, play_note("B", base_octave, time(0.25)))
    sound = np.append(sound, play_note("A", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))
    sound = np.append(sound, play_note("F#", base_octave, time(0.25)))
    sound = np.append(sound, play_note("F#", base_octave, time(0.75)))

    sound = np.append(sound, play_note("A", base_octave, time(0.25)))
    sound = np.append(sound, play_note("B", base_octave, time(0.25)))
    sound = np.append(sound, play_note("F#", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))
    sound = np.append(sound, play_note("G", base_octave, time(0.25)))

    sound = np.append(sound, play_note("G", base_octave, time(0.125)))
    sound = np.append(sound, play_note("A", base_octave, time(0.125)))
    sound = np.append(sound, play_note("B", base_octave, time(0.25)))
    sound = np.append(sound, play_note("B", base_octave, time(0.25)))
    sound = np.append(sound, play_note("B", base_octave, time(0.25)))

    sound = np.append(sound, play_note("A", base_octave, time(0.125)))
    sound = np.append(sound, play_note("B", base_octave, time(0.125)))
    sound = np.append(sound, play_note("C", base_octave+1, time(0.25)))
    sound = np.append(sound, play_note("C", base_octave+1, time(0.25)))
    sound = np.append(sound, play_note("C", base_octave+1, time(0.25)))

    sound = np.append(sound, play_note("B", base_octave, time(0.125)))
    sound = np.append(sound, play_note("C", base_octave+1, time(0.125)))
    sound = np.append(sound, play_note("D", base_octave+1, time(0.75)))


    sd.play(sound, output_fs)
    sd.wait()
    write("mozart_eine_kleine_nachtmusik_python(mochahadeh.com).wav", output_fs, sound)

mozart_eine_kleine_nachtmusik(3)