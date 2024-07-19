class testData:
  def __init__self(,filename =None):
    self.log_entries = [] # initialize empty list for log entries
    self.filename = filename #optional filename for output data defined in test
  

def log(self,label,value)
self.log_entries.append((label,value)) #associate label and value pair

# for filename optional
if self.filename:
  with open(self.filename, 'a') as f:
    f.write(f"{label}: {value}\n") #write label and value to file

def subscribe(self):
  #return copy of listed log entries (label,value) tuples.
  return self.log_entries.copy()

#instead of tuples format labels and values in columns
 def subscribe(self):
      # Initialize an empty string 
        log_str = ""
        
        # Iterate over each (label, value) pair in log_entries
        for label, value in self.log_entries:
            # Format the label and value in columns
            log_str += f"{value:<10} {label}\n"
        
        # Return the formatted string
        return log_str
