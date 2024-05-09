from domain.electricity_reading import ElectricityReading  # Importing the ElectricityReading class

class ElectricityReadingService:
    def __init__(self, repository):
        # Initializing ElectricityReadingService with a repository
        self.electricity_reading_repository = repository

    def store_reading(self, json):
        # Extracting electricity readings from JSON and converting them to ElectricityReading objects
        readings = list(map(lambda x: ElectricityReading(x), json['electricityReadings']))
        # Storing the readings associated with the smart meter ID in the repository
        return self.electricity_reading_repository.store(json['smartMeterId'], readings)

    def retrieve_readings_for(self, smart_meter_id):
        # Retrieving readings associated with a specific smart meter ID from the repository
        return self.electricity_reading_repository.find(smart_meter_id)
