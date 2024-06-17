from hardware.gpio import out_gpio
from hardware.pwm import enable_pwm_channel, set_pwm_dc
from hardware.adc import read_adc
import config

def stop_motor(pwm_channel, pwm_path, dir_pin, state, motor_label):
    enable_pwm_channel(pwm_path, False)  # Stop motor
    set_pwm_dc("pwmchip0", pwm_channel, 0)  # Set DC to 0 for safety
    print(f"Stopped {motor_label} motor, set direction to {state}")

def control_motor(pot_path, dir_pin, pwm_channel, pwm_path, adc_ref_val, motor_label):
    pot_val = read_adc(pot_path)
    if pot_val is None:
        return
    
    if 1.1 * config.ADC_MIN < pot_val < 0.5 * adc_ref_val:
        out_gpio("gpiochip1", dir_pin, 0)  # Set direction to low
        while 1.1 * config.ADC_MIN < pot_val < 0.5 * adc_ref_val:
            set_pwm_dc("pwmchip0", pwm_channel, config.PWM_DC_NS)  # Drive to limit
            pot_val = read_adc(pot_path)
        stop_motor(pwm_channel, pwm_path, dir_pin, "low", motor_label)

        out_gpio("gpiochip1", dir_pin, 1)  # Reverse direction
        while pot_val < 0.9 * adc_ref_val:
            set_pwm_dc("pwmchip0", pwm_channel, config.PWM_DC_NS)  # Drive at 25%
            pot_val = read_adc(pot_path)
        stop_motor(pwm_channel, pwm_path, dir_pin, "high", motor_label)

    else:
        out_gpio("gpiochip1", dir_pin, 1)
        while pot_val < 0.9 * adc_ref_val:
            set_pwm_dc("pwmchip0", pwm_channel, config.PWM_DC_NS)  # Drive to limit
            pot_val = read_adc(pot_path)
        stop_motor(pwm_channel, pwm_path, dir_pin, "high", motor_label)

        out_gpio("gpiochip1", dir_pin, 0)
        while 1.1 * config.ADC_MIN < pot_val < 0.5 * adc_ref_val:
            set_pwm_dc("pwmchip0", pwm_channel, config.PWM_DC_NS)  # Drive at 25%
            pot_val = read_adc(pot_path)
        stop_motor(pwm_channel, pwm_path, dir_pin, "low", motor_label)
