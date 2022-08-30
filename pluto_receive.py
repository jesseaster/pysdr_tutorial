import numpy as np
import adi
import time


sample_rate = 1e6  # Hz
center_freq = 1000e6  # Hz
num_samples = 1000000  # number of samples returned per call to rx()

sdr = adi.Pluto('ip:192.168.2.1')
sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 0.0  # dB
sdr.rx_lo = int(center_freq)
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate)  # filter width, same as sample rate for now
sdr.rx_buffer_size = num_samples

start_time = time.time()
samples = sdr.rx()  # receive samples off Pluto
end_time = time.time()
t_diff = end_time - start_time
print('t_diff: ', t_diff)
print('sample_len: ', len(samples))
print('samples per sec', len(samples)/ t_diff)
print(samples[0])
print(type(samples[0]))
