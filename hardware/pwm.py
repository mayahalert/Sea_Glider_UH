# module defining functions for enabling and setting PWM characteristics on the BBAI64
from config import *
import os

class PWMController:
    def __init__(self, pwm_chip_base, pwm_channel_path, period_ns):
        self.pwm_chip_base = pwm_chip_base
        self.pwm_channel_path = pwm_channel_path
        self.period_ns = period_ns
        
        # Set the period for both channels
        self.set_pwm_period(pwm_chip_base, "pwm0", period_ns)
        self.set_pwm_period(pwm_chip_base, "pwm1", period_ns)

        # Enable both PWM channels initially
        self.enable_pwm_channel(pwm_chip_base, "pwm0", True)
        self.enable_pwm_channel(pwm_chip_base, "pwm1", True)

    # function to enable or disable a PWM channel by setting the enable file in the channel directory to 1 or 0
    def enable_pwm_channel(self, channel_path, enable):
        enable_path = os.path.join(channel_path, "enable")
        try:
            with open(enable_path, 'w') as enbl_file:
                enbl_file.write("1" if enable else "0")
        except IOError as e:
            print(f"Failed to {'enable' if enable else 'disable'} PWM at {enable_path}: {e}")

    # function to set the period of a PWM channel by writing the desired period in nanoseconds to the period file in the channel directory
    def set_pwm_period(self, pwm_channel_path, period_ns):
        period_path = f"{pwm_channel_path}/period"
        try:
            with open(period_path, 'w') as period_file:
                period_file.write(str(period_ns))
        except IOError as e:
            print(f"Failed to set PWM period: {e}")

    # function to set the duty cycle of a PWM channel by writing the desired duty cycle in nanoseconds to the duty_cycle file in the channel directory
    def set_pwm_dc(self, pwm_channel_path, dc_percent):
        dc_path = f"{pwm_channel_path}/duty_cycle"
        
        if dc_percent <= 5:
            # Disable the channel
            dc_ns = 0
        elif dc_percent >= 85:
            dc_ns = PWM_DC_MAX_NS
        else:
            # Linear interpolation between 0 and 800000 ns
            dc_ns = int((dc_percent / 80) * 800000)
        
        try:
            with open(dc_path, 'w') as dc_file:
                dc_file.write(str(dc_ns))
        except IOError as e:
            print(f"Failed to set PWM duty cycle: {e}")