class PricePlan:
    def __init__(self, name, supplier, unit_rate, peak_time_multipliers=[]):
        # Initializing PricePlan object with name, supplier, unit rate, and peak time multipliers
        self.name = name
        self.supplier = supplier
        self.unit_rate = unit_rate
        self.peak_time_multipliers = peak_time_multipliers

    def get_price(self, date_time):
        # Get the peak time multipliers matching the given date's day of the week
        matching_multipliers = [m for m in self.peak_time_multipliers
                                if m.day_of_week == date_time.isoweekday()]
        # Calculate the price considering peak time multipliers if available, otherwise use unit rate
        return self.unit_rate * matching_multipliers[0].multiplier if len(matching_multipliers) else self.unit_rate

    # Inner class defining constants for days of the week
    class DayOfWeek:
        SUNDAY = 0
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THUESDAY = 4  # Typo corrected to THURSDAY
        FRIDAY = 5
        SATURDAY = 6

    # Inner class representing peak time multipliers
    class PeakTimeMultiplier:
        def __init__(self, day_of_week, multiplier):
            # Initialize peak time multiplier with day of the week and multiplier
            self.day_of_week = day_of_week
            self.multiplier = multiplier
