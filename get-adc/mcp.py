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

def plot_sensors_vs_time(time_values, photo_voltages, thermo_voltages):
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(time_values, photo_voltages, 'b-', linewidth=1)
    plt.title('Напряжение на фоторезисторе')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 1, 2)
    plt.plot(time_values, thermo_voltages, 'r-', linewidth=1)
    plt.title('Напряжение на терморезисторе')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    photo_voltages = []
    thermo_voltages = []
    time_values = []
    duration = 10
    
    try:
        mcp_photo = MCP3021(dynamic_range=3.3, verbose=False)
        mcp_thermo = MCP3021(dynamic_range=3.3, verbose=False)

        
        start_time = time.time()
        
        while (time.time() - start_time) < duration:
            current_time = time.time() - start_time
            
            photo_voltage = mcp_photo.get_voltage()
            thermo_voltage = mcp_thermo.get_voltage()
            
            photo_voltages.append(photo_voltage)
            thermo_voltages.append(thermo_voltage)
            time_values.append(current_time)
            
            print(f"Время: {current_time:.1f} с, Фото: {photo_voltage:.3f} В, Термо: {thermo_voltage:.3f} В")
            
            time.sleep(0.1)
        
        plot_sensors_vs_time(time_values, photo_voltages, thermo_voltages)
        
    except Exception as e:
        print(f"Ошибка: {e}")
    
    finally:
        mcp_photo.deinit()
        mcp_thermo.deinit()
