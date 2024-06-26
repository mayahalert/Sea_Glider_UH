# module to control GPIO pins on the BBAI64
# probably more efficient way to contorl GPIO pins than using the built-in functions this way in the terminal
# ********* need to test before using********

import subprocess #for interacting with the shell

def out_gpio(chip, pin, value):
    command = f"gpioset {chip} {pin}={value}"
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to set GPIO{pin}: {e}")


#&************************************ NEW FUNCTION ************************************&
import gpiod

class GPIOControl:
    def __init__(self, chip_name='gpiochip0'):
        self.chip = gpiod.Chip(chip_name)
        self.lines = {}

    def setup_pin(self, pin_name, line_num, direction='out', default_value=0):
        """
        Setup a GPIO pin.
        
        :param pin_name: A name to refer to the pin.
        :param line_num: The GPIO line number.
        :param direction: 'out' for output, 'in' for input.
        :param default_value: Default value for the pin (0 or 1).
        """
        line = self.chip.get_line(line_num)
        if direction == 'out':
            line.request(consumer=pin_name, type=gpiod.LINE_REQ_DIR_OUT, default_vals=[default_value])
        elif direction == 'in':
            line.request(consumer=pin_name, type=gpiod.LINE_REQ_DIR_IN)
        else:
            raise ValueError("Direction must be 'out' or 'in'.")
        self.lines[pin_name] = line

    def set_value(self, pin_name, value):
        """
        Set the value of a GPIO pin.
        
        :param pin_name: The name of the pin to set.
        :param value: The value to set (0 or 1).
        """
        if pin_name in self.lines:
            self.lines[pin_name].set_value(value)
        else:
            raise KeyError(f"Pin {pin_name} has not been set up.")

    def get_value(self, pin_name):
        """
        Get the value of a GPIO pin.
        
        :param pin_name: The name of the pin to read.
        :return: The value of the pin (0 or 1).
        """
        if pin_name in self.lines:
            return self.lines[pin_name].get_value()
        else:
            raise KeyError(f"Pin {pin_name} has not been set up.")

    def cleanup(self):
        """
        Release all GPIO pins.
        """
        for pin_name, line in self.lines.items():
            line.release()
        self.chip.close()