import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self,dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26,20,19,16,13,12,25,11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio,GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self,number):
        for i in range(8):
            bit = (number >> i) & 1
            GPIO.output(self.bits_gpio[7-i],bit)

        if self.verbose:
            binary = format(number, '08b')
            
    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 1:
                return number
        return 255.0


    def get_sc_voltage(self):
        digital_value = self.sequential_counting_adc()
        voltage = (digital_value/255.0)*self.dynamic_range
        return voltage

    
    def cleanup(self):
        GPIO.cleanup()


    def successive_approximation_adc(self):
        result = 0
        for bit in range(7,-1,-1):
            test_value = result | (1<<bit)
            self.number_to_dac(test_value)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 0:
                result = test_value
        return result


    def get_sar_voltage(self):
        digital_value = self.successive_approximation_adc()
        voltage = (digital_value/255.0)*self.dynamic_range
        return voltage


if __name__ == "__main__":
    try:
        adc = R2R_ADC(dynamic_range = 3.29)
        while True:
            voltage = adc.get_sar_voltage()
            print(f"Напряжение: {voltage:.2f} В")
            time.sleep(1)
    finally:
        adc.cleanup()


