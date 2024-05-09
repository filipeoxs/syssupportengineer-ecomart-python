from flask import abort

# Importing necessary modules and classes
from repository.electricity_reading_repository import ElectricityReadingRepository
from service.electricity_reading_service import ElectricityReadingService

# Creating an instance of ElectricityReadingRepository
repository = ElectricityReadingRepository()

# Creating an instance of ElectricityReadingService with the repository instance
service = ElectricityReadingService(repository)

# Function to store electricity reading data
def store(data):
    # Calling the store_reading method of the ElectricityReadingService instance
    service.store_reading(data)
    # Returning the stored data
    return data

# Function to retrieve electricity readings for a given smart meter ID
def read(smart_meter_id):
    # Retrieving readings for the given smart meter ID using the ElectricityReadingService instance
    readings = service.retrieve_readings_for(smart_meter_id)
    
    # If no readings are found for the given smart meter ID, return HTTP status code 404
    if len(readings) < 1:
        abort(404)
    else:
        # If readings are found, convert each reading to JSON format and return as a list
        return [r.to_json() for r in readings]
