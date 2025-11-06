import smbus
import time
import matplotlib.pyplot as plt

class MCP3021:
    def __init__(self, dynamic_range, verbose=False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        return number

    def get_voltage(self):
        number = self.get_number()
        voltage = (number / 1023.0) * self.dynamic_range
        return voltage

    def cleanup(self):
        self.deinit()

def plot_voltage_vs_time(time_values, voltage_values):
    plt.figure(figsize=(12, 6))
    plt.plot(time_values, voltage_values, 'b-', linewidth=1)
    plt.title('Зависимость напряжения на фоторезисторе от времени')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    voltage_values = []
    time_values = []
    duration = 30
    
    try:
        mcp = MCP3021(dynamic_range=3.3, verbose=False)
        start_time = time.time()
        
        while (time.time() - start_time) < duration:
            voltage = mcp.get_voltage()
            current_time = time.time() - start_time
            
            voltage_values.append(voltage)
            time_values.append(current_time)
            
            print(f"Время: {current_time:.1f} с, Напряжение: {voltage:.3f} В")
            time.sleep(0.1)
        
        plot_voltage_vs_time(time_values, voltage_values)
        
        if voltage_values:
            print(f"Минимальное напряжение: {min(voltage_values):.3f} В")
            print(f"Максимальное напряжение: {max(voltage_values):.3f} В")

    except Exception as e:
        print(f"Ошибка: {e}")
    
    finally:
        mcp.deinit()
        print("Измерение завершено")
