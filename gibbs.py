import numpy as np
import matplotlib.pyplot as plt


N = 500 # Number of points
sample_rate = 1e11

t = np.arange(N)/sample_rate
f = 5e8  # 500 MHz Frequency of starting wave
x1 = np.sin(2 * np.pi * f * t)
x2 = (1/3) * np.sin(3 * 2 * np.pi * f * t)
x3 = (1/5) * np.sin(5 * 2 * np.pi * f * t)
x4 = (1/7) * np.sin(7 * 2 * np.pi * f * t)
x5 = (1/9) * np.sin(9 * 2 * np.pi * f * t)
x = x1 + x2 + x3 + x4 + x5

plt.plot(t, x)
plt.show()
