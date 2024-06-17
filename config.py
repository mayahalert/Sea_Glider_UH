#configure macros for peripherals and pins

ROLL_POT_PATH = "/sys/bus/iio/devices/iio:device0/in_voltage0_raw"
PITCH_POT_PATH = "/sys/bus/iio/devices/iio:device0/in_voltage1_raw"
ADC_REF_PATH = "/sys/bus/iio/devices/iio:device0/in_voltage2_raw"

PWM_CHIP_BASE = "/sys/class/pwm/pwmchip0/"
PWM_PERIOD_NS = 1000000  # 1ms (1kHz)
PWM_DC_NS = 250000  # 25% duty cycle

M4_CHANNEL = "pwm0"  # P8_19
M3_CHANNEL = "pwm1"  # P8_13
M4_PATH = f"{PWM_CHIP_BASE}{M4_CHANNEL}"
M3_PATH = f"{PWM_CHIP_BASE}{M3_CHANNEL}"

M3_DIR_PIN = 75  # P8_14
M4_DIR_PIN = 51  # P8_26

ADC_MIN = 55 # Minimum ADC value for potentiometer
ADC_MAX = 2000  # Maximum ADC value for potentiometer