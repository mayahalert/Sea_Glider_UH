class PDController:
    def __init__(self, Kp, Kd, setpoint):
        self.Kp = Kp  # Proportional gain
        self.Kd = Kd  # Derivative gain
        self.setpoint = setpoint  # Target setpoint
        self.last_input = 0.0  # Last input value (for derivative calculation)
        self.output = 0.0  # Control output

    def compute(self, input_value):
        # Calculate error
        error = self.setpoint - input_value
        
        # Calculate derivative of the input
        delta_input = input_value - self.last_input
        
        # Compute the proportional term
        proportional_term = self.Kp * error
        
        # Compute the derivative term
        derivative_term = self.Kd * delta_input
        
        # Calculate the control output
        self.output = proportional_term + derivative_term
        
        # Update last input
        self.last_input = input_value
        
        return self.output

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint

    def set_gains(self, Kp, Kd):
        self.Kp = Kp
        self.Kd = Kd

    def get_output(self):
        return self.output

