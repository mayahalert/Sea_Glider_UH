from config import *
from hardware.pwm import PWMController
import time

# Initialize PWM controller for m4 led on motor cape
pwm = PWMController(PWM_CHIP_BASE, PWM_PERIOD_NS)

try:
    # Fade LED up to 100% and down to 0% over 5 seconds
    fade_time = 5  # total fade time in seconds
    steps = 100  # number of steps for smooth fade
    step_time = fade_time / steps  # time per step

    # Fade up
    for i in range(steps + 1):
        duty_cycle = int(PWM_PERIOD_NS * (i / steps))
        pwm.set_pwm_dc(M4_PATH, duty_cycle)
        time.sleep(step_time)

    # Fade down
    for i in range(steps, -1, -1):
        duty_cycle = int(PWM_PERIOD_NS * (i / steps))
        pwm.set_pwm_dc(M4_PATH, duty_cycle)
        time.sleep(step_time)

except KeyboardInterrupt:
    # Turn off LED and exit on Ctrl+C
    pwm.set_pwm_dc(0)