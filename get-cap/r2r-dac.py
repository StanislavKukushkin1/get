import RPi.GPIO as GPIO
dynamic_range = 3.17

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)


    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

        
    def set_number(self, number):
        lig = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(gpio_bits, lig)

        
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"Напряжение выходит за динамический ЦАП (0.00 - {dynamic_range:.2f} ) В")
            GPIO.output(lens,0)
            self.set_number(0)
            return 0
        self.set_number(int(voltage/dynamic_range * 255))
        return int(voltage/dynamic_range * 255)

    
if __name__ == "__main__":
    try:
        dac = R2R_DAC([16,20,21,25,26,17,27,22], 3.17, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_volatge(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()


