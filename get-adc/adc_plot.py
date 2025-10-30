import matplotlib.pyplot as plt
from r2r_adc import R2R_ADC 
import time

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.plot(time,voltage)

    plt.title("Зависимость напряжения от времени")
    plt.ylabel('Напряжение, В')
    plt.xlabel('Время, с')
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(time):

    sampling_periods = []

    for i in range(1,len(time)):
        period = time[i] - time[i-1]
        sampling_periods.append(period)

    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods,)

    plt.title("Распределение периодов дискретиsзации измерений по времени на одно измерение")
    plt.ylabel('Количество измерений')
    plt.xlabel('Период измерения, с')
    plt.xlim(0,0.06)
    plt.legend()
    plt.grid(True)
    plt.show()

adc = R2R_ADC(3.30)
voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while (time.time()-start_time) < duration:

        voltage = adc.get_sc_voltage()
        voltage_values.append(voltage)

        current_time = time.time() - start_time
        time_values.append(current_time)

    plot_voltage_vs_time(time_values, voltage_values, 3.30)
    plot_sampling_period_hist(time_values)
finally:
    adc.cleanup()




