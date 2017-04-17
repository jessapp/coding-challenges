class TempTracker(object):
    
    def __init__(self):
        
        # For Min and Max
        self.min_temp = None
        self.max_temp = None
        
        # For Mode
        self.all_temps = []
        
        # For Mean
        self.current_total = 0.0
        self.total_values = 0
    
    def insert(self, temperature):
        if self.min_temp is None or temperature < self.min_temp:
            self.min_temp = temperature
        if self.max_temp is None or temperature > self.max_temp:
            self.max_temp = temperature 
        
        self.current_total += temperature
        self.total_values += 1
        self.all_temps.append(temperature)
            
    def get_max(self):
        return self.max_temp
    
    def get_min(self):
        return self.min_temp
    
    def get_mean(self):
        mean = float(self.current_total / self.total_values)
        return mean
    
    def get_mode(self):
        temp_tracker = {}
        
        for temp in self.all_temps:
            temp_tracker[temp] = temp_tracker.get(temp, 0) + 1
        
        max_count = 0
        mode = None
        for temp, count in temp_tracker.items():
            if count >= max_count:
                mode = temp
        
        return mode