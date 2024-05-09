from flask import abort

# Importing necessary modules and classes
from service.account_service import AccountService
from service.price_plan_service import PricePlanService

# Importing readings_repository from the local module
from .electricity_reading_controller import repository as readings_repository

# Function to compare spend against price plans for a given smart meter ID
def compare(smart_meter_id):
    # Creating an instance of PricePlanService with the readings_repository
    price_plan_service = PricePlanService(readings_repository)
    
    # Creating an instance of AccountService
    account_service = AccountService()
    
    # Getting a list of spend against each price plan for the given smart meter ID
    list_of_spend_against_price_plans = price_plan_service.get_list_of_spend_against_each_price_plan_for(smart_meter_id)

    # If no spend data is available, return HTTP status code 404
    if len(list_of_spend_against_price_plans) < 1:
        abort(404)
    else:
        # If spend data is available, return a dictionary containing price plan ID and spend comparisons
        return {
            "pricePlanId": account_service.get_price_plan(smart_meter_id),
            "pricePlanComparisons": list_of_spend_against_price_plans
        }

# Function to recommend price plans for a given smart meter ID
def recommend(smart_meter_id, limit=None):
    # Creating an instance of PricePlanService with the readings_repository
    price_plan_service = PricePlanService(readings_repository)
    
    # Getting a list of spend against each price plan for the given smart meter ID with an optional limit
    list_of_spend_against_price_plans = price_plan_service.get_list_of_spend_against_each_price_plan_for(smart_meter_id, limit=limit)
    
    # Reversing the list of spend against price plans
    return list_of_spend_against_price_plans.reverse()
