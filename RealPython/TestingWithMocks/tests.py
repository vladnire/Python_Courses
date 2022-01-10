from unittest.mock import patch
from my_calendar import requests, get_holidays
from requests.exceptions import Timeout
import unittest

class TestCalendar(unittest.TestCase):

    # @patch('my_calendar.requests')
    # def test_get_holidays_timeout(self, mocked_requests):
    #     mocked_requests.get.side_effect = Timeout
    #     with self.assertRaises(Timeout):
    #         get_holidays()

    # def test_get_holidays_timeout(self):
    #     with patch('my_calendar.requests') as mocked_requests:
    #         mocked_requests.get.side_effect = Timeout
    #         with self.assertRaises(Timeout):
    #             get_holidays()

    # def test_get_holidays_timeout(self):
    #     with patch.object(requests, 'get', side_effect=Timeout) as _:
    #         with self.assertRaises(Timeout):
    #             get_holidays()

    @patch.object(requests, 'get', side_effect=Timeout)
    def test_get_holidays_timeout(self, mocked_get):
            with self.assertRaises(Timeout):
                get_holidays()


if __name__ == '__main__':
    unittest.main()