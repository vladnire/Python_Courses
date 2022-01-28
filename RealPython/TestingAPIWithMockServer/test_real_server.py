# Local imports...
from services import get_users


def test_request_response():
    response = get_users()

    assert response.ok is True
    assert isinstance(response.json(), list)
    # In Python 3, you can use dict.items() to get a set-like view of the dict items. 
    # You can then use the <= operator to test if one view is a "subset" of the other:
    assert {'Content-Type': 'application/json; charset=utf-8'}.items() <= response.headers.items()