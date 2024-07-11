#Create a Logger Class: Define a Logger class in utils/logger.py that handles writing data to a file.
# utils/logger.py

class Logger:
  #In utils/logger.py, the Logger class is defined with an __init__ method that takes output_file as an argument.
    def __init__(self, output_file): 
        self.output_file = output_file
#The log method of Logger writes the provided title and data to the specified output_file
    def log(self, title, data):
        with open(self.output_file, 'a') as f:
            f.write(f"=== {title} ===\n")
            f.write(f"{data}\n\n")


