import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.17
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16,20,21,25,26,17,27,22], 3.17, True)

        while True:
            try:
                signal_amplitude = sg.get_sin_wave_amplitude(signal_frequency, time.time())
                voltage = signal_amplitude * amplitude
                dac.set_voltage(voltage)
                time.sleep(sg.wait_for_sampling_period(sampling_frequency))

            except ValueError:
                print("Ошибка значения. Попробуйте еще раз\n")
            except KeyboardInterrupt:
                print("\nПрограмма завершена")
                break
    finally:
        dac.deinit()
