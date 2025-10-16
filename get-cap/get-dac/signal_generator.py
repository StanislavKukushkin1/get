import numpy as np
import time

def get_sin_wave_amplitude(freq, current_time):
    return (np.sin(2*np.pi*freq*current_time) + 1)/2

def wait_for_sampling_period(sampling_frequency):
    sampling_period = 1.0/sampling_frequency
    return sampling_period

def get_triangle_wave_amplitude(freq,current_time):
    period = 1.0/ freq
    phase = current_time % period / period

    return 2 * min (phase, 1 - phase)
