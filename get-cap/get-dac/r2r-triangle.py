import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 2.0
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16,20,21,25,26,17,27,22], 3.173, True)

        while True:
            try:
                signal_amplitude = sg.get_triangle_wave_amplitude(signal_frequency, time.time())
                voltage = signal_amplitude * amplitude
                dac.set_voltage(voltage)
                time.sleep(sg.wait_for_sampling_period(sampling_frequency))


            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()
