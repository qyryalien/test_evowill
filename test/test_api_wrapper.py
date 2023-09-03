import pytest
from api_wrapper import ApiWrapper

import json


class MockHttpRequestHandler:
    def __init__(self):
        """
        Initialize the MockHttpRequestHandler.

        This class simulates HTTP requests to external APIs
        by providing mock responses based on specified URL and parameters.
        """
        self.responses = {
            'https://www.boredapi.com/api/activity': {
                None: {
                    "activity": "Learn Express.js",
                    "type": "education",
                    "participants": 1,
                    "price": 0.1,
                    "link": "https://expressjs.com/",
                    "key": "3943509",
                    "accessibility": 0.1
                },
                json.dumps({'type': 'fun'}): {
                    "activity": "Have fun!",
                    "type": "fun",
                    "participants": 2,
                    "price": 0.2,
                    "link": "https://fun.com/",
                    "key": "123456",
                    "accessibility": 0.5
                },
                json.dumps({'participants': 3}): {
                    "activity": "Team building",
                    "type": "team",
                    "participants": 3,
                    "price": 0.3,
                    "link": "https://team-building.com/",
                    "key": "789012",
                    "accessibility": 0.7
                },
                json.dumps({'price': 0.5}): {
                    "activity": "Expensive activity",
                    "type": "luxury",
                    "participants": 2,
                    "price": 0.5,
                    "link": "https://luxury.com/",
                    "key": "999999",
                    "accessibility": 0.1
                },
                json.dumps({'key': '777777'}): {
                    "activity": "Special key activity",
                    "type": "special",
                    "participants": 1,
                    "price": 0.3,
                    "link": "https://special.com/",
                    "key": "777777",
                    "accessibility": 0.5
                },
            }
        }

    def get(self, url, params=None):
        """
        Simulate a GET request to a specified URL with optional parameters.

        :param url: The URL to which the GET request is made.
        :type url: str
        :param params: Optional parameters for the GET request, defaults to None.
        :type params: dict, optional

        :return: A tuple containing the mock response and a status code.
        :rtype: tuple
        """
        # Check if the specified URL exists in the responses dictionary.
        if url in self.responses:
            # Check if parameters were provided or are None.
            if params is None:
                params_str = None
            else:
                # Convert the parameters to a JSON string to make them hashable.
                params_str = json.dumps(params)
            # Check if the JSON representation of parameters exists in the URL's responses.
            if params_str in self.responses[url]:
                # Return the mock response along with a status code of 200 (OK).
                return self.responses[url][params_str], 200

        # Return None and a status code of 404 (Not Found) for all other cases.
        return None, 404


@pytest.fixture
def api_with_mock_handler():
    """
    Fixture to create an ApiWrapper object with a mock HttpRequestHandler.

    This fixture creates an ApiWrapper instance with a mock HttpRequestHandler and returns it for testing purposes.

    :return: An ApiWrapper instance with a mock HttpRequestHandler.
    :rtype: ApiWrapper
    """
    http_handler = MockHttpRequestHandler()
    api = ApiWrapper(http_handler)
    return api


def test_get_random_activity(api_with_mock_handler):
    """
    Test the get_random_activity method with a mock HttpRequestHandler.

    This test verifies that the get_random_activity method of the ApiWrapper class
    works as expected with a mock HttpRequestHandler.

    :param api_with_mock_handler: An ApiWrapper instance with a mock HttpRequestHandler.
    :type api_with_mock_handler: ApiWrapper
    """
    api = api_with_mock_handler
    response, status_code = api.get_random_activity()

    expected_response = {
        "activity": "Learn Express.js",
        "type": "education",
        "participants": 1,
        "price": 0.1,
        "link": "https://expressjs.com/",
        "key": "3943509",
        "accessibility": 0.1
    }

    expected_status_code = 200  # Ожидаемый статус-код

    assert response == expected_response
    assert status_code == expected_status_code


# Тестирование метода get_random_activity с фильтром "type": "fun"
def test_get_random_activity_with_type_filter(api_with_mock_handler):
    """
    Test the get_random_activity method with a "type" filter.

    This test verifies that the get_random_activity method of the ApiWrapper class
    correctly applies a "type" filter when fetching a random activity.

    :param api_with_mock_handler: An ApiWrapper instance with a mock HttpRequestHandler.
    :type api_with_mock_handler: ApiWrapper
    """
    api = api_with_mock_handler
    response, status_code = api.get_random_activity(filters={"type": "fun"})

    expected_response = {
        "activity": "Have fun!",
        "type": "fun",
        "participants": 2,
        "price": 0.2,
        "link": "https://fun.com/",
        "key": "123456",
        "accessibility": 0.5
    }

    expected_status_code = 200

    assert response == expected_response
    assert status_code == expected_status_code


def test_get_random_activity_with_participants_filter(api_with_mock_handler):
    """
    Test the get_random_activity method with an invalid filter.

    This test verifies that the get_random_activity method of the ApiWrapper class
    correctly applies a "participants" filter when fetching a random activity.

    :param api_with_mock_handler: An ApiWrapper instance with a mock HttpRequestHandler.
    :type api_with_mock_handler: ApiWrapper
    """
    api = api_with_mock_handler
    response, status_code = api.get_random_activity(filters={"participants": 3})

    expected_response = {
        "activity": "Team building",
        "type": "team",
        "participants": 3,
        "price": 0.3,
        "link": "https://team-building.com/",
        "key": "789012",
        "accessibility": 0.7
    }

    expected_status_code = 200

    assert response == expected_response
    assert status_code == expected_status_code


# Тестирование метода get_random_activity с фильтром "price": 0.5
def test_get_random_activity_with_price_filter(api_with_mock_handler):
    """
    Test the get_random_activity method with an invalid filter.

    This test verifies that the get_random_activity method of the ApiWrapper class
    correctly applies a "price" filter when fetching a random activity.

    :param api_with_mock_handler: An ApiWrapper instance with a mock HttpRequestHandler.
    :type api_with_mock_handler: ApiWrapper
    """
    api = api_with_mock_handler
    response, status_code = api.get_random_activity(filters={"price": 0.5})

    expected_response = {
        "activity": "Expensive activity",
        "type": "luxury",
        "participants": 2,
        "price": 0.5,
        "link": "https://luxury.com/",
        "key": "999999",
        "accessibility": 0.1
    }

    expected_status_code = 200

    assert response == expected_response
    assert status_code == expected_status_code


def test_get_random_activity_with_key_filter(api_with_mock_handler):
    """
    Test the get_random_activity method with an invalid filter.

    This test verifies that the get_random_activity method of the ApiWrapper class
    correctly applies a "key" filter when fetching a random activity.

    :param api_with_mock_handler: An ApiWrapper instance with a mock HttpRequestHandler.
    :type api_with_mock_handler: ApiWrapper
    """
    api = api_with_mock_handler
    response, status_code = api.get_random_activity(filters={"key": "777777"})

    expected_response = {
        "activity": "Special key activity",
        "type": "special",
        "participants": 1,
        "price": 0.3,
        "link": "https://special.com/",
        "key": "777777",
        "accessibility": 0.5
    }

    expected_status_code = 200

    assert response == expected_response
    assert status_code == expected_status_code


def test_get_random_activity_with_invalid_filter(api_with_mock_handler):
    """
    Test the get_random_activity method with an invalid filter.

    This test verifies that the get_random_activity method of the ApiWrapper class
    handles an invalid filter gracefully and returns the expected result.

    :param api_with_mock_handler: An ApiWrapper instance with a mock HttpRequestHandler.
    :type api_with_mock_handler: ApiWrapper
    """
    api = api_with_mock_handler
    response, status_code = api.get_random_activity(filters={"invalid_filter": "value"})

    assert response is None
    assert status_code == 404
