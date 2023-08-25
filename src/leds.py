import time
import machine


pin_white_cold = machine.PWM(machine.Pin(5))
pin_white_warm = machine.PWM(machine.Pin(13))
pin_r = machine.PWM(machine.Pin(4))
pin_g = machine.PWM(machine.Pin(12))
pin_b = machine.PWM(machine.Pin(14))
all_pwm_pins = (pin_r, pin_g, pin_b, pin_white_warm, pin_white_cold)

COLOUR_RANGE = (0, 255)
PWM_RANGE = (0, 768)


def map(value, from_range, to_range):
    return int(
        to_range[0] + \
            (((value - from_range[0]) / (from_range[1] - from_range[0])) * \
                (to_range[1] - to_range[0]))
    )


def set_all(red, green, blue, white_cold, white_warm):
    print((red, green, blue, white_cold, white_warm))
    pin_r.duty(map(red, COLOUR_RANGE, PWM_RANGE))
    pin_g.duty(map(green, COLOUR_RANGE, PWM_RANGE))
    pin_b.duty(map(blue, COLOUR_RANGE, PWM_RANGE))
    pin_white_cold.duty(map(white_cold, COLOUR_RANGE, PWM_RANGE))
    pin_white_warm.duty(map(white_warm, COLOUR_RANGE, PWM_RANGE))


def off():
    for pwm_pin in all_pwm_pins:
        pwm_pin.duty(0)


def flash_pwm():
    off()

    for pwm_pin in all_pwm_pins:
        for i in range(1024):
            pwm_pin.duty(i)
            time.sleep(0.001)
        for i in reversed(range(1024)):
            pwm_pin.duty(i)
            time.sleep(0.001)


def flash():
    off()

    for pwm_pin in all_pwm_pins:
        pwm_pin.duty(1024)
        time.sleep_ms(1000)
        pwm_pin.duty(0)
