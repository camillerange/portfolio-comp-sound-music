# This file contains a program that writes a sine wave to a WAV file
import scipy.io.wavfile as wav
import numpy as np
import math

def main():
        # Part 1
        channels = 1 # mono channel
        sample_format = 32767 # in range [-32767,32767]
        amp = 8192 # 1/4 Maximum possible 16-bit 
        duration = 1 # in seconds 
        freq = 440 # in Hz
        sample_rate = 48000 # samples per second 

        sine_wave = []

        for i in range(sample_rate):
            sample = int(amp * math.sin(2 * math.pi * freq * i / sample_rate))
            sine_wave.append(sample)
            
        sine_wave = np.array(sine_wave, dtype=np.int16)
        wav.write('sine.wav', sample_rate, sine_wave)

# Main
if __name__ == "__main__":
    main()

