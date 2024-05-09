from service.time_converter import iso_format_to_unix_time  # Importing iso_format_to_unix_time function from time_converter module
import math  # Importing math module for mathematical operations
import random  # Importing random module for generating random numbers
import datetime  # Importing datetime module for working with dates and times

# Function to generate a random integer between min_val and max_val
def random_int_between(min_val, max_val):
    return "%02d" % random.randrange(min_val, max_val)

# Function to get a time delta object with the given number of seconds
def get_timedelta(sec=60):
    return datetime.timedelta(seconds=sec)

# Function to generate electricity readings
def generate_electricity_readings(num):
    readings = []  # List to store generated readings
    for i in range(num):
        # Generating a random time in ISO format, decrementing by i*60 seconds each iteration
        random_time = (datetime.datetime.now() - get_timedelta(i*60)).isoformat()
        # Generating a random reading between 0 and 1 (exclusive)
        random_reading = math.floor(random.random() * 1000)/1000
        # Converting the random time to UNIX timestamp format and adding it to readings along with the random reading
        readings.append({"time": iso_format_to_unix_time(random_time), "reading": random_reading})

    return readings  # Returning the generated readings
