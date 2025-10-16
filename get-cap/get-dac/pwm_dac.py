import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin,GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        self.pwm.stop()
        GPIO.cleanup()

    def set_voltage(self,voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический ЦАП (0.00 - {self.dynamic_range:.2f} ) В")
            
            self.pwm.ChangeDutyCycle(0)
            return 0
        duty_cycle = (voltage/self.dynamic_range) * 100
        self.pwm.ChangeDutyCycle(duty_cycle)
        print(f" Заполнение: {duty_cycle}")
        return duty_cycle

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.173, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()