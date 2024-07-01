# module to control GPIO pins on the BBAI64

import os
import time

class GPIOControl:
    def __init__(self):
        self.gpio_base_path = '/sys/class/gpio'

    def export_pin(self, gpio_number):
        """
        Export a GPIO pin.
        
        :param gpio_number: The GPIO pin number to export.
        """
        export_path = os.path.join(self.gpio_base_path, 'export')
        if not os.path.exists(os.path.join(self.gpio_base_path, f'gpio{gpio_number}')):
            with open(export_path, 'w') as f:
                f.write(str(gpio_number))
            time.sleep(0.1)  # Give the system time to create the necessary files

    def unexport_pin(self, gpio_number):
        """
        Unexport a GPIO pin.
        
        :param gpio_number: The GPIO pin number to unexport.
        """
        unexport_path = os.path.join(self.gpio_base_path, 'unexport')
        if os.path.exists(os.path.join(self.gpio_base_path, f'gpio{gpio_number}')):
            with open(unexport_path, 'w') as f:
                f.write(str(gpio_number))

    def setup_pin(self, gpio_number, direction='out', default_value=0):
        """
        Setup a GPIO pin.
        
        :param gpio_number: The GPIO pin number to set up.
        :param direction: 'out' for output, 'in' for input.
        :param default_value: Default value for the pin (0 or 1).
        """
        self.export_pin(gpio_number)
        
        direction_path = os.path.join(self.gpio_base_path, f'gpio{gpio_number}', 'direction')
        value_path = os.path.join(self.gpio_base_path, f'gpio{gpio_number}', 'value')
        
        with open(direction_path, 'w') as f:
            f.write(direction)
        
        if direction == 'out':
            with open(value_path, 'w') as f:
                f.write(str(default_value))

    def set_value(self, gpio_number, value):
        """
        Set the value of a GPIO pin.
        
        :param gpio_number: The GPIO pin number to set.
        :param value: The value to set (0 or 1).
        """
        value_path = os.path.join(self.gpio_base_path, f'gpio{gpio_number}', 'value')
        if os.path.exists(value_path):
            with open(value_path, 'w') as f:
                f.write(str(value))
        else:
            raise FileNotFoundError(f"Pin gpio{gpio_number} is not set up.")

    def get_value(self, gpio_number):
        """
        Get the value of a GPIO pin.
        
        :param gpio_number: The GPIO pin number to read.
        :return: The value of the pin (0 or 1).
        """
        value_path = os.path.join(self.gpio_base_path, f'gpio{gpio_number}', 'value')
        if os.path.exists(value_path):
            with open(value_path, 'r') as f:
                return int(f.read().strip())
        else:
            raise FileNotFoundError(f"Pin gpio{gpio_number} is not set up.")

    def cleanup(self, gpio_number):
        """
        Unexport a GPIO pin to clean up.
        
        :param gpio_number: The GPIO pin number to unexport.
        """
        self.unexport_pin(gpio_number)

# Example:
# gpio = GPIOControl()
# gpio.setup_pin(351, direction='out', default_value=0)
# gpio.set_value(351, 1)
# print(gpio.get_value(351))
# gpio.cleanup(351)
