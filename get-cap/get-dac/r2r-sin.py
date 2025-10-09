import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequecy = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16,20,21,25,26,17,27,22], 3.17, True)

        while True:
            try:
                
                dac.set_voltage(sg(signal_frequecy))
                sg.wait_for_sampling_period(sampling_frequency)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()
