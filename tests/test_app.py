from flask_testing import TestCase

from app import app


class SiteTest(TestCase):
    """
    Extend TestCase with flask app instantiation
    """

    def create_app(self):
        app.config['TESTING'] = True
        return app


class RootEndpoint(SiteTest):
    """
    Test cases for the root endpoint and error handling
    """

    def test_response_code(self):
        """
        Check the root path responds with 200 OK
        """

        response = self.client.get('/')
        self.assert200(response)

    def test_response_content(self):
        """
        Check the root path responds with hello world json
        """

        response = self.client.get('/')
        self.assertEquals(response.json, {"hello": "world"})
