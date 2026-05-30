class Counter:
    def __init__(self, initial_value = 0):
        self.count = initial_value
    
    @classmethod
    def from_string(cls, value_str):
        return cls(initial_value = int(value_str))
    
    @property
    def value(self):
        return self.count
    
    def increment(self, amount = 1):
        self.count += amount

    def reset(self):
        self.count = 0

    
