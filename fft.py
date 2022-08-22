import numpy as np
import matplotlib.pyplot as plt


# https://pysdr.org/content/frequency_domain.html

Fs = 1  # Sample Rate, Hz
N = 1000 # number of points to simulate, and our FFT size

t = np.arange(N)
s = np.sin(0.15 * 2 * np.pi * t)

#s = s * np.hamming(N)
S = np.fft.fftshift(np.fft.fft(s))

S_mag = np.abs(S)
S_phase = np.angle(S)
f = np.arange(Fs/-2, Fs/2, Fs/N)
plt.figure(0)
plt.plot(f, S_mag, '.-')
plt.figure(1)
plt.plot(f, S_phase, '.-')
plt.show()
