class PricePlanRepository:
    def __init__(self):
        # Initializing the PricePlanRepository object with an empty list to store price plans
        self.price_plans = []

    # Method to store new price plans
    def store(self, new_price_plans):
        # Adding the new price plans to the existing list of price plans
        self.price_plans += new_price_plans

    # Method to get a copy of all price plans
    def get(self):
        # Returning a copy of the list of price plans to avoid modifying the original list
        return self.price_plans.copy()

    # Method to clear all price plans
    def clear(self):
        # Clearing all price plans by resetting the list to an empty list
        self.price_plans = []


# Creating an instance of PricePlanRepository and assigning it to price_plan_repository variable
price_plan_repository = PricePlanRepository()
