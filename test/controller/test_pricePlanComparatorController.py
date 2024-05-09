import unittest

from repository.price_plan_repository import price_plan_repository
from controller.electricity_reading_controller import repository as readings_repository
from app_initializer import initialize_data
from service.time_converter import iso_format_to_unix_time

from .setup_test_app import app

class TestPricePlanComparatorController(unittest.TestCase):
    def setUp(self):
        # Set up the test client and initialize data
        self.client = app.test_client()
        initialize_data()

    def tearDown(self):
        # Clean up repositories after each test
        price_plan_repository.clear()
        readings_repository.clear()

    def test_get_costs_against_all_price_plans(self):
        # Test getting costs against all price plans for a smart meter
        res = self.client.get('/price-plans/compare-all/smart-meter-1')
        # Assert response status code is 200 (Success)
        self.assertEqual(res.status_code, 200)
        # Assert the returned price plan ID matches the expected value
        self.assertEqual(res.get_json()['pricePlanId'], 'price-plan-1')
        # Assert the length of price plan comparisons matches the expected value
        self.assertEqual(len(res.get_json()['pricePlanComparisons']), 3)

    def test_recommend_cheapest_price_plans_no_limit_for_meter_usage(self):
        # Test recommending cheapest price plans for a meter with no usage limit
        readings = [
            { "time": iso_format_to_unix_time('2020-01-05T10:30:00'), "reading": 35.0 },
            { "time": iso_format_to_unix_time('2020-01-05T11:00:00'), "reading": 5.0 }
        ]

        readingJson = {
            "smartMeterId": "meter-103",
            "electricityReadings": readings
        }

        # Store electricity readings for meter-103
        self.client.post('/readings/store', json=readingJson)
        # Get recommended price plans for meter-103
        res = self.client.get('/price-plans/recommend/meter-103')
        # Assert response status code is 200 (Success)
        self.assertEqual(res.status_code, 200)
        # Assert the returned recommended price plans match the expected values
        self.assertEqual(res.get_json(), [
            { "price-plan-2": 40 },
            { "price-plan-1": 80 },
            { "price-plan-0": 400 }
        ])
