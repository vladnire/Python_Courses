from datetime import date, datetime
from unittest.mock import Mock


tuesday = datetime(year=2019, month=1, day=1)
saturday = datetime(year=2019, month=1, day=5)

datetime = Mock()
def is_weekday():
    today = datetime.today()
    day_of_the_week = today.weekday()
    # 0 Monday, 6 Sunday
    return (0 <= day_of_the_week < 5)

datetime.today.return_value = saturday
assert is_weekday()