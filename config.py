#configure macros for peripherals and pins

#analog sensor paths
ROLL_POT_PATH = "/sys/bus/iio/devices/iio:device0/in_voltage0_raw"
PITCH_POT_PATH = "/sys/bus/iio/devices/iio:device0/in_voltage1_raw"
ADC_REF_PATH = "/sys/bus/iio/devices/iio:device0/in_voltage2_raw"

#I2C


#pwm driver paths
PWM_CHIP_BASE = "/sys/class/pwm/pwmchip0/"
PWM_PERIOD_NS = 1000000  # 1ms (1kHz)
PWM_DC_MAX_NS = 850000  # set max allowable duty cycle to 85%

M4_CHANNEL = "pwm0"  # P8_19
M3_CHANNEL = "pwm1"  # P8_13
M4_PATH = f"{PWM_CHIP_BASE}{M4_CHANNEL}" #concatenate strings for full channel path
M3_PATH = f"{PWM_CHIP_BASE}{M3_CHANNEL}"

M3_DIR_PIN = 75  # P8_14
M4_DIR_PIN = 51  # P8_26

#safety limits for potentiometers in raw adc values
ROLL_POT_MAX = 2000
ROLL_POT_MIN = 100

PITCH_POT_MAX = 2000
PITCH_POT_MIN = 100
