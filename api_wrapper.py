import requests

URL = 'https://www.boredapi.com/api/activity'


class HttpRequestHandler:
    def get(self, url, params=None):
        """
        Send an HTTP GET request to the specified URL with optional query parameters.

        :param url: The URL to send the GET request to.
        :type url: str
        :param params: (Optional) Dictionary of query parameters.
        :type params: dict or None
        :return: JSON response from the GET request or None if the response status code is not 200.
        :rtype: dict or None
        """

        # Processing HTTP GET request with parameters
        response = requests.get(url, params=params)
        return response.json() if response.status_code == 200 else None


class ApiWrapper:
    def __init__(self, http_handler):
        """
        Initialize an object for working with the API.

        :param http_handler: Object for handling HTTP requests
        :type http_handler: HttpRequestHandler
        """
        self.http_handler = http_handler

    def get_random_activity(self, filters=None):
        """
        Get a random activity considering the specified filters.

        :param filters: Dictionary of filters for the request
        :type filters: dict or None
        :return: Information about a random activity
        :rtype: dict
        """

        # If a filters dictionary is provided, use it to create query parameters
        if filters:
            response = self.http_handler.get(URL, params=filters)
        else:
            response = self.http_handler.get(URL)

        return response
