import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# function of accessing (reading) the audio file
def read_file(str):
    sampleRate , audioData= wavfile.read(str)
    return sampleRate , audioData


# plot audio file (time domain) before editing
def plt_time_domain_before(sampleRate,audioData):
    time = np.arange(0,len(audioData))/sampleRate
    plt.figure(figsize=(10,10))
    plt.plot(time,audio)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()


# function of using fourier transform
def fourier_transform():
    # write your code here "" :)
    return


# plot audio file (freq domain) before editing
def plt_freq_domain_before():
    # write your code here "" :)
    return


# apply filter lowpass and high pass filter
def filter_signal():
    return


# plot audio file (freq domain) after editing
def plt_freq_domain_after():
    # write your code here "" :)
    return


# function of using inverse fourier transform
def fourier_inverse_transform():
    # write your code here "" :)
    return


# plot audio file (time domain) after editing
def plt_time_domain_after():
    # write your code here "" :)
    return


# function of saving new audio
def save_file():
    # write your code here "" :)
    return


if __name__ == "__main__":   # we can reduce the number of functions by combining some of them while coding
    read_file()
    plt_time_domain_before()
    fourier_transform()
    plt_freq_domain_before()
    filter_signal()
    plt_freq_domain_after()
    fourier_inverse_transform()
    plt_time_domain_after()
    save_file()
