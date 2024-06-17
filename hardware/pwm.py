# module defining functions for enabling and setting PWM characteristics on the BBAI64

import os

def enable_pwm_channel(channel_path, enable):
    enable_path = os.path.join(channel_path, "enable")
    try:
        with open(enable_path, 'w') as enbl_file:
            enbl_file.write("1" if enable else "0")
        print(f"{'Enabled' if enable else 'Disabled'} PWM at {enable_path}")
    except IOError as e:
        print(f"Failed to {'enable' if enable else 'disable'} PWM at {enable_path}: {e}")

def set_pwm_period(pwm_chip, pwm_channel, period_ns):
    period_path = f"/sys/class/pwm/{pwm_chip}/{pwm_channel}/period"
    try:
        with open(period_path, 'w') as period_file:
            period_file.write(str(period_ns))
        print(f"Set PWM period for {pwm_chip}/{pwm_channel} to {period_ns} ns")
    except IOError as e:
        print(f"Failed to set PWM period: {e}")

def set_pwm_dc(pwm_chip, pwm_channel, dc_ns):
    dc_path = f"/sys/class/pwm/{pwm_chip}/{pwm_channel}/duty_cycle"
    try:
        with open(dc_path, 'w') as dc_file:
            dc_file.write(str(dc_ns))
        print(f"Set PWM duty cycle for {pwm_chip}/{pwm_channel} to {dc_ns} ns")
    except IOError as e:
        print(f"Failed to set PWM duty cycle: {e}")
