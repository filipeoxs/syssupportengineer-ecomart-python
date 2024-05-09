class ElectricityReadingRepository:
    def __init__(self):
        # Initializing the ElectricityReadingRepository object with an empty dictionary to store readings
        self.meter_associated_readings = {}

    # Method to store readings associated with a smart meter ID
    def store(self, smart_meter_id, readings):
        # Check if the smart meter ID already exists in the repository
        if smart_meter_id in self.meter_associated_readings:
            # If it exists, get the existing list of readings
            existing_list_of_readings = self.meter_associated_readings.get(smart_meter_id)
            # Update the readings by concatenating the existing and new readings
            self.meter_associated_readings[smart_meter_id] = readings + existing_list_of_readings
        else:
            # If the smart meter ID does not exist, simply store the readings
            self.meter_associated_readings[smart_meter_id] = readings

    # Method to find readings associated with a smart meter ID
    def find(self, smart_meter_id):
        # Check if the smart meter ID exists in the repository
        if smart_meter_id in self.meter_associated_readings:
            # If it exists, return the associated readings
            return self.meter_associated_readings[smart_meter_id]
        else:
            # If it does not exist, return an empty list
            return []

    # Method to clear all readings from the repository
    def clear(self):
        # Clear all readings by resetting the repository to an empty dictionary
        self.meter_associated_readings = {}
