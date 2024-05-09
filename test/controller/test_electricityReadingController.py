import unittest

from .setup_test_app import app  # Importing the Flask app instance for testing

class TestElectricityReadingController(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.client = app.test_client()

    def test_successfully_add_the_reading_against_new_smart_meter_id(self):
        # Test adding a reading for a new smart meter ID
        readingJson = {
            "smartMeterId": "meter-11",
            "electricityReadings": [
                {"time": 1505825656, "reading": 0.6}
            ]
        }

        # Send POST request to store readings
        response = self.client.post('/readings/store', json=readingJson)
        # Assert the response status code is 200 (Success)
        self.assertEqual(200, response.status_code)

    def test_successfully_add_the_reading_against_existing_smart_meter_id(self):
        # Test adding readings for an existing smart meter ID
        readingJson1 = {
            "smartMeterId": "meter-100",
            "electricityReadings": [
                { "time": 1505825838, "reading": 0.6 },
                { "time": 1505825848, "reading": 0.65 },
            ]
        }

        readingJson2 = {
            "smartMeterId": "meter-100",
            "electricityReadings": [
                { "time": 1605825849, "reading": 0.7 }
            ]
        }

        # Send POST requests to store readings
        self.client.post('/readings/store', json=readingJson1)
        self.client.post('/readings/store', json=readingJson2)
        # Retrieve readings for the smart meter ID
        readings = self.client.get('/readings/read/meter-100').get_json()
        # Assert the readings are stored correctly
        self.assertIn({"time": 1505825838, "reading": 0.6 }, readings)
        self.assertIn({"time": 1505825848, "reading": 0.65 }, readings)
        self.assertIn({"time": 1605825849, "reading": 0.7}, readings)

    def test_respond_with_error_if_smart_meter_id_not_set(self):
        # Test response with error if smart meter ID is not set
        readingJson = {
            "electricityReadings": [
                { "time": 1505825838, "reading": 0.6 }
            ]
        }

        # Assert an Exception is raised when sending POST request without smartMeterId
        with self.assertRaises(Exception):
            self.client.post('/readings/store', json=readingJson)

    def test_respond_with_error_if_electricity_readings_not_set(self):
        # Test response with error if electricity readings are not set
        readingJson = {
            "smartMeterId": "meter-11"
        }

        # Assert an Exception is raised when sending POST request without electricityReadings
        with self.assertRaises(Exception):
            self.client.post('/readings/store', json=readingJson)
