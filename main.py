from config import *
from hardware.pwm import enable_pwm_channel, set_pwm_period
from hardware.gpio import out_gpio
from control.motor_control_law import control_motor
from hardware.adc import read_adc

def initialize_pwm():
    set_pwm_period("pwmchip0", M4_CHANNEL, PWM_PERIOD_NS)
    set_pwm_period("pwmchip0", M3_CHANNEL, PWM_PERIOD_NS)
    enable_pwm_channel(M4_PATH, True)
    enable_pwm_channel(M3_PATH, True)

def initialize_gpio():
    out_gpio("gpiochip1", M3_DIR_PIN, 0)  # Set M3.dir to low
    out_gpio("gpiochip1", M4_DIR_PIN, 0)  # Set M4.dir to low

def main():
    initialize_pwm()
    initialize_gpio()

    adc_ref_val = read_adc(ADC_REF_PATH)
    if adc_ref_val is None:
        print("Failed to read ADC reference value. Exiting.")
        return

    control_motor(ROLL_POT_PATH, M4_DIR_PIN, M4_CHANNEL, M4_PATH, adc_ref_val, "roll")
    control_motor(PITCH_POT_PATH, M3_DIR_PIN, M3_CHANNEL, M3_PATH, adc_ref_val, "pitch")

if __name__ == "__main__":
    main()