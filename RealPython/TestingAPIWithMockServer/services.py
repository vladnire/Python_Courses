# Standard library imports...
from urllib.parse import urljoin

# Third-party imports...
import requests

# Local imports...
from constants import BASE_URL


USERS_URL = urljoin(BASE_URL, 'users')


def get_users():
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    return None