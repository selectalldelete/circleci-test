import unittest
from app import app

class TestResponse(unittest.TestCase):
    def test_response(self):
        # Using flask's test client
        self.test_app = app.test_client()

        # Test response to conf app with fake number
        response = self.test_app.get('/')
        
        # Assert 200 OK
        self.assertEquals(response.status_code, 200)

        # Assert proper test response
        assert b'Hello World' in response.data