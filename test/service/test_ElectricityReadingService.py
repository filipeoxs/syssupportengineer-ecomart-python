from unittest import TestCase
from unittest.mock import MagicMock

from domain.electricity_reading import ElectricityReading
from repository.electricity_reading_repository import ElectricityReadingRepository
from service.electricity_reading_service import ElectricityReadingService
from service.time_converter import iso_format_to_unix_time

class TestElectricityReadingService(TestCase):
    def setUp(self):
        # Set up the test environment
        self.repository = ElectricityReadingRepository()
        # Mock the store method of the repository
        self.repository.store = MagicMock()
        # Create an instance of ElectricityReadingService with the mocked repository
        self.electricity_reading_service = ElectricityReadingService(self.repository)

    def test_call_repository_to_store_readings(self):
        # Test calling repository to store readings
        json = {
            "smartMeterId": "meter-45",
            "electricityReadings": [
                {"time": iso_format_to_unix_time('2015-03-02T08:55:00'), "reading": 0.812},
                {"time": iso_format_to_unix_time('2015-09-02T08:55:00'), "reading": 0.23}
            ]
        }

        # Call the store_reading method of the ElectricityReadingService
        self.electricity_reading_service.store_reading(json)

        # Assert the store method of the repository is called with the expected arguments
        self.repository.store.assert_called_with('meter-45', [
            ElectricityReading(
                {"time": iso_format_to_unix_time('2015-03-02T08:55:00'), "reading": 0.812}),
            ElectricityReading(
                {"time": iso_format_to_unix_time('2015-09-02T08:55:00'), "reading": 0.23})
        ])
