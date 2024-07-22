class testData:

  #modify filename to current .py script and concatenate with timestamp so that the filename is not optional
  def __init__self(self, filename = None):
    if filename is None:
      #oull filename from test script and add timestamp
      script_name = os.path.splitext(os.path.basename(__file__))[0]  # Get current script filename without extension
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Generate timestamp
        self.filename = f"{script_name}_{timestamp}.txt"  # Combine script name and timestamp to form filename
    else:
      self.filename = filename
      
        self.log_entries = []  # initialize empty list for log entries

def log(self,label,value)
self.log_entries.append((label,value)) # appen (label, value) tuple to log_entries

# for filename optional
if self.filename:
  with open(self.filename, 'a') as f:
    f.write(f"{label}: {value}\n") #write label and value to file

 def subscribe(self):
      # Initialize an empty string 
        log_str = ""
        # Iterate over each (label, value) pair in log_entries
        for label, value in self.log_entries:
            # Format the label and value in columns
            log_str += f"{value:<10} {label}\n"
        # Return the formatted string
        return log_str
