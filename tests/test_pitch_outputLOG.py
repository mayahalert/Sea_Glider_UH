from config import *
from control.PD_controller import PDController
from hardware.adc import read_adc
from hardware.pwm import PWMController
from hardware.gpio import GPIOControl

# Initialize GPIO controller
gpio = GPIOControl()
gpio.setup_pin(351, direction='out', default_value=0)  # Setup pin 351 P8_26
gpio.setup_pin(375, direction='out', default_value=0)  # Setup pin 375 P8_14

# Read initial position of pitch motor
pos_I = read_adc(PITCH_POT_PATH)

# Initialize PD controller for pitch motor with gains
controller = PDController(Kp=1, Kd=1, setpoint=pos_I)

# Initialize PWM controller for pitch motor
pwm = PWMController(PWM_CHIP_BASE, PWM_PERIOD_NS)

pos_min, pos_max = None, None  # Initialize position variables
pos_tol = 5  # Define tolerance for position comparison

# Lists to store data metrics
positions = []
control_outputs = []

while True:
    # Drive to the stop limit closest to start position
    if pos_I < 1000 and pos_min is None:
        setpoint = ROLL_POT_MIN + 10
        controller.set_setpoint(setpoint)
        pos = read_adc(PITCH_POT_PATH)

        while PITCH_POT_MIN < pos < setpoint:
            pos = read_adc(PITCH_POT_PATH)
            output_c = controller.compute(pos)
            if output_c > 0:
                gpio.set_value(M4_DIR_PIN, 1)  # Set direction pin to high
                pwm.set_pwm_dc(M4_PATH, output_c)
            elif output_c < 0:
                gpio.set_value(M4_DIR_PIN, 0)  # Set direction pin to low
                pwm.set_pwm_dc(M4_PATH, abs(output_c))
            pos_min = pos  # Update pos_min

            # Logging metrics
            positions.append(("pos_min", pos))
            control_outputs.append(("pos_min_output", output_c))

    # Drive to the opposite stop limit
    if pos_I > 1000 and pos_max is None:
        pos = read_adc(PITCH_POT_PATH)
        setpoint = ROLL_POT_MAX - 10
        controller.set_setpoint(setpoint)

        while setpoint < pos < PITCH_POT_MAX:
            pos = read_adc(PITCH_POT_PATH)
            output_c = controller.compute(pos)
            if output_c > 0:
                gpio.set_value(M4_DIR_PIN, 1)
                pwm.set_pwm_dc(M4_PATH, output_c)
            elif output_c < 0:
                gpio.set_value(M4_DIR_PIN, 0)
                pwm.set_pwm_dc(M4_PATH, abs(output_c))
            pos_max = pos  # Update pos_max

            # Logging metrics
            positions.append(("pos_max", pos))
            control_outputs.append(("pos_max_output", output_c))

    # Drive to the midpoint of the total pitch travel
    if pos_min is not None and pos_max is not None:
        pos_F = (pos_max + pos_min) / 2
        controller.set_setpoint(pos_F)

        while abs(pos - pos_F) > pos_tol:
            pos = read_adc(PITCH_POT_PATH)
            output_c = controller.compute(pos)
            if output_c > 0:
                gpio.set_value(M4_DIR_PIN, 1)
                pwm.set_pwm_dc(M4_PATH, output_c)
            elif output_c < 0:
                gpio.set_value(M4_DIR_PIN, 0)
                pwm.set_pwm_dc(M4_PATH, abs(output_c))

            # Logging metrics
            positions.append(("pos_midpoint", pos))
            control_outputs.append(("pos_midpoint_output", output_c))

    pwm.set_pwm_dc(M4_PATH, 0)  # Disable PWM channel to stop motor

    # Output useful data metrics with labels
    print("Positions:")
    for label, value in positions:
        print(f"{label}: {value}")

    print("Control Outputs:")
    for label, value in control_outputs:
        print(f"{label}: {value}")

    break  # Exit condition to break the main loop
