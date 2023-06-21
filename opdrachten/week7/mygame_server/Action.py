class Action:

    def __init__(self, name, acceleration):
        self.name = name
        self.acceleration = acceleration

    def get_name(self):
        return self.name

    def get_acceleration(self):
        return self.acceleration
    
    def __repr__(self):
        return f"name: {self.name} acceleration:{self.acceleration}"
