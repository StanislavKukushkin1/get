import smbus
import time

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
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte:x}, Число: {number}")
        return number

    def get_voltage(self):
        number = self.get_number()
        voltage = (number / 1023.0) * self.dynamic_range
        return voltage

    def cleanup(self):
        self.deinit()

if __name__ == "__main__":
    try:
        mcp = MCP3021(dynamic_range=5.0, verbose=True)
        
        while True:
            voltage = mcp.get_voltage()
            print(f"MCP3021 Напряжение: {voltage:.2f} В")
            time.sleep(1)

    finally:
        mcp.deinit()
