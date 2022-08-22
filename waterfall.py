import numpy as np
import matplotlib.pyplot as plt


# https://pysdr.org/content/frequency_domain.html

sample_rate = 1e6

# Generate tone plus noise
fft_size = 1024
t = np.arange(fft_size*1000)/sample_rate # time vector
noise = 10
f = 50e3 # freq of tone
x = np.sin(2*np.pi*f*t[0:fft_size*900]) + noise * np.random.randn(fft_size * 900)
x2 = noise * np.random.randn(fft_size*100)
x = np.append(x, x2)

#x = x * np.hamming(N)
num_rows = int(np.floor(len(x)/fft_size))
spectrogram = np.zeros((num_rows, fft_size))
for i in range(num_rows):
    x_s = x[i * fft_size:(i + 1) * fft_size]
    x_s = x_s * np.hamming(fft_size)
    spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x_s)))**2)
spectrogram = spectrogram[:,fft_size//2:] # get rid of negative freqs because we simulated a real signal

plt.imshow(spectrogram, aspect='auto', extent = [0, sample_rate/2/1e6, 0, len(x)/sample_rate])
plt.xlabel("Frequency [MHz]")
plt.ylabel("Time [s]")
plt.show()
