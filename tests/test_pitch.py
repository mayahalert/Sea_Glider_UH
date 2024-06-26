#*******work in progress dont test yet********
from config import *
from control.PD_controller import PDController
from hardware.adc import read_adc
from hardware.pwm import PWMController
from hardware.gpio import out_gpio

pos_I = read_adc(PITCH_POT_PATH)  # Read initial position of pitch motor
controller = PDController(Kp=1, Kd=1, setpoint=pos_I)  # Initialize PD controller for pitch motor with gains
pitch_M4 = PWMController(M4_PATH, "pwmchip0", "pwm0", PWM_PERIOD_NS)  # Initialize PWM controller for pitch motor

pos_min, pos_max = None, None  # Initialize position variables
pos_tol = 5  # Define tolerance for position comparison

while True:

    if pos_I < 1000 and pos_min is None:  # Drive to the stop limit closest to start position
        setpoint = ROLL_POT_MIN + 10  # Add a little safety margin to the stop limit value measured earlier
        controller.set_setpoint(setpoint)
        pos = read_adc(PITCH_POT_PATH)
        while PITCH_POT_MIN < pos < setpoint:
            pos = read_adc(PITCH_POT_PATH)
            output_c = controller.compute(pos)
            if output_c > 0:
                out_gpio("gpiochip0", M4_DIR_PIN, 1)  # Set direction pin to high
                pitch_M4.set_pwm_dc("pwmchip0", M4_CHANNEL, output_c)
            elif output_c < 0:
                out_gpio("gpiochip0", M4_DIR_PIN, 0)  # Set direction pin to low
                pitch_M4.set_pwm_dc("pwmchip0", M4_CHANNEL, abs(output_c))
            pos_min = pos  # Update pos_min

    if pos_I > 1000 and pos_max is None:
        pos = read_adc(PITCH_POT_PATH)
        setpoint = ROLL_POT_MAX - 10
        controller.set_setpoint(setpoint)
        while setpoint < pos < PITCH_POT_MAX:
            pos = read_adc(PITCH_POT_PATH)
            output_c = controller.compute(pos)
            if output_c > 0:
                out_gpio("gpiochip0", M4_DIR_PIN, 1)
                pitch_M4.set_pwm_dc("pwmchip0", M4_CHANNEL, output_c)
            elif output_c < 0:
                out_gpio("gpiochip0", M4_DIR_PIN, 0)
                pitch_M4.set_pwm_dc("pwmchip0", M4_CHANNEL, abs(output_c))
            pos_max = pos  # Update pos_max

    # Drive to the midpoint of the total pitch travel
    if pos_min is not None and pos_max is not None:
        pos_F = (pos_max + pos_min) / 2
        controller.set_setpoint(pos_F)
        while abs(pos - pos_F) > pos_tol:  # Define some_tolerance as needed
            pos = read_adc(PITCH_POT_PATH)
            output_c = controller.compute(pos)
            if output_c > 0:
                out_gpio("gpiochip0", M4_DIR_PIN, 1)
                pitch_M4.set_pwm_dc("pwmchip0", M4_CHANNEL, output_c)
            elif output_c < 0:
                out_gpio("gpiochip0", M4_DIR_PIN, 0)
                pitch_M4.set_pwm_dc("pwmchip0", M4_CHANNEL, abs(output_c))

    pitch_M4.enable_pwm_channel(M4_PATH, False)  # Disable PWM channel to stop motor
    
    break  #exit condition to break the main loop
