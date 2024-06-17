#*******work in progress dont test yet********
from config import *
from control.PD_controller import PDController
from hardware.adc import read_adc

pos_I = read_adc(PITCH_POT_PATH)
controller = PDController(Kp=1, Kd=1, setpoint=900)

if pos_I < 1000:
    setpoint = ADC_MIN + 10 #add a little saftey margin to the stop limit value measured earlier
    controller.set_setpoint(setpoint)
    while pos_I < setpoint:
        pos = read_adc(PITCH_POT_PATH)
        output_c = controller.compute(pos)


else:
    setpoint = ADC_MAX - 10
    controller.set_setpoint(setpoint)