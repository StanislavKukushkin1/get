import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def set_number(self, number):
        number = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(gpio_bits, number)
        
            
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"Напряжение выходит за динамический ЦАП (0.00 - {dynamic_range:.2f} ) В")
            print("Устанавливаем 0.0 В")
            return 0
        set_number(self, voltage)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    


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


