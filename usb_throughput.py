import numpy as np
import adi
import matplotlib.pyplot as plt
import time

sample_rate = 1000000 # Hz
center_freq = 100e6 # Hz

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_lo = int(center_freq)
sdr.rx_buffer_size = 2048000
start_time = time.time()
read_num = 10
for i in range(read_num):
    samples = sdr.rx()
end_time = time.time()
secs = end_time - start_time
print(samples[1])
print('seconds elapsed:', secs)
print('samples per sec:', read_num / secs)
print('bits received:', read_num * sdr.rx_buffer_size)
print('bits per sec:', (read_num * sdr.rx_buffer_size) / secs)

