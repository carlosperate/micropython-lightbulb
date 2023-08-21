import time
import machine

pin_white_cold = machine.PWM(machine.Pin(5))
pin_white_warm = machine.PWM(machine.Pin(13))
pin_r = machine.PWM(machine.Pin(4))
pin_g = machine.PWM(machine.Pin(12))
pin_b = machine.PWM(machine.Pin(14))
all_pwm_pins = (pin_r, pin_g, pin_b, pin_white_warm, pin_white_cold)


def off():
    for pwm_pin in all_pwm_pins:
        pwm_pin.duty(0)


def flash_pwm():
    off()

    for pwm_pin in all_pwm_pins:
        for i in range(1024):
            pwm_pin.duty(i)
            time.sleep_ms(1)
        for i in reversed(range(1024)):
            pwm_pin.duty(i)
            time.sleep_ms(1)


def flash():
    off()

    for pwm_pin in all_pwm_pins:
        pwm_pin.duty(1024)
        time.sleep_ms(1000)
        pwm_pin.duty(0)