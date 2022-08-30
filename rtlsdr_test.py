from rtlsdr import RtlSdr
import numpy as np
import matplotlib.pyplot as plt


sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.48e6  # Hz
print(sdr.sample_rate)
sdr.center_freq = 915e6     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

fft_size = 1024
lines = 4000
x = sdr.read_samples(fft_size*lines)
sdr.close()

num_rows = int(np.floor(len(x)/fft_size))
spectrogram = np.zeros((num_rows, fft_size))
for i in range(num_rows):
    x_s = x[i * fft_size:(i + 1) * fft_size]
    x_s = x_s * np.hamming(fft_size)
    spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x_s)))**2)
spectrogram = spectrogram[:,fft_size//2:] # get rid of negative freqs because we simulated a real signal

plt.imshow(spectrogram, aspect='auto', extent = [0, sdr.sample_rate/2/1e6, 0, len(x)/sdr.sample_rate])
plt.xlabel("Frequency [MHz]")
plt.ylabel("Time [s]")
plt.show()



