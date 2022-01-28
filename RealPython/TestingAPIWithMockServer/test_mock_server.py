# Third-party imports 
from unittest.mock import patch

# Local imports...
from services import get_users
from mocks import get_free_port, start_mock_server


class TestMockServer():
    @classmethod
    def setup_class(cls):
        # Configure mock server.
        cls.mock_server_port = get_free_port()
        start_mock_server(cls.mock_server_port)

    def test_request_response(self):
        mock_users_url  = f"http://localhost:{self.mock_server_port}/users"

        # Patch USERS_URL so that the service uses the mock server URL instead of the real URL.
        with patch.dict('services.__dict__', {'USERS_URL': mock_users_url}):
            response = get_users()

        assert response.ok is True
        assert response.json() == []
        assert {'Content-Type': 'application/json; charset=utf-8'}.items() <= response.headers.items()