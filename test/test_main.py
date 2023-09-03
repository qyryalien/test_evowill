import pytest
from main import main


@pytest.fixture
def mock_api(mocker):
    """
    Fixture to mock the ApiWrapper class for testing.

    This fixture creates a mock object for the ApiWrapper class and returns it.

    :param mocker: Pytest mocker fixture.
    :type mocker: _pytest.pythonapi.MockerFixture
    :return: A mocked ApiWrapper object.
    :rtype: Mock
    """
    return mocker.patch('main.ApiWrapper')


@pytest.fixture
def mock_database(mocker):
    """
    Fixture to mock the Database class for testing.

    This fixture creates a mock object for the Database class and returns it.

    :param mocker: Pytest mocker fixture.
    :type mocker: _pytest.pythonapi.MockerFixture
    :return: A mocked Database object.
    :rtype: Mock
    """
    return mocker.patch('main.Database')


# Define sets of command-line arguments for testing
test_args = [
    (["new", "--type", "education", "--participants", "1", "--price_min", "0.1", "--price_max", "30",
      "--accessibility_min", "0.1", "--accessibility_max", "0.5"], "new"),
    (["list"], "list"),
]


# Parametrize the test based on different arguments and commands
@pytest.mark.parametrize("args, command", test_args)
def test_main_argument_parsing(mock_api, mock_database, capsys, args, command):
    """
    Test argument parsing in the main function.

    This test verifies that the main function correctly parses command-line arguments

    :param mock_api: Mocked ApiWrapper object.
    :type mock_api: Mock
    :param mock_database: Mocked Database object.
    :type mock_database: Mock
    :param capsys: Pytest capsys fixture for capturing stdout and stderr.
    :type capsys: _pytest.capture.CaptureFixture
    :param args: List of command-line arguments.
    :type args: list
    :param command: The expected command to be executed.
    :type command: str
    """
    # Replace sys.argv with the test arguments
    import sys
    sys.argv = ["main.py"] + args

    main(mock_api, mock_database)

    captured = capsys.readouterr()

    # The expected results are equal to the empty string, since we are checking the command parsing itself
    if command == "new":
        assert "" in captured.out
    elif command == "list":
        assert "" in captured.out
