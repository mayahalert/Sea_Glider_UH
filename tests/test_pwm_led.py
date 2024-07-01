from config import *
from hardware.pwm import PWMController
import time
import unittest

# Initialize PWM controller for m4 led on motor cape
pwm = PWMController(PWM_CHIP_BASE, PWM_PERIOD_NS)

pwm.set_pwm_dc(M3_PATH, 10)
pwm.set_pwm_dc(M4_PATH, 90)
time.sleep(1)
pwm.set_pwm_dc(M3_PATH, 25)
pwm.set_pwm_dc(M4_PATH, 75)
time.sleep(1)
pwm.set_pwm_dc(M3_PATH, 50)
pwm.set_pwm_dc(M4_PATH, 50)
time.sleep(1)
pwm.set_pwm_dc(M3_PATH, 75)
pwm.set_pwm_dc(M4_PATH, 25)
time.sleep(1)
pwm.set_pwm_dc(M3_PATH, 90)
pwm.set_pwm_dc(M4_PATH, 10)
time.sleep(1)
pwm.set_pwm_dc(M3_PATH, 10)
pwm.set_pwm_dc(M4_PATH, 90)
time.sleep(1)
pwm.set_pwm_dc(M3_PATH, 90)
pwm.set_pwm_dc(M4_PATH, 10)
time.sleep(1)
pwm.set_pwm_dc(M3_PATH, 10)
pwm.set_pwm_dc(M4_PATH, 90)
time.sleep(1)
pwm.set_pwm_dc(M3_PATH, 90)
pwm.set_pwm_dc(M4_PATH, 10)
time.sleep(1)
pwm.set_pwm_dc(M3_PATH, 0)
pwm.set_pwm_dc(M4_PATH, 0)

