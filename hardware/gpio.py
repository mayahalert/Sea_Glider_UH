# module to control GPIO pins on the BBAI64
# probably more efficient way to contorl GPIO pins than using the built-in functions this way in the terminal
# ********* need to test before using********
import subprocess #for interacting with the shell

def out_gpio(chip, pin, value):
    command = f"gpioset {chip} {pin}={value}"
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Set GPIO{pin} on {chip} to {value}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set GPIO{pin}: {e}")
