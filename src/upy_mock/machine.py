class Pin:

    def __init__(self, pin_number):
        self.pin_number = pin_number


class PWM:

    def __init__(self, pin_obj: Pin):
        self.pin_obj = pin_obj

    def duty(self, value):
        # print("PWM {}: {}".format(self.pin_obj.pin_number, value))
        pass
