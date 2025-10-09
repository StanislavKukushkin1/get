import numpy as np
import time as time

def get_sin_wave_amplitude(freq):
    return (np.sin(2*np.pi*freq*time.time()) + 1)/2

def wait_for_sampling_period(sampling_frequency):
    sampling_period = 1.0/sampling_frequency
    return sampling_period