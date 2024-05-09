from dataclasses import dataclass

# Defining a dataclass named ElectricityReading
@dataclass
class ElectricityReading:
    # Declaring attributes: time (int) and reading (float)
    time: int
    reading: float

    # Constructor to initialize the attributes from a JSON object
    def __init__(self, json):
        # Assigning the 'time' attribute from the JSON object
        self.time = json['time']
        # Assigning the 'reading' attribute from the JSON object
        self.reading = json['reading']

    # Method to convert the ElectricityReading object to JSON format
    def to_json(self):
        # Returning a dictionary with 'time' and 'reading' keys
        return {
            'time': self.time,
            'reading': self.reading,
        }
