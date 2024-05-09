from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

from generator import electricity_reading_generator

class TestElectricityReadingGenerator(TestCase):
    def test_generate_electricity_readings(self):
        # Test generating electricity readings
        generated = electricity_reading_generator.generate_electricity_readings(10)
        # Assert the number of generated readings is as expected
        self.assertEqual(len(generated), 10)
        # Assert each generated reading meets the criteria
        for r in generated:
            # Assert the year of the generated reading is the current year
            self.assertEqual(datetime.fromtimestamp(r['time']).year,  datetime.now().year)
            # Assert the reading is greater than or equal to 0
            self.assertGreaterEqual(r['reading'], 0)
            # Assert the reading is less than or equal to 1
            self.assertLessEqual(r['reading'], 1)

    def test_return_two_digit_number_for_single_digit_number(self):
        # Test return a two-digit number for a single-digit number
        with patch('random.randrange', return_value=9):
            # Patching random.randrange to return 9
            self.assertEqual(electricity_reading_generator.random_int_between(0, 1), '09')

    def test_return_two_digit_number_for_two_digit_number(self):
        # Test return a two-digit number for a two-digit number
        with patch('random.randrange', return_value=11):
            # Patching random.randrange to return 11
            self.assertEqual(electricity_reading_generator.random_int_between(0, 1), '11')
