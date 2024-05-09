from functools import reduce  # Importing reduce function from functools module

# Importing price_plan_repository from the repository.price_plan_repository module
from repository.price_plan_repository import price_plan_repository

# Importing ElectricityReadingService and time_elapsed_in_hours from the local modules
from .electricity_reading_service import ElectricityReadingService
from .time_converter import time_elapsed_in_hours


# Function to calculate the total time elapsed between the earliest and latest readings
def calculate_time_elapsed(readings):
    # Extracting the minimum and maximum time from the readings
    min_time = min(map(lambda r: r.time, readings))
    max_time = max(map(lambda r: r.time, readings))
    # Calculating the time elapsed in hours using the time_elapsed_in_hours function
    return time_elapsed_in_hours(min_time, max_time)


class PricePlanService:
    def __init__(self, reading_repository):
        # Initializing PricePlanService with an instance of ElectricityReadingService
        self.electricity_reading_service = ElectricityReadingService(reading_repository)

    # Method to get a list of spend against each price plan for a given smart meter ID
    def get_list_of_spend_against_each_price_plan_for(self, smart_meter_id, limit=None):
        # Retrieving electricity readings for the given smart meter ID
        readings = self.electricity_reading_service.retrieve_readings_for(smart_meter_id)
        # If no readings are available, return an empty list
        if len(readings) < 1:
            return []

        # Calculating average reading consumption
        average = self.calculate_average_reading(readings)
        # Calculating total time elapsed
        time_elapsed = calculate_time_elapsed(readings)
        # Calculating consumed energy per hour
        consumed_energy = average / time_elapsed

        # Getting all price plans from the repository
        price_plans = price_plan_repository.get()

        # Function to calculate the cost from a price plan
        def cost_from_plan(price_plan):
            cost = {}
            cost[price_plan.name] = consumed_energy * price_plan.unit_rate
            return cost
        
        # Mapping the cost_from_plan function to each price plan and storing the result in a list
        list_of_spend = list(map(cost_from_plan, self.cheapest_plans_first(price_plans)))

        # Returning the list of spend against each price plan, limited by the given limit
        return list_of_spend[:limit]

    # Method to sort price plans by unit rate in ascending order
    def cheapest_plans_first(self, price_plans):
        return list(sorted(price_plans, key=lambda plan: plan.unit_rate))

    # Method to calculate the average reading consumption
    def calculate_average_reading(self, readings):
        # Using reduce to sum up all readings and then calculate the average
        sum = reduce((lambda p, c: p + c), map(lambda r: r.reading, readings), 0)
        return (sum * 2) / len(readings)
