from datetime import datetime  # Importing datetime module to work with dates and times

# Function to convert ISO format string to UNIX timestamp
def iso_format_to_unix_time(iso_format_string):
    # Converting ISO format string to datetime object and passing it to __unix_time_of function
    return __unix_time_of(datetime.fromisoformat(iso_format_string))

# Function to calculate UNIX timestamp from datetime object
def __unix_time_of(dt):
    # Calculating the total seconds elapsed since epoch (1970-01-01) and returning as an integer
    return int((dt - datetime(1970, 1, 1)).total_seconds())

# Function to calculate time elapsed in hours given earliest and latest UNIX timestamps
def time_elapsed_in_hours(earliest_unix_timestamp, latest_unix_timestamp):
    # Calculating time difference in seconds and converting it to hours
    return (latest_unix_timestamp - earliest_unix_timestamp) / 3600
