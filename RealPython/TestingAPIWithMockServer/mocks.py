# Standard library imports...
import socket
import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

# Third-party imports...
import requests


class MockServerRequestHandler(BaseHTTPRequestHandler):
    """
    This class captures the request and constructs the response to return
    Override the do_GET() function to craft the response for 
    an HTTP GET request. In this case, just return an OK status.
    """
    USERS_PATTERN = re.compile(r'/users')

    def do_GET(self):
        """
        """
        if re.search(self.USERS_PATTERN, self.path):
            # Add response status code
            self.send_response(requests.codes.ok)

            # Add response headers
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            
            # Add response contant
            response_content = json.dumps([])
            self.wfile.write(response_content.encode('utf-8'))
            return


def get_free_port():
    """Get an available port number for the mock server to use."""
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    address, port = s.getsockname()
    s.close()
    return port


def start_mock_server(port):
    mock_server = HTTPServer(
            ('localhost', port), 
            MockServerRequestHandler)
    mock_server_thread = Thread(target=mock_server.serve_forever)
    mock_server_thread.daemon = True
    mock_server_thread.start()