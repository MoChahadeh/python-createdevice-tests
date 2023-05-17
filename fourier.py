import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

fs = 44100

def time(seconds):
    return np.arange(0, seconds, 1/fs)


duration = 5
sound_in = np.array([], dtype=np.float32)
def in_callback(indata, frames, time, status):
    global sound_in
    sound_in = np.append(sound_in, indata)

with sd.InputStream(samplerate=fs, channels=1,callback=in_callback, dtype=np.float32) as stream:
    print("RECORDING")
    while True:
        print(stream.time)
        if len(sound_in) > fs*duration:
            break

print("DONE RECORDING")

sleep(1)

fourier = np.fft.fft(sound_in)
fourier = np.fft.fftfreq(len(fourier), 1/fs)

# # cut out the negative frequencies
# fourier = fourier[0:int(len(fourier)/2)]

# # cut out frequencies above between 1900 and 2100 Hz
# fourier[1900:2100] /= 1000

fourier = np.abs(fourier)

# get the inverse fourier transform
sound_out = np.fft.ifft(fourier)
sound_out = np.real(sound_out)

sd.play(sound_out, fs)

#plot the sound_in and fourier
plt.subplot(2,1,1)
plt.plot(time(duration), sound_in[0:int(fs*duration)])
plt.subplot(2,1,2)
plt.plot(fourier)
plt.show()
