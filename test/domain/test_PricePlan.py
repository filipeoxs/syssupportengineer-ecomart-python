from datetime import datetime
from unittest import TestCase

from domain.price_plan import PricePlan

class TestPricePlan(TestCase):
    def test_return_the_base_price_given_an_off_peak_date_time(self):
        # Test return the base price given an off-peak date time
        peak_time_multiplier = PricePlan.PeakTimeMultiplier(PricePlan.DayOfWeek.WEDNESDAY, 10)
        off_peak_time = datetime(2000, 1, 1, 11, 11, 11)

        # Create a PricePlan instance with a peak time multiplier
        plan = PricePlan('plan-name', 'supplier-name', 1, [ peak_time_multiplier ])

        # Get the price for the off-peak time
        price = plan.get_price(off_peak_time)

        # Assert the price matches the base price
        self.assertEqual(price, 1)

    def test_return_a_peak_price_given_a_datetime_matching_peak_day(self):
        # Test return a peak price given a datetime matching peak day
        peak_time_multiplier = PricePlan.PeakTimeMultiplier(PricePlan.DayOfWeek.WEDNESDAY, 10)
        peak_time = datetime(2000, 1, 5, 11, 11, 11)

        # Create a PricePlan instance with a peak time multiplier
        plan = PricePlan('plan-name', 'supplier-name', 1, [ peak_time_multiplier ])

        # Get the price for the peak time
        price = plan.get_price(peak_time)

        # Assert the price matches the peak price
        self.assertEqual(price, 10)
