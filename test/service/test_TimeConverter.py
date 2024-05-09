from unittest import TestCase

from service.time_converter import iso_format_to_unix_time, time_elapsed_in_hours


class TestTimeConverter(TestCase):

    def test_iso_format_to_unix_time(self):
        # Test iso_format_to_unix_time function
        # Test conversion for epoch time (0 seconds)
        self.assertEqual(iso_format_to_unix_time('1970-01-01T00:00:00'), 0)
        # Test conversion for 1 hour and 1 second after epoch time
        self.assertEqual(iso_format_to_unix_time('1970-01-01T01:00:01'), 3601)
        # Test conversion for a specific date and time
        self.assertEqual(iso_format_to_unix_time('2020-02-29T23:12:41'), 1583017961)

    def test_calculate_elapsed_time_in_hours_from_two_unix_timestamps(self):
        # Test time_elapsed_in_hours function
        # Set up two Unix timestamps representing a time interval of 30 minutes
        earlier = iso_format_to_unix_time('2018-05-24T11:30:00')
        later = iso_format_to_unix_time('2018-05-24T12:00:00')

        # Calculate the elapsed time in hours between the two timestamps
        self.assertEqual(time_elapsed_in_hours(earlier, later), 0.5)
