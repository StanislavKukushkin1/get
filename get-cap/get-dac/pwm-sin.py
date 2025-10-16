import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.173
signal_frequency = 10
sampling_frequency = 2000

if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC(12, 500, 3.173, True)

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
