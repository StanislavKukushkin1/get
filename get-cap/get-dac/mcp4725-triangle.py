import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 2.0
signal_frequency = 10
sampling_frequency = 1000



if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(5.18)
        while True:
            try:
              
                signal_amplitude = sg.get_triangle_wave_amplitude(signal_frequency, time.time())
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