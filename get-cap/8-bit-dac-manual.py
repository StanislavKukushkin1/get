import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pins = [16,20,21,25,26,17,27,22] #safasf
GPIO.setup(pins, GPIO.OUT)
dynamic_range = 3.17
def voltage_to_number(voltage): #вольты в число (от 0 до 255)
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический ЦАП (0.00 - {dynamic_range:.2f} ) В")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage/dynamic_range * 255)

def number_to_dac(number): #число в двоичный код
    number = [int(bit) for bit in bin(number)[2:].zfill(8)]
    GPIO.output(pins, number)
    #сообщить число R2R-цап


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах"))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число, попробуйте еще раз \n")
finally:
    GPIO.output(pins,0)
    GPIO.cleanup()