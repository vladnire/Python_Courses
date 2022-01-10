import requests
from datetime import datetime

def is_weekday():
    today = datetime.today()
    day_of_the_week = today.weekday()
    # 0 Monday, 6 Sunday
    return (0 <= day_of_the_week < 5)


def get_holidays():
    r = requests.get('https://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()

    return None
