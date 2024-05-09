class AccountService:
    # Dictionary mapping smart meter IDs to price plan IDs
    plan_ids_by_meter = {
        "smart-meter-0": "price-plan-0",
        "smart-meter-1": "price-plan-1",
        "smart-meter-2": "price-plan-0",
        "smart-meter-3": "price-plan-2",
        "smart-meter-4": "price-plan-1",
    }

    # Method to get the price plan associated with a smart meter ID
    def get_price_plan(self, smart_meter_id):
        # Retrieve and return the price plan ID for the given smart meter ID from the dictionary
        return self.plan_ids_by_meter[smart_meter_id]
