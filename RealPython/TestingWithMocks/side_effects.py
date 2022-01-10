from datetime import date, datetime
from unittest.mock import Mock
from requests.exceptions import ConnectionError
import unittest

requests = Mock()

tuesday = datetime(year=2019, month=1, day=1)
saturday = datetime(year=2019, month=1, day=5)

datetime = Mock()
def is_weekday():
    today = datetime.today()
    day_of_the_week = today.weekday()
    # 0 Monday, 6 Sunday
    return (0 <= day_of_the_week < 5)

datetime.today.return_value = saturday
assert not is_weekday()


def get_holidays():
    r = requests.get('https://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()

    return None


class TestGetHolidays(unittest.TestCase):

    def test_get_holidays_connection(self):
        requests.get.side_effect = ConnectionError
        with self.assertRaises(ConnectionError):
            get_holidays()

    def test_get_holidays_timeout(self):
        requests.get.side_effect = TimeoutError
        with self.assertRaises(TimeoutError):
            get_holidays()

    def log_request(self, url):
        print(f'Making a request to {url}')
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '25/12': 'Christmas',
            '01/01': 'New Year'
        }

        return response_mock

    def test_request_with_logging(self):
        requests.get.call_count = 0
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '25/12': 'Christmas',
            '01/01': 'New Year'
        }
        requests.get.side_effect = [TimeoutError, response_mock]
        with self.assertRaises(TimeoutError):
            get_holidays()
        assert get_holidays()['25/12'] == 'Christmas'
        assert requests.get.call_count == 2


if __name__ == '__main__':
    unittest.main()