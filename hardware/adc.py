# module defining fucntion for reading ADC values from the ADC file in the sysfs filesystem on the BBAI64
def read_adc(path):
    try:
        with open(path, 'r') as adc_file:
            return float(adc_file.read().strip())
    except IOError as e:
        print(f"Failed to read ADC value from {path}: {e}")
        return None
